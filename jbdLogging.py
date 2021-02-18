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

from xlsxwriter import Workbook
import os
import time

class Logger:
    'currently written to be compatible with the JBD official app logging'
    @staticmethod
    def pvConvCompat(x):
        return f'{float(x) / 1000:.02f}V'

    @staticmethod
    def cvConvCompat(x):
        return f'{float(x) / 1000:.03f} V' # yes, space is intentional 
    
    @staticmethod
    def piConvCompat(x):
        return f'{float(x) / 1000:.02f}A'

    @staticmethod
    def pctConvCompat(x):
        return f'{int(x):d}%'

    @staticmethod
    def capConvCompat(x):
        return f'{int(x)}mAH'

    @staticmethod
    def tempConvCompat(x):
        return float(x)

    @staticmethod
    def boolConvCompat(x):
        return 'ON' if x else 'OFF'
    
    @staticmethod
    def faultConvCompat(x):
        return f'{int(x):x}'

    @staticmethod
    def balConvCompat(x):
        return f'{int(x):x}'

    headerNames1 = 'Date time PackVoltage current'.split()
    headerNames2 = ['Average Vol', 'MaxCell', 'MinCell', 
                    'RSOC', 'Remain cap', 'Full Charge Cap', # capitalization intentionally wrong
                    'Cycle Count'] 
    headerNames3 = ['CHG Fet Status', 'DSG Fet Status', 
                    'ProtectStatus', 'BalanceStatus']
    
    def __init__(self, fn):
        self.logFilename = fn
        print(f'logfile name: {fn}')
        if os.path.exists(fn):
            os.remove(fn)
        self.headerWritten = False
        self.rowNum = 0
        if fn.lower().endswith('.xls') or fn.lower().endswith('.xlsx'):
            self.logFileHandle = Workbook(fn, {'constant_memory': True})
        else:
            self.logFileHandle = open(fn, 'w+')
        self.fn = fn

    def _logRow(self, row):
        if not self.logFileHandle: return
        h = self.logFileHandle
        if isinstance(h, Workbook):
            worksheets = h.worksheets()
            if not worksheets:
                name = os.path.basename(os.path.splitext(self.fn)[0])
                ws = h.add_worksheet(name) 
            else:
                ws = worksheets[0]

            for col, data in enumerate(row):
                ws.write(self.rowNum, col, data)
        else:
            h.write(','.join([str(i) for i in row])+'\n')
            h.flush()

        self.rowNum += 1

    def _logCompat(self, basicInfo, cellInfo):
        cellInfo = list(cellInfo.values())
        cellCnt = len(cellInfo)
        ntcCnt = basicInfo['ntc_cnt']
        if not self.headerWritten:
            self.headerWritten = True
            h = (*self.headerNames1,
                 *[f'Cell{i+1}' for i in range(cellCnt)],
                 *self.headerNames2,
                 *[f'temp{i+1}' for i in range(ntcCnt)],
                 * self.headerNames3)
            self._logRow(h)
        row = (
            *self.dateGen(),
            self.pvConvCompat(basicInfo['pack_mv']),
            self.piConvCompat(basicInfo['pack_ma']),
            *[self.cvConvCompat(i) for i in cellInfo],
            self.cvConvCompat(sum(cellInfo) / cellCnt),
            self.cvConvCompat(max(cellInfo)),
            self.cvConvCompat(min(cellInfo)),
            self.pctConvCompat(basicInfo['cap_pct']),
            self.capConvCompat(basicInfo['cur_cap']),
            self.capConvCompat(basicInfo['full_cap']),
            basicInfo['cycle_cnt'],
            *[self.tempConvCompat(basicInfo[f'ntc{i}']) for i in range(ntcCnt)],
            self.boolConvCompat(basicInfo['chg_fet_en']),
            self.boolConvCompat(basicInfo['dsg_fet_en']),
            self.faultConvCompat(basicInfo['fault_raw']),
            self.balConvCompat(basicInfo['bal_raw']) 
        )
        self._logRow(row)

    def log(self, basicInfo, cellInfo):
        self._logCompat(basicInfo, cellInfo)

    @staticmethod
    def dateGen():
        t = time.localtime()
        return time.strftime('%Y-%m-%d', t), time.strftime('%H:%M:%S', t)

    def close(self):
        if not self.logFileHandle: return
        self.logFileHandle.close()
        self.logFileHandle = None
        print(self.fn, 'closed')

    def __del__(self):
        self.close()

class DbgLock(object):
    def __init__(self):
        self._lock = threading.Lock()

    def acquire(self, *args, **kwargs):
        print('acquire ...', end='')
        sys.stdout.flush()
        ret = self._lock.acquire(*args, **kwargs)
        print(f'{"LOCK" if ret else "FAIL"}')
        return ret

    def release(self, *args, **kwargs):
        print('release ... UNLOCK')
        return self._lock.release(*args, **kwargs)

    def __enter__(self):
        self.acquire()

    def __exit__(self, type, value, traceback):
        self.release()