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

class JBDPersist:
    fields =  {
        #'FileCode' __unknown__ 3838
        'DesignCapacity':       (('design_cap',), IntParserX10),
        'CycleCapacity':        (('cycle_cap',), IntParserX10),
        'FullChargeVol':        (('cap_100',), IntParserX1),
        'ChargeEndVol':         (('cap_0',), IntParserX1),
        'DischargingRate':      (('dsg_rate',), IntParserD10),
        'ManufactureDate':      (('year', 'month', 'day'), DateParser),
        'SerialNumber':         (('serial_num',), IntParserX1),
        'CycleCount':           (('cycle_cnt',), IntParserX1),
        'ChgOverTemp':          (('chgot',), TempParser),
        'ChgOTRelease':         (('chgot_rel',), TempParser),
        'ChgLowTemp':           (('chgut',), TempParser),
        'ChgUTRelease':         (('chgut_rel',), TempParser),
        'DisOverTemp':          (('dsgot',), TempParser),
        'DsgOTRelease':         (('dsgot_rel',), TempParser),
        'DisLowTemp':           (('dsgut' ,), TempParser),
        'DsgUTRelease':         (('dsgut_rel',), TempParser),
        'PackOverVoltage':      (('povp',), IntParserX10),
        'PackOVRelease':        (('povp_rel',), IntParserX10),
        'PackUnderVoltage':     (('puvp',), IntParserX10),
        'PackUVRelease':        (('puvp_rel',), IntParserX10),
        'CellOverVoltage':      (('covp',), IntParserX1),
        'CellOVRelease':        (('covp_rel',), IntParserX1),
        'CellUnderVoltage':     (('cuvp',), IntParserX1),
        'CellUVRelease':        (('cuvp_rel',), IntParserX1),
        'OverChargeCurrent':    (('chgoc',), IntParserX10),
        'OverDisCurrent':       (('dsgoc',), IntParserX10),
        'BalanceStartVoltage':  (('bal_start',), IntParserX1),
        'BalanceWindow':        (('bal_window',), IntParserX1),
        'SenseResistor':        (('shunt_res',), IntParserD10),
        'BatteryConfig':        (('switch', 'scrl', 'balance_en', 'chg_balance_en', 'led_en', 'led_num'), BitfieldParser), 
        'NtcConfig':            (tuple([f'ntc{i+1}' for i in range(8)]), BitfieldParser),
        'PackNum':              (('cell_cnt',), IntParserX1),
        'fet_ctrl_time_set':    (('fet_ctrl',), IntParserX1),
        'led_disp_time_set':    (('led_timer',), IntParserX1),
        'VoltageCap80':         (('cap_80',), IntParserX1),
        'VoltageCap60':         (('cap_60',), IntParserX1),
        'VoltageCap40':         (('cap_40',), IntParserX1),
        'VoltageCap20':         (('cap_20',), IntParserX1),
        'HardCellOverVoltage':  (('covp_high',), IntParserX1),
        'HardCellUnderVoltage': (('cuvp_high',), IntParserX1),
        'HardChgOverCurrent':   (('sc', 'sc_delay', 'sc_dsgoc_x2'), ScParser),
        'HardDsgOverCurrent':   (('dsgoc2', 'dsgoc2_delay'), Dsgoc2Parser),
        'HardTime':             (('covp_high_delay', 'cuvp_high_delay'), CxvpDelayParser),
        'SCReleaseTime':        (('sc_rel',), IntParserX1),
        'ChgUTDelay':           (('chgut_delay',), IntParserX1),
        'ChgOTDelay':           (('chgot_delay',), IntParserX1),
        'DsgUTDelay':           (('dsgut_delay',), IntParserX1),
        'DsgOTDelay':           (('dsgot_delay',), IntParserX1),
        'PackUVDelay':          (('puvp_delay',), IntParserX1),
        'PackOVDelay':          (('povp_delay',), IntParserX1),
        'CellUVDelay':          (('cuvp_delay',), IntParserX1),
        'CellOVDelay':          (('covp_delay',), IntParserX1),
        'ChgOCDelay':           (('chgoc_delay',), IntParserX1),
        'ChgOCRDelay':          (('chgoc_rel',), IntParserX1),
        'DsgOCDelay':           (('dsgoc_delay',), IntParserX1),
        'DsgOCRDelay':          (('dsgoc_rel',), IntParserX1),
        'ManufacturerName':     (('mfg_name',), StrParser),
        'DeviceName':           (('device_name',), StrParser),
        'BarCode':              (('barcode',), StrParser),
    }

    def __init__(self):
        pass

    def deserialize(self, data):
        opened = False
        ret = {}
        lines = [l.strip() for l in data.splitlines() if l.strip()] # non-empty lines
        kv = [l.split(maxsplit=1) for l in lines]               # split into key/value
        kv = [(i + [''])[:2] for i in kv]                       # ensure empty values are '' 
        for fieldName, data in kv:
            if fieldName not in self.fields:
                print(f'unknown field {fieldName}')
                continue
            valueNames, conv = self.fields[fieldName]
            values = conv.decode(data)
            values = values[:len(valueNames)] #sometimes decoders return too many values
            ret.update(dict(zip(valueNames, values)))
        return ret

    def serialize(self, data):
        allPassedValueNames = set(data.keys())
        # noidea what this is
        lines = ['  FileCode               3838']

        for fieldName, meta in self.fields.items():
            valueNames, parser = meta
            valueNameSet = set(valueNames)
            foundValueNames = valueNameSet & allPassedValueNames
            if foundValueNames != valueNameSet:
                raise ValueError(f'savefile field "{field}"" requires values {tuple(valueNames)}')
            values = [data[i] for i in valueNames]
            print(fieldName, valueNames, 'values:', ' '.join(repr(i) for i in values))
            if parser == StrParser:
                spacer = ' ' * (23 - len(fieldName))
            else:
                spacer = ' ' * 8
            lines.append(f'  {fieldName}{spacer}{str(parser.encode(values))}')
        return bytes(''.join([i + '\r\r\n' for i in lines]), 'utf-8')

