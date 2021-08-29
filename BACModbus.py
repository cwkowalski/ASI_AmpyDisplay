import os
import platform
from xml.etree import ElementTree as et
from numpy import array
#from scipy import interpolate as interp
from interpolate import cubic_interp1d as interp
import csv
#import minimalmodbus
#import serial

# =======================================================
# ASI Object Dictionary filepath to build dictionary definitions
# =======================================================
filename = 'ASIObjectDictionary.xml'
filepath = os.path.abspath(os.path.dirname(__file__)) + '/' #Checks local directory
xml = et.parse(filepath + filename)
Obdic = xml.iterfind('Parameters/ParameterDescription')


# IO class
class BACModbus():
    def __init__(self, port):
        self.port = port
        self.address = 1
        self.method = 'rtu'
        self.baudrate = 115200
        self.bytesize = 8
        self.stopbits = 1
        self.timeout = 1
        self.parity = 'N'

        self.ObdicAddress = {}
        self.ObdicScale = {}
        self.ObdicUnit = {}
        self.ObdicEnum = {}  # "enumerated" bitwise parameters, returns bit key/name as string
        self.ObdicBit = {}  # "bit vector" bitwise parameters, returns bit key/name
        self.ObdicBits = {}
        self.RegsDic = {}

        self.socmap_volts, self.socmap_soc, self.socmap_ah, self.socmap_wh_volts, self.socmap_wh = \
            [],[],[],[],[]

        with open(filepath + 'socmap.csv', mode='r', encoding='utf-8-sig') as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:  # If using own socmap, identify columns appropriately.
                self.socmap_ah.append(float(row[0]))
                self.socmap_volts.append(float(row[1]))
                self.socmap_soc.append(float(row[2]))
                self.socmap_wh.append(float(row[0]))
        self.socmap_volts = array(self.socmap_volts)
        self.socmap_soc = array(self.socmap_soc)
        self.socmap_ah = array(self.socmap_ah)
        self.socmap_wh = array(self.socmap_wh)
        file.close()

        #self.socmap_wh = []
        #for n, val in enumerate(self.socmap_volts):
        #    pass
            #self.socmap_wh.append(self.socmap_volts[])
        self.socmap = interp(self.socmap_volts, self.socmap_soc)
        self.ahmap = interp(self.socmap_volts, self.socmap_ah)
        self.wh_a2v_map = interp(self.socmap_ah, self.socmap_volts)
        self.whmap = interp(self.socmap_volts, self.socmap_wh)

        for parent in Obdic:  # InternalAppEntity/Parameters/ParameterDescription children
            scale = parent.find('Scale').text
            if scale == ('enum'):
                key = parent.find('Key').text
                address = int(parent.find('Address').text)
                self.ObdicAddress.update({key: address})
                Enumerations = parent.findall('Enumerations/string')  # Text string
                # print('Parent: ', key)
                for EnumBit, EnumKey in enumerate(
                        Enumerations):  # returns loop number from 0 for first term EnumBit, while EnumKey = iteration of each Enumerations element
                    self.ObdicEnum.update(
                        {key: {EnumKey.text: EnumBit}})  # Ordered to return bit controlling key:string e.g.
                    # 'Speed_Regulator_Mode: Torque Mode with Speed Limiting'
                    # print('Parent: ', key, 'Enumbit: ', EnumBit, 'Enumstring: ', EnumKey.text) #et.tostring(EnumKey, encoding='unicode'))
                    # ***print('Address: ', address, 'EnumParent: ', key, 'bit: ', EnumBit, 'key: ',
                    # EnumKey.text)  # ObdicEnum[key][EnumKey.text] to return positional bit
            else:
                if scale == ('bit vector'):
                    key = parent.find('Key').text
                    address = int(parent.find('Address').text)
                    self.ObdicAddress.update({key: address})
                    Bits = parent.findall('BitArray/Bit/Key')  # Overwrites previous instances in loop
                    for Bit, BitKey in enumerate(Bits):
                        self.ObdicBits[Bit] = BitKey.text
                        # print('Key: ', key, 'Bit: ', Bit, 'String: ', BitKey.text) ### !DESIRED OUTPUT!
                    if key not in self.ObdicBit:
                        self.ObdicBit[key] = self.ObdicBits.copy()  # MUST COPY otherwise simply points to overwritten dict!


                else:
                    try:  # Convert scale strings to integers where possible, floats where not
                        scale = int(scale)
                    except ValueError:
                        try:
                            scale = float(scale)
                        except ValueError:
                            pass
                            # print('Float scale error: ', scale, 'Scale type: ', type(scale))
                    key = parent.find('Key').text
                    address = int(parent.find('Address').text)
                    try:
                        unit = parent.find('Units').text
                    except AttributeError:
                        unit = 'None'
                    self.ObdicAddress.update({key: address})
                    self.ObdicUnit.update({key: unit})
                    self.ObdicScale.update({address: scale})

    def bitflags(self, byte, address):  # Function to parse bit flags of byte from ObdicBit, returns fault strings
        # binary = "{0:b}".format(byte).zfill(16)
        binary = [(byte >> bit) & 1 for bit in range(16)]
        output = []
        for position, bit in enumerate(binary):
            # print('Pos:', position, 'Bit:', bit, 'ObidcBit:', ObdicBit[address][position], '\n')
            if bool(bit) == True:
                output.append(self.ObdicBit[address][position])
        return output
    def floop_parse(self, rawdata): # todo: delete, moved to BACSerialEmitter
        data = {'Faults': self.bitflags(0, 'Faults'), 'Powerboard_Temperature': rawdata[1],
                    'Vehicle_Speed': self.twocomp(rawdata[2], 16) / 256, 'Motor_Temperature': rawdata[3],
                    'Motor_Current': self.twocomp(rawdata[4], 16) / 32, 'Motor_RPM': self.twocomp(rawdata[5], 16),
                    'Percent_Of_Rated_RPM': rawdata[6] / 40.96, 'Battery_Voltage': rawdata[7] / 32,
                    'Battery_Current': self.twocomp(rawdata[8], 16) / 32}
        return data
    def parse(self, rawdata, address):
        # Parse register(s)-- return bitstrings or scaled values as appropriate in dict of [label name]:val OR [strings]
        data = []
        labels = []
        procdata = {}
        for count, value in enumerate(rawdata):
            address = int(self.ObdicAddress[address]) + count
            try:
                scaledvalue = value / self.ObdicScale[address]
            except KeyError:
                scaledvalue = self.bitflags(value, address)
            data.append(scaledvalue)
            labels.append(list(self.ObdicAddress.keys())[list(self.ObdicAddress.values()).index(address)])
        for index, label in enumerate(labels):
            procdata[label] = data[index]
        return procdata
    def twocomp(self, val_int, val_size):
        # Calculate the 2's complement
        # avoid overflow
        if not -1 << val_size - 1 <= val_int < 1 << val_size:
            err_msg = 'BACModbus: floop_parse: twocomp: could not compute two\'s complement for %i on %i bits'
            err_msg %= (val_int, val_size)
            raise ValueError(err_msg)
        # test negative int
        if val_int < 0:
            val_int += 1 << val_size
        # test MSB (do two's comp if set)
        elif val_int & (1 << (val_size - 1)):
            val_int -= 1 << val_size
        return val_int
    def socmapper(self, cell_v):
        return float(self.socmap.interp1d(cell_v))

    import numpy as np
    from math import sqrt