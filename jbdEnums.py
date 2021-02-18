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

from enum import Enum
class Unit(Enum):
    MV   = ('millivolt', 'mV')
    V    = ('volt', 'V')
    C    = ('Celsius', '°C')
    S    = ('second', 's')
    K    = ('Kelvin', 'K')
    MA   = ('milliampere', 'mA')
    MAH  = ('milliampere hour', 'mAh')
    AH   = ('ampere hour', 'Ah')
    A    = ('ampere', 'A')
    PCT  = ('percent', '%')
    MO   = ('milliohms', 'mΩ')
    NONE = ('None', '')

    def __init__(self, long_name, symbol):
        self.long_name = long_name
        self.symbol = symbol

class LabelEnum(Enum):
    def __new__(cls, display, value):
        obj = object.__new__(cls)
        obj.val = value
        obj.display = display
        return obj

    def __str__(self):
        return str(self.display)

    @classmethod
    def byDisplay(cls, value):
        for v in cls:
            if value == v.display:
                return v
        return None

    @classmethod
    def byValue(cls, value):
        for v in cls:
            if value == v.val:
                return v
        return None

class Dsgoc2Enum(LabelEnum):
    _8MV  = (8,   0x0)
    _11MV = (11,  0x1)
    _14MV = (14 , 0x2)
    _17MV = (17 , 0x3)
    _19MV = (19 , 0x4)
    _22MV = (22 , 0x5)
    _25MV = (25 , 0x6)
    _28MV = (28 , 0x7)
    _31MV = (31 , 0x8)
    _33MV = (33 , 0x9)
    _36MV = (36 , 0xa)
    _39MV = (39 , 0xb)
    _42MV = (42 , 0xc)
    _44MV = (44 , 0xd)
    _47MV = (47 , 0xe)
    _50MV = (50 , 0xf)

class Dsgoc2DelayEnum(LabelEnum):
    _8MS    = (8,    0x0)
    _20MS   = (20,   0x1)
    _40MS   = (40,   0x2)
    _80MS   = (80,   0x3)
    _160MS  = (160,  0x4)
    _320MS  = (320,  0x5)
    _640MS  = (640,  0x6)
    _1280MS = (1280, 0x7)

class ScEnum(LabelEnum):
    _22MV  = (22,  0x0)
    _33MV  = (33,  0x1)
    _44MV  = (44,  0x2)
    _56MV  = (56,  0x3)
    _67MV  = (67,  0x4)
    _78MV  = (78,  0x5)
    _89MV  = (89,  0x6)
    _100MV = (100, 0x7)

class ScDelayEnum(LabelEnum):
    _70US  = (70,  0x0) 
    _100US = (100, 0x1) 
    _200US = (200, 0x2) 
    _400US = (400, 0x3) 

class CuvpHighDelayEnum(LabelEnum):
    _1S  = (1,  0x0)
    _4S  = (4,  0x1)
    _8S  = (8,  0x2)
    _16S = (16, 0x3)

class CovpHighDelayEnum(LabelEnum):
    _1S  = (1,  0x0)
    _2S  = (2,  0x1)
    _4S  = (4,  0x2)
    _8S  = (8,  0x3)
