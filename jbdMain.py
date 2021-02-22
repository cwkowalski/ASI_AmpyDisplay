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

import serial
import time
import struct
import threading
import sys
from enum import Enum
from functools import partial
from jbdPersist import JBDPersist

from jbdRegisters import (Unit, DateReg, IntReg,
                        TempReg, TempRegRO, DelayReg, 
                        ScDsgoc2Reg, CxvpHighDelayScRelReg,
                        BitfieldReg, StringReg, ErrorCountReg,
                        BasicInfoReg, CellInfoReg, DeviceInfoReg, ReadOnlyException)

__all__ = 'JBD'

class BMSError(Exception): pass

class JBD:
    START               = 0xDD
    END                 = 0x77
    READ                = 0xA5
    WRITE               = 0x5A

    CELL_CAL_REG_START  = 0xB0
    CELL_CAL_REG_END    = 0xCF

    NTC_CAL_REG_START   = 0xD0
    NTC_CAL_REG_END     = 0xD7

    I_CAL_IDLE_REG      = 0xAD
    I_CAL_CHG_REG       = 0xAE
    I_CAL_DSG_REG       = 0xAF

    CHG_DSG_EN_REG      = 0xE1
    BAL_CTRL_REG        = 0xE2

    CAP_REM_REG         = 0xE0

    def __init__(self, s, timeout = 1, debug = False):
        self.s = serial.Serial(s)
        try:
            self.s.close()
            s.timeout = timeout
        except: 
            pass
        self._open_cnt = 0
        #self._lock = threading.RLock()
        self.timeout = timeout
        self.debug = debug
        self.writeNVMOnExit = False

        self.eeprom_regs = [
            ### EEPROM settings
            ## Settings
            # Basic Parameters
            IntReg('covp', 0x24, Unit.MV, 1),
            IntReg('covp_rel', 0x25, Unit.MV, 1),
            IntReg('cuvp', 0x26, Unit.MV, 1),
            IntReg('cuvp_rel', 0x27, Unit.MV, 1),
            IntReg('povp', 0x20, Unit.MV, 10),
            IntReg('povp_rel', 0x21, Unit.MV, 10),
            IntReg('puvp', 0x22, Unit.MV, 10),
            IntReg('puvp_rel', 0x23, Unit.MV, 10),
            TempReg('chgot', 0x18),
            TempReg('chgot_rel', 0x19),
            TempReg('chgut', 0x1a),
            TempReg('chgut_rel', 0x1b),
            TempReg('dsgot', 0x1c),
            TempReg('dsgot_rel', 0x1d),
            TempReg('dsgut', 0x1e),
            TempReg('dsgut_rel', 0x1f),
            IntReg('chgoc', 0x28, Unit.MA, 10),
            IntReg('dsgoc', 0x29, Unit.MA, 10),
            DelayReg('cell_v_delays', 0x3d, 'cuvp_delay', 'covp_delay'),
            DelayReg('pack_v_delays', 0x3c, 'puvp_delay', 'povp_delay'),
            DelayReg('chg_t_delays', 0x3a, 'chgut_delay', 'chgot_delay'),
            DelayReg('dsg_t_delays', 0x3b, 'dsgut_delay', 'dsgot_delay'),
            DelayReg('chgoc_delays', 0x3e, 'chgoc_delay', 'chgoc_rel'),
            DelayReg('dsgoc_delays', 0x3f, 'dsgoc_delay', 'dsgoc_rel'),

            # High Protection Configuration
            IntReg('covp_high', 0x36, Unit.MV, 1),
            IntReg('cuvp_high', 0x37, Unit.MV, 1),
            ScDsgoc2Reg('sc_dsgoc2', 0x38),
            CxvpHighDelayScRelReg('cxvp_high_delay_sc_rel', 0x39),

            # Function Configuration
            BitfieldReg('func_config', 0x2d, 'switch', 'scrl', 'balance_en', 'chg_balance_en', 'led_en', 'led_num'),

            # NTC Configuration
            BitfieldReg('ntc_config', 0x2e, *(f'ntc{i+1}' for i in range(8))),

            # Balance Configuration
            IntReg('bal_start', 0x2a, Unit.MV, 1),
            IntReg('bal_window', 0x2b, Unit.MV, 1),

            # Other Configuration
            IntReg('shunt_res', 0x2c, Unit.MO, .1),
            IntReg('cell_cnt', 0x2f, int, 1),
            IntReg('cycle_cnt', 0x17, int, 1),
            IntReg('serial_num', 0x16, int, 1),
            StringReg('mfg_name', 0xa0),
            StringReg('device_name', 0xa1),
            StringReg('barcode', 0xa2),
            DateReg('mfg_date', 0x15),

            # Capacity Config
            IntReg('design_cap', 0x10, Unit.MAH, 10), 
            IntReg('cycle_cap', 0x11, Unit.MAH, 10),
            IntReg('dsg_rate', 0x14, Unit.PCT, .1), # presuming this means rate of self-discharge
            IntReg('cap_100', 0x12, Unit.MV, 1), # AKA "Full Chg Vol"
            IntReg('cap_80', 0x32, Unit.MV, 1),
            IntReg('cap_60', 0x33, Unit.MV, 1),
            IntReg('cap_40', 0x34, Unit.MV, 1),
            IntReg('cap_20', 0x35, Unit.MV, 1),
            IntReg('cap_0', 0x13, Unit.MV, 1), # AKA "End of Dsg VOL"
            IntReg('fet_ctrl', 0x30, Unit.S, 1),
            IntReg('led_timer', 0x31, Unit.S, 1),

            # Errors
            ErrorCountReg('error_cnts', 0xaa),
        ]
        self.eeprom_reg_by_valuename = {}
        for reg in self.eeprom_regs:
            map = {k:reg for k in reg.valueNames}
            self.eeprom_reg_by_valuename.update(map)

        self.basicInfoReg = BasicInfoReg('basic_info', 0x03)
        self.cellInfoReg = CellInfoReg('cell_info', 0x04)
        self.deviceInfoReg = DeviceInfoReg('device_info', 0x05)
    @staticmethod
    def toHex(data):
        return ' '.join([f'{i:02X}' for i in data])

    def dbgPrint(self, *args, **kwargs):
        kwargs['file'] = sys.stderr
        if self.debug:
            print(*args, **kwargs)

    @property
    def serial(self):
        return self.s
    
    @serial.setter
    def serial(self, s):
        s.timeout = .25
        self.s = s 

    def open(self):
        self._open_cnt += 1
        if self._open_cnt == 1:
            #self._lock.acquire()
            self.s.open()
            time.sleep(0.5)

    
    def close(self):
        if not self._open_cnt: 
            return
        self._open_cnt -= 1
        if not self._open_cnt:
            self.s.close()
            #self._lock.release()

    @staticmethod
    def chksum(payload):
        return 0x10000 - sum(payload)

    def extractPayload(self, data):
        assert len(data) >= 7
        datalen = data[3]
        data = data[4:4+datalen]
        self.dbgPrint('extractPayload returning', self.toHex(data))
        return data

    def cmd(self, op, reg, data):

        payload = [reg, len(data)] + list(data)
        chksum = self.chksum(payload)
        data = [self.START, op] + payload + [chksum, self.END]
        format = f'>BB{len(payload)}BHB'
        return struct.pack(format, *data) 

    def readCmd(self, reg, data  = []):
        return self.cmd(self.READ, reg, data)

    def writeCmd(self, reg, data = []):
        return self.cmd(self.WRITE, reg, data)

    def readPacket(self):
        then = time.time() + self.timeout
        self.dbgPrint(f'timeout is {self.timeout}')
        d = []
        msgLen = 0
        complete = False
        while then > time.time():
            byte = self.s.read()
            print('readPacket: byte:', byte)
            if not byte:
                print('not byte!')
                continue
            byte = byte[0]
            d.append(byte)
            if len(d) == 4:
                msgLen = d[-1]
            if byte == 0x77 and len(d) == 7 + msgLen: 
                complete = True
                break
        if d and complete:
            self.dbgPrint('readPacket:', self.toHex(d))
            ok = not d[2]
            return ok, self.extractPayload(bytes(d))
        self.dbgPrint(f'readPacket failed with {len(d)} bytes')
        return False, None

    def __enter__(self):
        self.open()
        self.enterFactory()

    def __exit__(self, type, value, traceback):
        self.exitFactory(self.writeNVMOnExit)
        self.writeNVMOnExit = False
        self.close()

    def factoryContext(self, writeNVMOnExit = False):
        self.writeNVMOnExit = writeNVMOnExit 
        return self

    def enterFactory(self):
        try:
            self.open()
            cnt = 5
            while cnt:
                cmd = self.writeCmd(0, [0x56, 0x78])
                self.s.write(cmd)
                ok, x = self.readPacket()
                if ok and x is not None: # empty payload is valid
                    self.dbgPrint('pong')
                    return x
                self.dbgPrint('no response')
                cnt -= 1
                time.sleep(.3)
            return False
        except Exception as e:
            print('JBD: enterFactory: Exception: ', e)
        finally:
            self.close()

    def exitFactory(self, writeNVM = False):
        try:
            self.open()
            cmd = self.writeCmd(1,  [0x28, 0x28] if writeNVM else [0,0])
            self.s.write(cmd)
            ok, d = self.readPacket()
            return ok
        finally:
            self.close()

    def readEeprom(self, progressFunc = None):
        with self.factoryContext():
            ret = {}
            numRegs = len(self.eeprom_regs)
            if progressFunc: progressFunc(0)

            for i, reg in enumerate(self.eeprom_regs):
                cmd = self.readCmd(reg.adx)
                self.s.write(cmd)
                ok, payload = self.readPacket()
                if not ok:
                    print('BMSError: ', ok, payload)
                    raise BMSError()
                if payload is None: raise TimeoutError()
                if progressFunc: progressFunc(int(i / (numRegs-1) * 100))
                reg.unpack(payload)
                ret.update(dict(reg))
            return ret

    def writeEeprom(self, data, progressFunc = None):
        with self.factoryContext(True):
            ret = {}
            numRegs = len(self.eeprom_regs)
            if progressFunc: progressFunc(0)
            regs = set()

            for valueName, value in data.items():
                reg = self.eeprom_reg_by_valuename.get(valueName)
                if not reg: raise RuntimeError(f'unknown valueName {valueName}')
                try:
                    reg.set(valueName, value)
                    regs.add(reg)
                except ReadOnlyException:
                    print(f'skipping read-only valueName {valueName}')

            for i,reg in enumerate(regs):
                data = reg.pack()
                cmd = self.writeCmd(reg.adx, data)
                self.s.write(cmd)
                ok, payload = self.readPacket()
                if not ok: raise BMSError()
                if payload is None: raise TimeoutError()
                if progressFunc: progressFunc(int(i / (numRegs-1) * 100))

    def loadEepromFile(self, filename):
        p = JBDPersist()
        with open(filename) as f:
            data = f.read()
        return p.deserialize(data)

    def saveEepromFile(self, filename, data):
        p = JBDPersist()
        with open(filename, 'wb') as f:
            f.write(p.serialize(data))

    def readInfo(self):
        try:
            self.open()
            basic = self.readBasicInfo()
            cell = self.readCellInfo()
            device = self.readDeviceInfo()
            return basic, cell, device
        finally:
            self.close()

    def readBasicInfo(self):
        #try:
        self.open()
        cmd = self.readCmd(self.basicInfoReg.adx)
        self.s.write(cmd)
        ok, payload = self.readPacket()
        if not ok:
            print('JBD: readBasicInfo: BMSError!')
            raise BMSError()
        if payload is None:
            print('JBD: readBasicInfo: Timeout error!')
            raise TimeoutError()
        self.basicInfoReg.unpack(payload)
        return dict(self.basicInfoReg)
        #finally:
        self.close()

    def readCellInfo(self):
        #try:
        print('JBD: readCellInfo begin')
        self.open()
        print('JBD: port opened:', self.s.isOpen())
        cmd = self.readCmd(self.cellInfoReg.adx)
        self.s.write(cmd)
        ok, payload = self.readPacket()
        if not ok: raise BMSError()
        if payload is None: raise TimeoutError()
        self.cellInfoReg.unpack(payload)
        return dict(self.cellInfoReg)
        #finally:
        self.close()

    def readDeviceInfo(self):
        try:
            self.open()
            cmd = self.readCmd(self.deviceInfoReg.adx)
            self.s.write(cmd)
            ok, payload = self.readPacket()
            if not ok: raise BMSError()
            if payload is None: raise TimeoutError()
            self.deviceInfoReg.unpack(payload)
            return dict(self.deviceInfoReg)
        finally:
            self.close()
    
    def clearErrors(self):
        with self.factoryContext(True):
            pass

    def calCell(self, cells, progressFunc = None):
        'cells is a dict of cell # (base 0) to mV'
        with self.factoryContext():
            cur = 0
            cnt = len(cells)
            for n, v in cells.items():
                adx = self.CELL_CAL_REG_START + n
                if adx > self.CELL_CAL_REG_END: continue
                reg = IntReg('cal', adx, Unit.MV, 1)
                reg.set('cal', v)
                cmd = self.writeCmd(adx, reg.pack())
                self.s.write(cmd)
                #print(' '.join(f'{i:02X}' for i in cmd))
                ok, payload = self.readPacket()
                if not ok: raise BMSError()
                if payload is None: raise TimeoutError()
                if progressFunc: progressFunc(cur / cnt)
                cur += 1

    def calNtc(self, ntc, progressFunc = None):
        'ntc is a dict of ntc # (base 0) to K'
        with self.factoryContext():
            cur = 0
            cnt = len(ntc)
            for n, v in ntc.items():
                adx = self.NTC_CAL_REG_START + n
                if adx > self.NTC_CAL_REG_END: continue
                reg = TempReg('cal', adx)
                reg.set('cal', v)
                cmd = self.writeCmd(adx, reg.pack())
                self.s.write(cmd)
                #print(' '.join(f'{i:02X}' for i in cmd))
                ok, payload = self.readPacket()
                if not ok: raise BMSError()
                if payload is None: raise TimeoutError()
                if progressFunc: progressFunc(cur / cnt)
                cur += 1

    def calIdleCurrent(self):
        with self.factoryContext():
            reg = IntReg('ma', self.I_CAL_IDLE_REG, Unit.MA, 10)
            reg.set('ma', 0)
            cmd = self.writeCmd(self.I_CAL_IDLE_REG, reg.pack())
            self.s.write(cmd)
            ok, payload = self.readPacket()
            if not ok: raise BMSError()
            if payload is None: raise TimeoutError()

    def calChgCurrent(self, value):
        with self.factoryContext(True):
            reg = IntReg('ma', self.I_CAL_CHG_REG, Unit.MA, 10)
            reg.set('ma', value)
            cmd = self.writeCmd(reg.adx, reg.pack())
            self.s.write(cmd)
            ok, payload = self.readPacket()
            if not ok: raise BMSError()
            if payload is None: raise TimeoutError()

    def calDsgCurrent(self, value):
        with self.factoryContext(True):
            reg = IntReg('ma', self.I_CAL_DSG_REG, Unit.MA, 10)
            reg.set('ma', value)
            cmd = self.writeCmd(reg.adx, reg.pack())
            self.s.write(cmd)
            ok, payload = self.readPacket()
            if not ok: raise BMSError()
            if payload is None: raise TimeoutError()

    def chgDsgEnable(self, chgEnable, dsgEnable):
        ce = 0 if chgEnable else 1
        de = 0 if dsgEnable else 1
        value = ce | (de << 1)
        with self.factoryContext():
            reg = IntReg('x', self.CHG_DSG_EN_REG, Unit.NONE, 1)
            reg.set('x', value)
            cmd = self.writeCmd(reg.adx, reg.pack())
            self.s.write(cmd)
            ok, payload = self.readPacket()
            if not ok: raise BMSError()
            if payload is None: raise TimeoutError()

    def balCloseAll(self):
        self._balTestWrite(3)
    
    def balOpenOdd(self):
        self._balTestWrite(1)

    def balOpenEven(self):
        self._balTestWrite(2)

    def balExit(self):
        with self: # enter / leave factory
            pass

    def _balTestWrite(self, value):
        # Intentionally don't exit factory here
        try:
            self.open()
            self.enterFactory()
            reg = IntReg('x', self.BAL_CTRL_REG, Unit.NONE, 1)
            reg.set('x', value)
            cmd = self.writeCmd(reg.adx, reg.pack())
            self.s.write(cmd)
            ok, payload = self.readPacket()
            if not ok: raise BMSError()
            if payload is None: raise TimeoutError()
        finally:
            self.close()

    def setPackCapRem(self, value):
        with self.factoryContext():
            reg = IntReg('mah', self.CAP_REM_REG, Unit.MAH, 10)
            reg.set('mah', value)
            cmd = self.writeCmd(reg.adx, reg.pack())
            self.s.write(cmd)
            ok, payload = self.readPacket()
            if not ok: raise BMSError()
            if payload is None: raise TimeoutError()

    def readIntReg(self, adx):
        with self.factoryContext():
            reg = IntReg('x', adx, Unit.NONE, 1)
            cmd = self.readCmd(reg.adx, reg.pack())
            self.s.write(cmd)
            ok, payload = self.readPacket()
            if not ok: raise BMSError()
            if payload is None: raise TimeoutError()
            reg.unpack(payload)
            return reg.get('x')

    def writeIntReg(self, adx, value):
        with self.factoryContext():
            reg = IntReg('x', adx, Unit.NONE, 1)
            reg.set('x', int(value))
            cmd = self.writeCmd(reg.adx, reg.pack())
            self.s.write(cmd)
            ok, payload = self.readPacket()
            if not ok: raise BMSError()
            if payload is None: raise TimeoutError()



def checkRegNames():
    jbd = JBD(None)
    errors = []
    valueNamesToRegs = {}
    regNameCounts = {}
    # These have duplicate fields, but we don't care.
    ignore=BasicInfoReg,
    for reg in jbd.eeprom_regs:
        if reg.__class__ in ignore: continue
        if reg.regName not in regNameCounts:
            regNameCounts[reg.regName] = 1
        else:
            regNameCounts[reg.regName] += 1

    for regName, count in regNameCounts.items():
        if count == 1: continue
        errors.append(f'register name {regName} occurs {count} times')

    for reg in jbd.eeprom_regs:
        if reg.__class__ in ignore: continue
        valueNames = reg.valueNames
        for n in valueNames:
            if n in valueNamesToRegs:
                otherReg = valueNamesToRegs[n]
                errors.append(f'duplicate value name "{n}" in regs {reg.regName} and {otherReg.regName}')
            else:
                valueNamesToRegs[n] = reg
    return errors

# sanity check for reg setup
errors = checkRegNames()
if errors:
    for error in errors:
        print(error)
    raise RuntimeError('register errors')
del errors
# j = JBD('COM3')
#print('dbghook')