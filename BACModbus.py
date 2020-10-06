import os
from xml.etree import ElementTree as et
import minimalmodbus
import serial

# =======================================================
# ASI Object Dictionary filepath to build dictionary definitions
# =======================================================
filename = 'ASIObjectDictionary.xml'
filepath = os.path.abspath(os.path.join('', filename)) #Checks local directory
xml = et.parse(filepath)
Obdic = xml.iterfind('Parameters/ParameterDescription')

# ===============================================================
# Basic serial connection parameters for RS232/RTU MODBUS protocol
# ===============================================================

BACport = "COM4"
BACaddress = 1
BACmode = minimalmodbus.MODE_RTU
BACbaudrate = 115200
BACbytesize = 8
#BACparity = serial.PARITY_NONE
BACstopbits = 1
BACtimeout = 0.2

instr = minimalmodbus.Instrument(BACport, BACaddress)
instr.address = BACaddress
instr.mode = BACmode
instr.serial.baudrate = BACbaudrate
instr.serial.bytesize = BACbytesize
instr.serial.parity = serial.PARITY_NONE
instr.serial.stopbits = BACstopbits
instr.serial.timeout = BACtimeout

#Instantiate dictionaries
ObdicAddress = {}
ObdicScale = {}
ObdicUnit = {}
ObdicEnum = {}  # "enumerated" bitwise parameters, returns bit key/name as string
ObdicBit = {}  # "bit vector" bitwise parameters, returns bit key/name
ObdicBits = {}
RegsDic = {}  # Updated every fastloop 'floop' via BAC.reads()

# IO class
class BACModbus:
    def __init__(self):
        pass
    def read(self, addressKey):
        read = (instr.read_register(int(ObdicAddress[addressKey]), 0) / float(ObdicScale[ObdicAddress[addressKey]]))
        # print(BAC.open)
        print("Address: ", ObdicAddress[addressKey], "Value: ", read)
        return read

    def reads(self, addressKey, addressSpan): #Used only for fastloop reads (260-267) for serial bit efficiency
        RegsList = instr.read_registers(int(ObdicAddress[addressKey]), addressSpan)
        for count, value in enumerate(RegsList):
            address = int(ObdicAddress[addressKey]) + count
            # print(address, ObdicScale[address])
            try: scaledvalue = value/ObdicScale[address]
            except KeyError: # Scaling will fail for enumbit/bitvectors. For flooping over 'Faults' key:
                value = [(value >> bit) & 1 for bit in range(16)]
                bits = []
                for position, bit in enumerate(value):
                    if bool(bit) == True:
                        bits.append(ObdicBit[addressKey][position])
                scaledvalue = bits
            RegsDic.update({address: scaledvalue})
        return RegsDic

    def read_bitvectors(self, addressKey, ):
        # read = f'{instr.read_register(int(ObdicAddress[addressKey]), 0):016b}'
        read = instr.read_register(int(ObdicAddress[addressKey]), 0)
        read = [(read >> bit) & 1 for bit in range(16)]
        bits = []
        for position, bit in enumerate(read):
            if bool(bit) == True:
                # print(ObdicBit[addressKey][position])
                bits.append(ObdicBit[addressKey][position])
        return bits

    def write(self, addressKey, value):
        try:
            instr.write_register(ObdicAddress[addressKey], value)
        except IOError:
            print("Failed to write register of controller!")
        else:
            print('Address: ', ObdicAddress[addressKey], 'Key: ', addressKey, 'Write value: ', value)

    def writescaled(self, addressKey, value):
        try:
            instr.write_register(int(ObdicAddress[addressKey]), (ObdicScale[ObdicAddress[addressKey]] * value))
        except IOError:
            print("Failed to write write register of controller! (RegWriteScaled)")
        else:
            print('Address: ', ObdicAddress[addressKey], 'Key:', addressKey, 'Write value: ', value, 'Scale: ', ObdicScale[(ObdicAddress[addressKey])])

    def profile(self, profile):
        if profile == 1:
            self.writescaled('Maximum_Field_Weakening_Current', 50)
            self.writescaled('Rated_Motor_Current', 450)
            self.writescaled('Remote_Maximum_Battery_Current_Limit', 300)
        else:
            if profile == 2:
                self.writescaled('Maximum_Field_Weakening_Current', 0)
                self.writescaled('Rated_Motor_Current', 220)
                self.writescaled('Remote_Maximum_Battery_Current_Limit', 200)
            else:
                if profile == 3:
                    self.writescaled('Maximum_Field_Weakening_Current', 0)
                    self.writescaled('Rated_Motor_Current', 220)
                    self.writescaled('Remote_Maximum_Battery_Current_Limit', 15)

    def assist(self, assistLevel):
        # AssistScale.set(int(assistLevel))
        # print('AssistLevel: ', assistLevel)
        self.write('Remote_Assist_Mode', int(assistLevel))

# ======================================
# Build parameter dictionaries from ASIObjectDictionary.xml
# ======================================
for parent in Obdic:  # InternalAppEntity/Parameters/ParameterDescription children
    scale = parent.find('Scale').text
    if scale == ('enum'):
        key = parent.find('Key').text
        address = int(parent.find('Address').text)
        ObdicAddress.update({key: address})
        Enumerations = parent.findall('Enumerations/string')  #Text string
        # print('Parent: ', key)
        for EnumBit, EnumKey in enumerate(Enumerations):  #returns loop number from 0 for first term EnumBit, while EnumKey = iteration of each Enumerations element
            ObdicEnum.update({key: {EnumKey.text: EnumBit}})  # Ordered to return bit controlling key:string e.g.
            # 'Speed_Regulator_Mode: Torque Mode with Speed Limiting'
            # print('Parent: ', key, 'Enumbit: ', EnumBit, 'Enumstring: ', EnumKey.text) #et.tostring(EnumKey, encoding='unicode'))
            # ***print('Address: ', address, 'EnumParent: ', key, 'bit: ', EnumBit, 'key: ',
                 # EnumKey.text)  # ObdicEnum[key][EnumKey.text] to return positional bit
    else:
        if scale == ('bit vector'):
            key = parent.find('Key').text
            address = int(parent.find('Address').text)
            ObdicAddress.update({key: address})
            Bits = parent.findall('BitArray/Bit/Key')  # Overwrites previous instances in loop
            for Bit, BitKey in enumerate(Bits):
                ObdicBits[Bit] = BitKey.text
                # print('Key: ', key, 'Bit: ', Bit, 'String: ', BitKey.text) ### !DESIRED OUTPUT!
            if key not in ObdicBit:
                ObdicBit[key] = ObdicBits.copy() # MUST COPY otherwise simply points to overwritten dict!


        else:
            try: # Convert scale strings to integers where possible, floats where not
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
            ObdicAddress.update({key: address})
            ObdicUnit.update({key: unit})
            ObdicScale.update({address: scale}) # originally key: scale, changed to Address for RegsRead;
                                            # faster to avoid lookup of string for each address to lookup scale,
                                            # than to just iterate through addresses.
            # print('Address: ', address, 'ValueParent: ', key, 'Unit: ', unit, 'Scale: ', scale)

# Check ObdicBit dict
#for key in ObdicBit:
#    for bit in (ObdicBit[key]):
#        print('Bit: ', bit, 'Key: ', key, 'BitField: ', ObdicBit[key][bit])