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


# parsers operate on non-binary data -- integers or strings
# 
# wherever possible, these are shared by registers and the persist library

from jbdEnums import (Dsgoc2Enum, Dsgoc2DelayEnum,
                        ScEnum, ScDelayEnum, CuvpHighDelayEnum, 
                        CovpHighDelayEnum, LabelEnum)

import struct

class BaseParser: pass

def SafeFloat(v):
    try:
        return float(v)
    except ValueError:
        return 0.0
class IntParserX1(BaseParser):
    'encodes or decodes a single integer'
    factor = 1

    @staticmethod
    def UtoS(v): # unsigned --> signed
        return struct.unpack('>h', struct.pack('>H',int(v)))[0]

    @staticmethod
    def StoU(v): # signed --> unsigned
        return struct.unpack('>H', struct.pack('>h',int(v)))[0]

    @classmethod
    def decode(cls, string):
        # fileformat stores int16_t as uint16_t
        # need to convert to signed
        v = cls.UtoS(string)
        return (v * cls.factor,)

    @classmethod
    def encode(cls, values):
        value = SafeFloat(values[0])
        return cls.StoU(value / cls.factor)

class IntParserX10(IntParserX1):
    factor = 10

class IntParserD10(IntParserX1):
    factor = .1

class ScParser(BaseParser):
    @staticmethod
    def decode(string):
        i = int(string)
        sc = i & 0x7
        sc_delay = (i >> 3) & 0x3
        sc_dsgoc_x2 = bool(i & 0x80)
        return ScEnum.byValue(sc), ScDelayEnum.byValue(sc_delay), sc_dsgoc_x2

    @staticmethod
    def encode(values):
        sc, sc_delay, sc_dsgoc_x2 = values
        i = sc_delay.val << 3
        i |= sc.val
        i |= (0x80 if sc_dsgoc_x2 else 0)
        return i

class Dsgoc2Parser(BaseParser):
    @staticmethod
    def decode(string):
        i = int(string)
        dsgoc2 = i & 0xF
        dsgoc2_delay = i >> 4
        return Dsgoc2Enum.byValue(dsgoc2), Dsgoc2DelayEnum.byValue(dsgoc2_delay)

    @staticmethod
    def encode(values):
        dsgoc2, dsgoc2_delay = values
        i = dsgoc2.val | (dsgoc2_delay.val << 4)
        return i

    
class BitfieldParser(BaseParser):
    @staticmethod
    def decode(value):
        value = int(value)
        return [bool(value & (1 << i)) for i in range(16)]
    
    @staticmethod
    def encode(values):
        r = 0
        for i, value in enumerate(values):
            r |= (1<<i) if value else 0
        return r

class CxvpDelayParser(BaseParser):
    @staticmethod
    def decode(value):
        i = int(value)
        covp_high_delay = (i >> 6) & 0x3
        cuvp_high_delay = (i >> 4) & 0x3
        return (CovpHighDelayEnum.byValue(covp_high_delay), 
                CuvpHighDelayEnum.byValue(cuvp_high_delay))

    @staticmethod
    def encode(values):
        covp_high_delay, cuvp_high_delay = values
        i = (covp_high_delay.val & 0x3) << 6
        i |= (cuvp_high_delay.val & 0x3) << 4
        return i

class DateParser(BaseParser):
    @staticmethod
    def decode(value):
        value = int(value)
        day = value & 0x1f
        value >>= 5
        month = value & 0xf
        value >>= 4
        year = (value & 0x7f) + 2000
        return year, month, day

    @staticmethod
    def encode(values):
        year, month, day = (int(SafeFloat(i)) for i in values)
        year = max(min(year, 2128), 2000)
        month = max(min(month, 12), 1)
        day = max(min(day, 31), 1)
        value = (year - 2000) & 0x7f
        value <<= 4
        value |= month
        value <<= 5
        value |= day
        return value

class TempParser(IntParserX1):
    @classmethod
    def decode(cls, value):
        value = int(value)
        return ((value - 2731) / 10,)

    @classmethod
    def encode(cls, values):
        value = int(values[0])
        return int(value * 10 + 2731)


class StrParser(BaseParser):
    'encodes or decodes a single string'
    @staticmethod
    def decode(string):
        return (str(string),)

    @staticmethod
    def encode(values):
        if type(values) not in (tuple, list):
            values = (values,)
        return str(values[0])