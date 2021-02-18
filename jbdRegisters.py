#!/usr/bin/env python

# BMS Tools
# Copyright (C) 2020 Eric Poulsen
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from jbdParsers import *
from jbdEnums import *
import struct

class BaseReg:
    'register base class; mostly exists for documenting methods and properties'

    @property 
    def regName(self):
        'get name of register'
        return self._regName

    @property
    def valueNames(self):
        'return a list of values this register covers'
        return self._valueNames

    def __repr__(self):
        return f'<{self.__class__.__name__}: {self.regName}>'

    @property
    def unit(self, valueName):
        'return the unit for this value'
        raise NotImplementedError()

    @property
    def adx(self):
        'get the address of the register'
        return self._adx

    def get(self, valueName):
        'return a single value'
        raise NotImplementedError()

    def set(self, valueName, value):
        'set a single value'
        raise NotImplementedError()

    def unpack(self, payload):
        'extract value(s) from register payload and store internally'
        raise NotImplementedError()

    def pack(self):
        'return a device-compatible payload from the current value(s)'
        raise NotImplementedError()

    def __getitem__(self, valueName):
        return self.get(valueName)
       
    def __setitem__(self, valueName, value):
        return self.set(valueName, value)

    def _toDict(self):
        return {k:self.get(k) for k in self.valueNames}

    def keys(self):
        return self._toDict().keys()

    def values(self):
        return self._toDict().values()

    def items(self):
        return self._toDict().items()

class ReadOnlyException(RuntimeError): pass
class ReadOnlyMixin:
    def set(self, valueName, value):
        raise ReadOnlyException(f'{self._regName} is read-only')

    def pack(self):
        raise ReadOnlyException(f'{self._regName} is read-only')

class IntReg(BaseReg): 
    def __init__(self, regName, adx, unit, factor, range=(-32768, 32768)):
        self._regName = regName
        self._adx = adx
        self._unit = unit
        self._value = 0
        self._factor = factor # multiplier for (un)packing
        assert type(range) in (list, tuple) and len(range) == 2 and all([type(i) == int for i in range])
        self.range = tuple((i * factor for i in range))
        if self.range[0] >= 0:
            self.format = '>H'
        else:
            self.format = '>h'

    @property
    def valueNames(self):
        return [self._regName]
    
    @property
    def unit(self, valueName):
        if not valueName == self._regName:
            raise KeyError(f'unknown value name {valueName}')
        return self._unit

    def get(self, valueName): 
        if not valueName == self._regName:
            raise KeyError(f'unknown value name {valueName}')
        return self._value
    
    def set(self, valueName, value):
        if not valueName == self._regName:
            raise KeyError(f'unknown value name {valueName}')
        value = value or 0
        try:
            value = float(value)
            if value < self.range[0] or value > self.range[1]:
                raise ValueError(f'value {repr(value)} is outside of range {self.range}')
        except Exception as e:
            raise ValueError(f'value {repr(value)} is not valid for {self.__class__.__name__}')
        self._value = value

    def unpack(self, payload):
        self._value = struct.unpack(self.format, payload)[0] * self._factor

    def pack(self):
        return struct.pack(self.format, int(self._value // self._factor))

    def __str__(self):
        return f'{self._regName}: {self._value}'

class TempReg(IntReg):
    'actual temperatures on device are stored as Kelvin * 10'
    def __init__(self, valueName, adx):
        super().__init__(valueName, adx, Unit.C, 0)

    def set(self, valueName, value):
        if not valueName == self._regName:
            raise KeyError(f'unknown value name {valueName}')
        try:
            value = float(value)
            if not -273.15 <= value <= 6136.4: # maps to 0 --> 65535
                raise ValueError(f'value {repr(value)} is outside of range(-32768, 327670)')
        except:
            raise ValueError(f'value {repr(value)} is not valid for {self.__class__.__name__}')
        self._value = value
    
    def unpack(self, payload):
        value = struct.unpack('>H', payload)[0]
        self._value = TempParser.decode(value)[0]

    def pack(self):
        value = TempParser.encode((self._value,))
        return struct.pack('>H', value)

class TempRegRO(TempReg, ReadOnlyMixin): pass

class ErrorCountReg(ReadOnlyMixin, BaseReg):
    def __init__(self, regName, adx):
        self._regName = regName
        self._adx = adx

        valueNames = 'sc chgoc dsgoc covp cuvp chgot chgut dsgot dsgut povp puvp'.split()
        self._values = {n+'_err_cnt':0 for n in valueNames}

    @property
    def valueNames(self):
        return list(self._values.keys())
    
    @property
    def unit(self):
        return int

    def __str__(self):
        return f'{self._regName}: ' + ', '.join(f'{k}: {v}' for k,v in self._values.items())
    
    def get(self, valueName):
        return self._values[valueName]
    
    def unpack(self, payload):
        valueCount = len(self._values)
        bmsValueCount = len(payload) // 2
        values = struct.unpack(f'>{bmsValueCount}H', payload)

        self._values = dict(zip(self._values.keys(), values[:valueCount]))

class DelayReg(BaseReg):
    'class that deals with registers that store two time values, in seconds'

    def __init__(self, regName, adx, name1, name2):
        self._regName = regName
        self._adx = adx
        self._values = {name1: 0, name2: 0}

    def get(self, valueName):
        return self._values[valueName]

    def set(self, valueName, value):
        if valueName not in self._values:
            raise KeyError(valueName)
        value = value or 0
        try:
            value = int(value)
            if not 0 <= value <= 255:
                raise ValueError(f'value {repr(value)} is outside of range(0, 255)')
        except:
            raise ValueError(f'value {repr(value)} is not valid for {self.__class__.__name__}')
        self._values[valueName] = value

    def __str__(self):
        return ', '.join(f'{k}: {v}' for k,v in self._values.items())

    @property
    def valueNames(self):
        return list(self._values.keys())

    def unpack(self, payload):
        values = struct.unpack('>2B', payload)
        self._values = dict(zip(self._values.keys(), values))

    def pack(self):
        return struct.pack('>2B', *self._values.values())


class BitfieldReg(BaseReg):
    def __init__(self, regName, adx, *fields):
        'fields are in order, from bit 0'
        self._regName = regName
        self._adx = adx
        self._values = {f:False for f in fields}

    @property
    def valueNames(self):
        return list(self._values.keys())
        
    def get(self, valueName):
        return self._values[valueName]
    
    def set(self, valueName, value):
        if valueName not in self._values:
            raise KeyError(valueName)
        self._values[valueName] = bool(value)

    def unpack(self, payload):
        values = BitfieldParser.decode(struct.unpack('>H', payload)[0])
        values = values[:len(self.valueNames)]

        for k,v in zip(self._values.keys(), values):
            self._values[k] = v

    def pack(self):
        value = BitfieldParser.encode(self._values.values())
        return struct.pack('>H', value)

class StringReg(BaseReg):
    def __init__(self, regName, adx, maxLen = 31):
        self._regName = regName
        self.maxLen = maxLen
        self._adx = adx
        self._value = ''

    @property
    def valueNames(self):
        return [self._regName]

    def get(self, valueName):
        if not valueName == self._regName:
            raise KeyError(f'unknown value name {valueName}')
        return self._value

    def set(self, valueName, value):
        if not valueName == self._regName:
            raise KeyError(f'unknown value name {valueName}')

        if type(value) not in (str, bytes, bytearray):
            raise ValueError(f'value should be str, byte, or bytearray')
        if len(value) > self.maxLen:
            raise ValueError(f'string length should not exceed {self.maxLen}')

        self._value = value

    def pack(self):
        l = len(self._value)
        return struct.pack(f'>B{l}s', l, bytes(self._value, 'utf-8'))

    def unpack(self, payload):
        l = payload[0]
        l = min(l, self.maxLen)
        self._value = str(payload[1:1+l], 'utf-8')

    def __str__(self):
        return f'{self._regName}: {self._value}'

class DateReg(BaseReg):
    _valueNames = ('year', 'month', 'day')
    def __init__(self, regName, adx):
        self._regName = regName
        self._adx = adx
        self._year = 0
        self._month = 0
        self._day = 0
        self._yearRange = range(2000,2128)
        self._monthRange = range(1,13)
        self._dayRange = range(1,32)

    def get(self, valueName):
        if valueName not in self._valueNames:
            raise KeyError(valueName)
        return getattr(self, '_'+valueName)
    
    def set(self, valueName, value):
        if valueName not in self._valueNames:
            raise KeyError(valueName)
        value = int(value)
        if value not in getattr(self, f'_{valueName}Range'):
            raise ValueError(f'invalid value for {valueName}: {repr(value)}')
        setattr(self, '_'+valueName, value)

    def __str__(self):
        return f'{self._year}-{self._month}-{self._day}'

    def unpack(self, payload):
        value = struct.unpack('>H', payload)[0]
        self._year, self._month, self._day = DateParser.decode(value)
    
    def pack(self):
        return struct.pack('>H', DateParser.encode((self._year, self._month, self._day)))

class ScDsgoc2Reg(BaseReg):
    _valueNames = ('sc', 'sc_delay', 'dsgoc2', 'dsgoc2_delay', 'sc_dsgoc_x2')
    def __init__(self, regName, adx):
        self._regName = regName
        self._adx = adx
        self._sc = ScEnum._22MV
        self._sc_delay = ScDelayEnum._70US
        self._dsgoc2 = Dsgoc2Enum._8MV
        self._dsgoc2_delay = Dsgoc2DelayEnum._8MS
        self._sc_dsgoc_x2 = False
    
    def get(self, valueName):
        if valueName not in self._valueNames:
            raise KeyError(valueName)
        return getattr(self, '_'+valueName)

    def set(self, valueName, value):
        if valueName == 'sc':
            if  value not in ScEnum:
                raise ValueError(value)
            self._sc = value
        elif valueName == 'sc_delay':
            if value not in ScDelayEnum:
                raise ValueError(value)
            self._sc_delay = value
        elif valueName == 'dsgoc2':
            if value not in Dsgoc2Enum:
                raise ValueError(value)
            self._dsgoc2 = value
        elif valueName == 'dsgoc2_delay':
            if value not in Dsgoc2DelayEnum:
                raise ValueError(value)
            self._dsgoc2_delay = value
        elif valueName == 'sc_dsgoc_x2':
            self._sc_dsgoc_x2 = bool(value)
        else:
            raise KeyError(valueName)

    def unpack(self, payload):
        b1, b2 = struct.unpack('>BB', payload)

        self._sc, self._sc_delay, self._sc_dsgoc_x2 = ScParser.decode(b1)
        self._dsgoc2, self._dsgoc2_delay = Dsgoc2Parser.decode(b2)

    def pack(self):
        b1 = ScParser.encode((self._sc, self._sc_delay, self._sc_dsgoc_x2))
        b2 = Dsgoc2Parser.encode((self._dsgoc2, self._dsgoc2_delay))
        return struct.pack('>BB', b1, b2)


class CxvpHighDelayScRelReg(BaseReg):
    _valueNames = ('cuvp_high_delay', 'covp_high_delay', 'sc_rel')
    def __init__(self, regName, adx):
        self._regName = regName
        self._adx = adx

        self._cuvp_high_delay = CuvpHighDelayEnum._1S
        self._covp_high_delay = CovpHighDelayEnum._1S
        self._sc_rel = 0

    def get(self, valueName):
        if valueName not in self._valueNames:
            raise KeyError(valueName)
        return getattr(self, '_'+valueName)

    def set(self, valueName, value):
        if valueName == 'cuvp_high_delay':
            if value not in CuvpHighDelayEnum:
                raise ValueError(value)
            self._cuvp_high_delay = value
        elif valueName == 'covp_high_delay':
            if value not in CovpHighDelayEnum:
                raise ValueError(value)
            self._covp_high_delay = value
        elif valueName == 'sc_rel':
            value = value or 0
            value = int(value)
            if value not in range(256):
                raise ValueError(value)
            self._sc_rel = value
        else:
            raise KeyError(valueName)

    def unpack(self, payload):
        b1, self._sc_rel= struct.unpack('>BB', payload)
        self._covp_high_delay, self._cuvp_high_delay = CxvpDelayParser.decode(b1)
    
    def pack(self):
        b1 = CxvpDelayParser.encode((self._cuvp_high_delay, self._covp_high_delay))
        return struct.pack('>BB', b1, self._sc_rel)

class BasicInfoReg(BaseReg):
    _balBits = [f'bal{i}' for i in range(32)]
    _faultBits = [f'{i}_err' for i in 'covp cuvp povp puvp chgot chgut dsgot dsgut chgoc dsgoc sc afe software'.split() ]
    _ntcFields = [f'ntc{i}' for i in range(8)]
    _fetBits = 'chg_fet_en', 'dsg_fet_en'
    _valueNames = [
        'pack_mv', 'pack_ma', 'cur_cap', 
        'full_cap', 'cycle_cnt', 
        'year', 'month', 'day',
        *_balBits,
        *_faultBits,
        'version',
        'cap_pct',
        *_fetBits,
        'ntc_cnt',
        'cell_cnt',
        *_ntcFields,
        'fault_raw',
        'bal_raw'
    ]

    def __init__(self, regName, adx):
        self._regName = regName
        self._adx = adx
    
    def get(self, valueName):
        if valueName not in self._valueNames:
            raise KeyError(valueName)
        return getattr(self, '_'+valueName)

    @staticmethod
    def _unpackBits(fields, value):
        ret = []
        for bit, field in enumerate(fields):
            ret.append(('_'+field,  bool(value & (1 << bit))))
        return ret

    def unpack(self, payload):
        offset = 0
        fmt = '>HhHHHH'
        values = struct.unpack_from(fmt, payload, offset)
        self._pack_mv, self._pack_ma, self._cur_cap, self._full_cap, self._cycle_cnt, date_raw = values
        self._pack_mv *= 10
        self._pack_ma *= 10
        self._cur_cap *= 10
        self._full_cap *= 10
        self._year, self._month, self._day = DateParser.decode(date_raw)
        offset += struct.calcsize(fmt)

        fmt = '>HHHBBBBB'
        values = struct.unpack_from(fmt, payload, offset)
        bal_raw0, bal_raw1, self._fault_raw, self._version, self._cap_pct, fet_raw, self._cell_cnt, self._ntc_cnt = values
        self._bal_raw = bal_raw0 | (bal_raw1 << 16)
        for fn, value in self._unpackBits(self._balBits, self._bal_raw):
            setattr(self, fn, value)
        for fn, value in self._unpackBits(self._faultBits, self._fault_raw):
            setattr(self, fn, value)
        for fn, value in self._unpackBits(self._fetBits, fet_raw):
            setattr(self, fn, value)
        offset += struct.calcsize(fmt)

        for i in range(8):
            fn = f'_ntc{i}'
            if i < self._ntc_cnt:
                o = offset + i *2
                date_raw = struct.unpack_from('>H', payload,o)[0]
                setattr(self, fn, TempParser.decode(date_raw)[0])
            else:
                setattr(self, fn, None)

class CellInfoReg(BaseReg):
    def __init__(self, regName, adx):
        self._regName = regName
        self._adx = adx
        self._cellCnt = 0
        self._values = []

    @property
    def valueNames(self):
        return [f'cell{i}_mv' for i in range(self._cellCnt)]

    def unpack(self, payload):
        self._cellCnt = len(payload) // 2
        self._values = struct.unpack(f'>{self._cellCnt}H', payload)

    def get(self, valueName):
        if valueName not in self.valueNames:
            raise KeyError(valueName)

        d = ''.join([i for i in valueName if i.isdigit()])
        return self._values[int(d)]

class DeviceInfoReg(BaseReg):
    _valueNames = ['device_name']
    def __init__(self, regName, adx):
        self._regName = regName
        self._adx = adx

    def get(self, valueName):
        if valueName not in self._valueNames:
            raise KeyError(valueName)
        return getattr(self, '_'+valueName, None)

    def unpack(self, payload):
        try:
            self._device_name = str(payload, 'utf-8')
        except UnicodeDecodeError:
            self._device_name = payload
        
