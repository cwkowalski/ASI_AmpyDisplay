from PyQt5 import QtCore, QtWidgets, QtGui
from sys import exit
import os
import time
import csv
from multiprocessing import Process, Pipe, Queue
import datetime
import BACModbus
from setup import read_setup
from jbdMain import JBD
from ampy import Ui_MainWindow
#import serial
#import logging # logging
import modbus_tk_ampy.defines as cst
from modbus_tk_ampy import modbus_rtu
#from scipy import integrate
from integrate import simps
#from scipy.stats import linregress
from numpy import mean, isnan, array, prod, abs
#import pdb  # pdb.set_trace() to add breakpoint
import simple_pid as pid
#DisableForDesktopDebug
#from platform import system as platsys
#if platsys() == 'Linux': # Need better solution for crossplatform dev...
#import RPi.GPIO as GPIO
# import psutil # Process = psutil.Process(getpid()) # To get memory use
import sqlite3
#import argparse
from number_pad import numberPopup
from options_dialog import optionsDialog
from bms_dialog import bmsDialog
from bmscfg_dialog import bmscfgDialog
# todo: Misc dev.
#   A. try a fork with restricted imports/refactors and recheck strace to minimize depsize, include .pyc; e.g.
#       QtWidgets.QMainWindow .QApplication .QMessageBox, QSlider... etc
#       from scipy.integrate import simps vs. from scipy import integrate >> integrate.simps
#   B. Consider serial control of walk mode registers for 'zero RR' riding assist.
#       Three RR settings could be derived from trip simulator experimental RR;
#       "Coast" e.g. eliminate all RR at x mph, "Normal" to offset hysteresis torque only,
#       and "Emulate Cancer Farts" for ICE-like "engine-braking" AKA "plug-braking".
#  C.Verify 'Regeneration_battery_current_limit' parameter behavior. Currently controller reports
#       calculated battery current braking limit parameter = system voltage *  Rated motor power (Race mode PAS power)
#       is this the only difference between rated/remote power registers?
#  C1. Does assist level affect regeneration current?
#  C2. Does PAS power actually control regen current with Throttle bypass assist level = 1?
#  C3. Does Race mode PAS power actually scale regen current with Alternate speed/power limit disabled?
#  C4. 'Rated battery voltage' is supposed to be peak battery voltage...? I prefer average/shallow DoD...
#  C5. Also test the Overload_..._current/time values (Addr 99-104) after ferrofluid mod.
#  E. Backup EEPROM in SQL each write, include ComboBox to select priors?
#       Or, add a manual save/restore feature with existing JBD backend.
#  F. Simulate cruise control by switching to remote throttle, speed type, set current speed? Then back?

# Throttle bypass assist level: 6.015+ Features3 Bit0 enable, to ignore assist level and use 100% throttle input.
# Human Power Assist Standard: If enabled: https://support.accelerated-systems.com/KB/?p=2175
# Full Pedelec Assistance Speed: Point at which foldback on Max Pedelec Assistance Gain terminates.
# Pedelec gain = 0 when speed = Vehicle_Maximum_Speed (for assistance only, addr 1920)

# SOC rundown test, while polling;
# 12:25 AM
# 38.7% SOC (16.2567Ahrem)
# 9:46 AM
# 37.4% SOC (15.7276Ahrem
# 0.134974971 percent SOC per hour
# 0.056689306 AH/H
# 4.32681378 Watt-hours/H
# ~5.14285714 watts idle controller power not detected by shunt-- factor into mileage?

# Self. vars used only for labels should be updated as formatted string, instead of np_float64's.
# ~18750 elements for last 5 minutes of data

# Redirect stdout print to file for debug logs
# orig_stdout = sys.stdout
# f = open('out.txt', 'w')
# sys.stdout = f
# sys.stdout = orig_stdout
# f.close()

#############################
# 139mA draw controller + display at 76.719 volts. NO running lights.

class BACProcessEmitter(QtCore.QThread):
    bac_msg = QtCore.pyqtSignal(object)
    diag_msg = QtCore.pyqtSignal(object)
    hack_msg = QtCore.pyqtSignal(object)
    def __init__(self, from_bac_process: Pipe):
        super().__init__()
        self.data_from_bacprocess = from_bac_process

        self.bacmsg = None
        self.workercmd = 0
        self.setup = setup
        self.running = True

    def run(self):
        while True:
            try:
                self.bacmsg = self.data_from_bacprocess.recv()
                if type(self.bacmsg) is tuple:
                    self.bac_msg.emit(self.bacmsg)
                elif type(self.bacmsg) is dict:
                    self.diag_msg.emit(self.bacmsg)
                elif type(self.bacmsg) is list:
                    self.hack_msg.emit(self.bacmsg)
            except EOFError:
                pass


class BMSProcessEmitter(QtCore.QThread):
    bms_basic_msg = QtCore.pyqtSignal()
    bms_eeprom_msg = QtCore.pyqtSignal()
    bms_exception = QtCore.pyqtSignal(str)
    def __init__(self, from_bms_process: Pipe):
        super().__init__()
        # BMS Attributes
        self.data_from_bmsprocess = from_bms_process
        self.bmsmsg = None
        self.basicMsg = None
        self.eepromMsg = None
        # BAC Attributes
        # self.msg.connect(callback)
        self.workercmd = 0
        self.setup = setup

        self.newcmd = False
        self.running = True
        #self.client = modbus_rtu.RtuMaster(serial.Serial(port=BAC.port, baudrate=BAC.baudrate, bytesize=BAC.bytesize,
        #                                                 parity=BAC.parity, stopbits=BAC.stopbits))
        #self.client.set_timeout(1)

    def run(self):
        while True:
            # todo: Check for alternative to try: if you can find a way to use 'if', may improve performance here
            try:
                self.bmsmsg = self.data_from_bmsprocess.recv()
            except EOFError:
                break
            if self.bmsmsg[0] == 0:
                # todo: instead store locally for accessing by Parent. Use signal only to trigger check whether to...
                #  throw faults, or update bmspopup, etc
                self.basicMsg = self.bmsmsg[1:]
                self.bms_basic_msg.emit()
            elif self.bmsmsg[0] == 1:
                self.eepromMsg = self.bmsmsg[1:]
                self.bms_eeprom_msg.emit()
            else:
                print('BMSSerialEmitter message not recognized!')

class BMSSerialProcess(Process):
    def __init__(self, bmsport, to_emitter: Pipe, from_window: Queue):
        #super(BMSSerialProcess, self).__init__(target=self.pickle_wrapper)
        super(BMSSerialProcess, self).__init__()
        #print('BMSSerialProcV2 init begin.')
        self.daemon = True
        self.data_to_emitter = to_emitter
        self.data_from_window = from_window
        self.basicData = None
        self.cellData = None
        self.scanning = True

        self.t1 = time.time_ns() / 1000000000
        self.t2 = None

        self.jbdcmd = 0 # 0 = basic/cell loop, 1 = eeprom read, 2 = eeprom write
        self.bmsport = bmsport
        self.j = JBD(self.bmsport, timeout = 1, debug = False)

    def run(self):
        print('bmsProc runloop begin.')
        while self.scanning:
            try:
                if not self.data_from_window.empty():
                    self.jbdcmd = self.data_from_window.get()
                    print('bmsProc: cmd recvd: ', self.jbdcmd)
                self.bms_loop()
            except Exception as e:
                print('bmsProc: exception: ', e)

    def bms_loop(self):
        if self.jbdcmd == 0:
            #print('bmsProc.loop: ', self.jbdcmd)
            self.poller()
        elif self.jbdcmd == 1:
            #print('bmsProc.loop: ', self.jbdcmd)
            self.eeprom_read()
            self.jbdcmd = 0
        elif self.jbdcmd == 2:
            self.j.clearErrors()
            self.jbdcmd = 0
        elif len(self.jbdcmd[0]) > 1:
            #print('bmsProc::run:serloop; ', self.jbdcmd)
            self.eeprom_write(self.jbdcmd[0])
            self.jbdcmd = 0
    def poller(self):
        lastTime = self.t1
        self.t1 = time.time_ns() / 1000000000
        self.cellData = self.j.readCellInfo()
        #print('bmsProc: basicPoller: cellData: ', self.cellData)
        self.basicData = self.j.readBasicInfo()
        #print('bmsProc: basicPoller: basicData: ', self.basicData)
        self.t2 = time.time_ns() / 1000000000
        runtime = self.t2 - self.t1
        looptime = self.t1 - lastTime
        msg = (0, self.cellData, self.basicData, looptime, runtime)
        self.data_to_emitter.send(msg)
        #print('bmsProc: basicPoller finished')
        #print(self.cellData, '\n', self.basicData, '\n', looptime, runtime)
    def eeprom_read(self):
        if self.j.s.isOpen():
            self.j.close()
            msg = (1, self.j.readEeprom())
            self.data_to_emitter.send(msg)
        else:
            msg = (1, self.j.readEeprom())
            self.data_to_emitter.send(msg)
    def eeprom_write(self, update_eeprom):
        self.j.writeEeprom(update_eeprom)

class BACSerialProcess(Process):
    #bac_msg = QtCore.pyqtSignal(object)
    #hack_msg = QtCore.pyqtSignal(object)  # Notify main thread when successful
    # cmd = QtCore.pyqtSignal(object)
    def __init__(self, setup, to_emitter: Pipe, from_window: Queue, BAC):
        super(BACSerialProcess, self).__init__()
        # self.msg.connect(callback)
        self.data_to_emitter = to_emitter
        self.data_from_window = from_window
        self.BAC = BAC
        self.workercmd = 0
        self.lastworkercmd = None
        self.setup = setup

        self.bmsmsg = None
        self.battamps = 0
        self.fluxcommand = 0

        self.newcmd = False
        self.running = True
        self.time1 = time.time_ns() / 1000000000
        self.time2 = self.time1
        #self.client = modbus_rtu.RtuMaster(serial.Serial(port=BACport, baudrate=BACbaud, bytesize=BACbytesize,
        #                                                 parity=BACparity, stopbits=BACstopbits))
        #self.client.set_timeout(1)
        #self.serial = serial.Serial(port=BACport, baudrate=BACbaud, bytesize=BACbytesize,parity=BACparity, stopbits=BACstopbits)
        #self.client = modbus_rtu.RtuMaster(self.serial)

        # self.client.connect()
        # self.client.set_debug(True)
        # self.client.strict = False  # Use MODBUS interchar spacing as timeout... MODBUSIOException err
        # self.client.inter_char_timeout = 3.5 *

    def run(self):  # Executed via .start() method on instance, NOT .run()! Method name MUST be run.
        self.client = modbus_rtu.RtuMaster(self.BAC.port, self.BAC.baudrate, self.BAC.bytesize, self.BAC.parity, self.BAC.stopbits)
        self.client.set_timeout(1)
        while self.running:
            #self.time2 = time.time_ns() / 1000000000
            #print('bacProc: ', self.time2 - self.time1)
            #self.time1 = time.time_ns() / 1000000000
            if not self.data_from_window.empty():
                self.lastworkercmd = self.workercmd
                message = self.data_from_window.get()
                if len(message) == 1: # If only integer command, update command; elif data included, update command/data
                    self.workercmd = message[0]
                elif message[0] == -30:
                    self.workercmd = message[0]
                    self.battamps = message[1]
                elif message[0] == -31:
                    self.workercmd = message[0]
                    self.flux = message[1]
                elif message[0] == -32:
                    self.workercmd = message[0]
                    self.bmsmsg = (message[1], message[2])
                    #print('bmsmsg:', self.bmsmsg)
                elif message[0] == -34:
                    self.workercmd = message[0]
                    self.motamps = message[1]
            try: # Try to poll BAC. If problem with connection, reset and try again.
                self.run_command()
            except Exception as e:
                print('BACSerial exception: ', e)
                self.client.close()
                self.client.open()
                self.run_command()

            # print('worker: ', self.workercmd)
            # time.sleep(.2)
            # Tempting to convert each 'if' into a function, use dict to lookup function. However, this setup
            # prioritizes the main fast-loop slightly which is most important.

    def run_command(self):
        #if not self.newcmd or self.workercmd == 0:
        if self.workercmd == 0:
            # output = self.client.read_holding_registers(BAC.ObdicAddress['Faults'], count=9, unit=self.unit)
            self.data_to_emitter.send(self.reads('Faults', 9))
        elif self.workercmd > 0:  # Positive ints reserved for simple rangelimiter integration
            print('Rangelimiter received val: ', self.workercmd)
            self.write('Remote_Maximum_Battery_Current_Limit', self.workercmd)  # Enable to limit
            self.data_to_emitter.send(self.reads('Faults', 9))
            # Remain in this worker while rangelimiter enabled
        elif self.workercmd == -32:  # Update remote battery SOC/temperature for BAC foldbacks.
            self.writes('Remote_Battery_SOC', self.bmsmsg)
            self.workercmd = self.lastworkercmd # Because this is an automatic period command, do not disrupt ongoing processes.
        elif self.workercmd == -11:  # Set Profile 1
            # Possibly need to scale up Maximum braking torque/Maximum braking current parameters
            # which are a % of rated motor current, for consistent regen braking across profiles.
            # Currently both are 1229 / 40.96 = 30%!
            # 84 amps would be a conservative limit. 100 ok in bursts
            for i in self.setup['profile1']:
                self.write_scaled(i[0], i[1])
            self.workercmd = 0
            print('profile 1 called')
        elif self.workercmd == -12:  # Set Profile 2
            for i in self.setup['profile2']:
                self.write_scaled(i[0], i[1])
            self.workercmd = 0
            print('profile 2 called')
        elif self.workercmd == -13:  # Set Profile 3
            for i in self.setup['profile3']:
                self.write_scaled(i[0], i[1])
            self.workercmd = 0
            print('profile 3 called')
        elif self.workercmd < 0 and self.workercmd >= -10:  # -1 to -10 for Assist Levels 1-9
            self.write_scaled('Remote_Assist_Mode', -self.workercmd)  # -(-x) = positive x
            self.workercmd = 0
        elif self.workercmd == -14:  # Clear Fault codes
            self.client.execute(BAC.address, cst.WRITE_MULTIPLE_REGISTERS, 508, output_value=[1])
            self.workercmd = 0
        elif self.workercmd == -15:
            self.write('Remote_Maximum_Battery_Current_Limit', 0)  # Reset range power limiter-- ensure 0 = ignore.
            # Todo: Check if 0 = ignore, then keep track of profile state to choose limit.
            self.workercmd = 0
        elif self.workercmd == -16:  # Antitheft disable
            # intelligent bit-parsing for conditional switching;
            # modbit(n, p, b):  # mod byte at bit p in n to b
            #    mask = 1 << p
            #    return (n & ~mask) | ((b << p) & mask)
            bits = self.read('Features3')
            modbyte = (bits & ~(1 << 3)) | ((1 << 3)) & (1 << 3)
            print('Antitheft disable. bits: ', bits, 'modbyte: ', modbyte, '\n', 'bits: ', "{0:b}".format(bits),
                  'modbyte: ', "{0:b}".format(modbyte))
            self.write('Features3', modbyte)  # 8 = 4th binary bit
            self.workercmd = 0
        elif self.workercmd == -17:  # Antitheft enable
            bits = self.read('Features3')
            modbyte = (bits & ~(1 << 3)) | ((0 << 3)) & (1 << 3)
            print('Antitheft enable. Features3 bits: ', bits, 'modbyte: ', modbyte, '\n', 'bits: ',
                  "{0:b}".format(bits), 'modbyte: ', "{0:b}".format(modbyte))
            self.write('Features3', modbyte)
            self.workercmd = 0
        elif self.workercmd == -18:  # Reverse (cruise input) enable
            bits = self.read('Features3')
            modbyte = (bits & ~(1 << 4)) | ((0 << 4)) & (1 << 4)
            print('Reverse enable. Features3 bits: ', bits, 'modbyte: ', modbyte, '\n', 'bits: ', "{0:b}".format(bits),
                  'modbyte: ', "{0:b}".format(modbyte))
            self.write('Features3', modbyte)  # 16 = 5th binary bit
            self.workercmd = 0
        elif self.workercmd == -19:  # Reverse (cruise input) disable
            bits = self.read('Features3')
            modbyte = (bits & ~(0 << 4)) | ((1 << 4)) & (1 << 4)
            print('Reverse disable. Features3 bits: ', bits, 'modbyte: ', modbyte, '\n', 'bits: ', "{0:b}".format(bits),
                  'modbyte: ', "{0:b}".format(modbyte))
            self.write('Features3', modbyte)
            self.workercmd = 0
        elif self.workercmd == -20:
            bits = self.read('Features3')
            modbyte = (bits & ~(0 << 0)) | ((1 << 0)) & (1 << 0)
            print('Throttle bypass assist level enable. Features3 bits: ', bits, 'modbyte: ', modbyte, '\n', 'bits: ',
                  "{0:b}".format(bits),
                  'modbyte: ', "{0:b}".format(modbyte))
            self.write('Features3', modbyte)
            self.workercmd = 0
        elif self.workercmd == -21:
            bits = self.read('Features3')
            modbyte = (bits & ~(1 << 0)) | ((0 << 0)) & (1 << 0)
            print('Throttle bypass assist level disable. Features3 bits: ', bits, 'modbyte: ', modbyte, '\n', 'bits: ',
                  "{0:b}".format(bits),
                  'modbyte: ', "{0:b}".format(modbyte))
            self.write('Features3', modbyte)
            self.workercmd = 0
        elif self.workercmd == -22:
            bits = self.read('Features')
            modbyte = (bits & ~(0 << 11)) | ((1 << 11)) & (1 << 11)
            print('Walk mode enable. Features bits: ', bits, 'modbyte: ', modbyte, '\n', 'bits: ', "{0:b}".format(bits),
                  'modbyte: ', "{0:b}".format(modbyte))
            self.write('Features', modbyte)
            self.workercmd = 0
        elif self.workercmd == -23:
            bits = self.read('Features')
            modbyte = (bits & ~(1 << 11)) | ((0 << 11)) & (1 << 11)
            print('Walk mode disable. Features bits: ', bits, 'modbyte: ', modbyte, '\n', 'bits: ',
                  "{0:b}".format(bits), 'modbyte: ', "{0:b}".format(modbyte))
            self.write('Features', modbyte)
            self.workercmd = 0
        elif self.workercmd == -24:
            bits = self.read('Features')
            modbyte = (bits & ~(0 << 13)) | ((1 << 13)) & (1 << 13)
            print('Engine braking enable. Features bits: ', bits, 'modbyte: ', modbyte, '\n', 'bits: ',
                  "{0:b}".format(bits),
                  'modbyte: ', "{0:b}".format(modbyte))
            self.write('Features', modbyte)
            self.workercmd = 0
        elif self.workercmd == -25:
            bits = self.read('Features')
            modbyte = (bits & ~(1 << 13)) | ((0 << 13)) & (1 << 13)
            print('Engine braking disable. Features bits: ', bits, 'modbyte: ', modbyte, '\n', 'bits: ',
                  "{0:b}".format(bits), 'modbyte: ', "{0:b}".format(modbyte))
            self.write('Features', modbyte)
            self.workercmd = 0
        elif self.workercmd == -26:
            print('Motor Position Sensor Type set Hall')
            self.write('Motor_Position_Sensor_Type', 0)
            self.workercmd = 0
        elif self.workercmd == -27:
            print('Motor Position Sensor Type set Hall start & Sensorless')
            self.write('Motor_Position_Sensor_Type', 1)
            self.workercmd = 0
        elif self.workercmd == -28:
            print('Motor Position Sensor Type set Sensorless Only')
            self.write('Motor_Position_Sensor_Type', 2)
            self.workercmd = 0
        elif self.workercmd == -29:  # Diagnostics Mode-- Poller
            input_voltages = self.reads('Throttle_Voltage', 8)
            EbikeFlags = self.read('Ebike_Flags')
            SensorlessState = self.read('Sensorless_State')
            EbikeFlagsLabels = ['Brake', 'Cut out', 'Run Req', 'Pedal', 'Regen', 'Walk', 'Walk Start', 'Throttle',
                                'Reverse Mode', 'Interlock Off', 'Pedal Ramps', 'Gate Req', 'Gate Enabled',
                                'Boost Mode', 'Antitheft', 'Free Wheel']
            DigitalInputsLabels = ['Hall C', 'Hall B', 'Hall A', 'Pedal First Input', 'Cruise Input', 'Brake 1 Input',
                                   'Brake 2 Input', 'HWOC Pin', 'HWOC Latch', 'Remote Brake', 'Remote Pwr Rating Sw',
                                   'Remote Regen1', 'Remote Regen2', 'Remote Spd Rating Sw', 'Throttle Spd Rating Sw', 'N/A']
            WarningsLabels = ['Communication timeout', 'Hall sensor', 'Hall stall', 'Wheel speed sensor', 'CAN Bus',
                              'Hall sector', 'Hall transition', 'VdcLowFLDBK', 'VdcHighFLDBK', 'MotorTempFLDBK',
                              'ControllerTempFLDBK', 'LowSoCFLDBK', 'HiSoCFLDBK', 'I2tFLDBK', 'Reserved',
                              'LIN - BMS communication timeout']
            SensorlessStateEnum = ['Sensorless Idle', 'Sensorless DC-Ramp', 'Sensorless DC-Hold',
                                   'Sensorless FreqRamp', 'Sensorless CloseLoop', 'Sensorless Stall']
            DigitalInputsFlagged = []
            WarningsFlagged = []
            EbikeFlagsFlagged = []

            bitstring = "{0:b}".format(input_voltages[6])
            for i in range(len(bitstring)):
                if int(bitstring[i]):
                    DigitalInputsFlagged.append(DigitalInputsLabels[i])
            bitstring = "{0:b}".format(input_voltages[7])
            for i in range(len(bitstring)):
                if int(bitstring[i]):
                    WarningsFlagged.append(WarningsLabels[i])
            bitstring = "{0:b}".format(EbikeFlags)
            for i in range(len(bitstring)):
                if int(bitstring[i]):
                    EbikeFlagsFlagged.append(EbikeFlagsLabels[i])

            outmsg = {'Throttle_Voltage': input_voltages[0]/self.BAC.ObdicScale[self.BAC.ObdicAddress['Throttle_Voltage']],
                      'Brake_1_Voltage': input_voltages[1]/self.BAC.ObdicScale[self.BAC.ObdicAddress['Brake_1_Voltage']],
                      'Brake_2_Voltage': input_voltages[2] / self.BAC.ObdicScale[self.BAC.ObdicAddress['Brake_2_Voltage']],
                      'Analog_BMS_SOC_Voltage': input_voltages[5] / self.BAC.ObdicScale[self.BAC.ObdicAddress['Analog_BMS_SOC_Voltage']],
                      'EbikeFlags': EbikeFlagsFlagged, 'DigitalInputs': DigitalInputsFlagged, 'Warnings': WarningsFlagged,
                      'SensorlessState': SensorlessStateEnum[SensorlessState]}
            self.data_to_emitter.send(outmsg)

            # Digital Inputs 276
            # Throttle_Voltage 270
            # Brake_1_Voltage 271
            # Brake_2_Voltage 272
            # Analog_BMS_SOC_Voltage 275
            #
            # Warnings 277
            # Warnings2 359
            # Sensorless State 330
            # Motor_Temperature_Sensor_Voltage 398
            # Ebike Flags 327
            # 0 Brake
            # 1 Cutout
            # 2 Run Req
            # 3 Pedal
            # 4 Regen
            # 5 Walk
            # 6 Walk Start
            # 7 Throttle
            # 8 Reverse
            # 9 Interlock off
            # 10 Pedal ramp rate active
            # 11 Gate enable request
            # 12 Gate enabled
            # 13 Boost Enabled
            # 14 Antitheft enabled
            # 15 Free wheel
            # Ebike Flags2 488
            # 0 Regen always without analog input
            # 1 Cruise enable
        elif self.workercmd == -30:  # Adjust max battery power %
            self.write_scaled('Battery_Current_Limit', self.battamps)
            self.workercmd = 0
        elif self.workercmd == -31:
            self.write_scaled('Maximum_Field_Weakening_Current', self.fluxcommand)
            self.workercmd = 0
        elif self.workercmd == -33:  # Hack access level code.
            print('Beginning brute-force of BAC User Access Level codes.')
            # Keys = Spare_430, Spare_431, Spare_432
            # Check spare registers first:
            code1_spare = self.read('Spare_430')
            self.write('User_Access_Level', code1_spare)
            read = self.read('User_Access_Level')
            if read == 1:
                print('User access code cracked! Level ', read, ' code is #', code1_spare)
                self.data_to_emitter.send([read, code1_spare])
                self.code1 = read
            code2_spare = self.read('Spare_431')
            self.write('User_Access_Level', code2_spare)
            read = self.read('User_Access_Level')
            if read == 2:
                print('User access code cracked! Level ', read, ' code is #', code2_spare)
                self.data_to_emitter.send([read, code2_spare])
                self.code2 = read
            code3_spare = self.read('Spare_432')
            self.write('User_Access_Level', code3_spare)
            read = self.read('User_Access_Level')
            if read == 3:
                print('User access code cracked! Level ', read, ' code is #', code3_spare)
                self.data_to_emitter.send([read, code3_spare])
                self.code3 = read
            # If any of the above failed/deprecated, fallback to bruteforce, passes if code1 & code2 & code3 > 0
            val = 0
            running = True
            code1 = False
            code2 = False
            code3 = False
            while running:
                val += 1
                self.write('Parameter_Access_Code', val)
                read = self.read('User_Access_Level')
                if read == 1:
                    print('User access code cracked! Level ', read, ' code is #', val)
                    self.data_to_emitter.send([read, val])
                    self.code1 = read
                elif read == 2:
                    print('User access code cracked! Level 2 code is #', read)
                    self.data_to_emitter.send([read, val])
                    self.code2 = read
                elif read == 3:
                    print('User access code cracked! Level 3 code is #', read)
                    self.data_to_emitter.send([read, val])
                    self.code3 = read
                if code1 and code2 and code3:
                    running = False
                    print("Code1:", code1, "Code2:", code2, "Code3:", code3)
                    self.write('Parameter_Access_Code', code3)
                elif val > 100000:
                    running = False
        elif self.workercmd == -34:
            self.write_scaled('Rated_Motor_Current', self.motamps)
            self.workercmd = 0

    def read(self, address):
        output = self.client.execute(self.BAC.address, cst.READ_HOLDING_REGISTERS, self.BAC.ObdicAddress[address], 1)
        return output[0]

    def reads(self, address, length):
        return self.client.execute(self.BAC.address, cst.READ_HOLDING_REGISTERS, self.BAC.ObdicAddress[address], length)

    def read_scaled(self, address):
        val = (self.client.execute(self.BAC.address, cst.READ_HOLDING_REGISTERS, self.BAC.ObdicAddress[address], 1))
        scalar = self.BAC.ObdicScale[self.BAC.ObdicAddress[address]]
        output = tuple([x / scalar for x in val])
        return output[0]

    def reads_scaled(self, address, length):
        val = (self.client.execute(self.BAC.address, cst.READ_HOLDING_REGISTERS, self.BAC.ObdicAddress[address], length))
        scalar = self.BAC.ObdicScale[self.BAC.ObdicAddress[address]]
        output = tuple([x / scalar for x in val])
        return output

    def write(self, address, value):  # Helper function
        self.client.execute(self.BAC.address, cst.WRITE_MULTIPLE_REGISTERS, self.BAC.ObdicAddress[address], output_value=[value])

    def writes(self, address, value):  # Helper function
        self.client.execute(self.BAC.address, cst.WRITE_MULTIPLE_REGISTERS, self.BAC.ObdicAddress[address], output_value=value)

    def write_scaled(self, address, value):  # Helper function
        # todo: use returned values (register, 1 if written) to check for serial errors?
        write = int(value * self.BAC.ObdicScale[self.BAC.ObdicAddress[address]])
        self.client.execute(self.BAC.address, cst.WRITE_MULTIPLE_REGISTERS, self.BAC.ObdicAddress[address], output_value=[write])

class AmpyDisplay(QtWidgets.QMainWindow):
    #bacqueue = QtCore.pyqtSignal(int)
    powercmd = QtCore.pyqtSignal(int)
    fluxcmd = QtCore.pyqtSignal(float)
    hackaccesscmd = QtCore.pyqtSignal(int)
    bmsmsg_bac = QtCore.pyqtSignal(object)
    bmsbasiccmd = QtCore.pyqtSignal(object)
    bmseepromcmd = QtCore.pyqtSignal(object)
    def __init__(self, setup, bacqueue: Queue, bmsqueue: Queue, processManager: BMSProcessEmitter, *args, **kwargs, ):
        self.setup = setup
        self.battseries = setup['battery'][0]
        self.battparallel = setup['battery'][1]
        self.battah = setup['battery'][2]
        self.wheelcircum = setup['wheel']  # In mm
        self.speedparse = True
        self.first_floop = True
        self.lockpin = setup['pin']
        if setup['units'] == 'imperial':
            self.units = False
        elif setup['units'] == 'metric':
            self.units = True
        else:
            print('Setup.csv \"units\" parameter not recognized!')
        print('self.units:', self.units, setup['units'])
        #
        super().__init__(*args, **kwargs)
        # DISPLAY AND VEHICLE VARIABLES
        self.bmsqueue = bmsqueue
        self.bacqueue = bacqueue
        self.processEmitter = processManager
        self.processEmitter.daemon = True
        self.processEmitter.start()
        self.bmseeprom_initter = True
        self.bmstemps = (0, 0, 0, 0)
        self.bmscmd = 10 # 0 = Basic Poll, 1 = Read EEPROM, 2 = Write EEPROM, 10 = Poll then EEPROM init
        self.chargestate = False
        self.bmsCall() # Init EEPROM.

        self.message = {}
        self.profile = 0
        self.assist_level = 0
        self.opt_tripRangeValue = None  # Check Wh/mi every interval with floop/lastfloop for Range fxn only
        self.opt_throttleAssistBool = None
        self.opt_battaValue = None # todo: update in SQL setup
        self.opt_fluxValue = None

        self.tripReset(True) # To instantiate all floats, lists

        # For lifestats:
        self.lifestat_iter_ID = 0
        # Todo: update profilestate in sql init setup
        self.lifestat_ah_used, self.lifestat_ah_charged, self.lifestat_ahregen, self.lifestat_wh, self.lifestat_whregen, \
        self.lifestat_dist, self.lifestat_Rbatt = \
            float(0), float(0), float(0), float(0), float(0), float(0), float(0)

        # Range limiter PID:
        self.pid_kp = 0.09375
        self.pid_ki = 0.032
        self.pid_kd = 0.008
        self.pid = pid.PID(self.pid_kp, self.pid_ki, self.pid_kd, setpoint=self.flt_range_limit,
                           sample_time=0.016, output_limits=(0, 1))
        self.pid.auto_mode = False  # Don't run PID calculation until enabled. Possibly could replace trip_range_enabled
        # Kp = 1.2 * (width of process 'bump') / (amplitude * dead time)
        ## Kp = 1.2 * 0.1 / (80*0.016
        # Kt = 2*dead time
        ## Kt = 0.032
        # Kd = 0.5*dead time

        #RPi GPIO Brightness for Makerplane 5" display (pin18) conditional for PC development
        #if platsys() == 'Linux':
        #Makerplane Brightness Output
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(18, GPIO.OUT)
        self.pwm = GPIO.PWM(18, 100)
        self.pwm.start(0)
        # Profile Selector Switch
        GPIO.setup([22, 23], GPIO.IN, GPIO.PUD_DOWN)
        GPIO.add_event_detect(22, GPIO.BOTH)
        GPIO.add_event_detect(23, GPIO.BOTH)

        # Iterators and thresholds for averaging, interpolation, etc
        self.mean_length = 18750  # Average for trip_ floats over last 5 minutes (300s / 16ms)
        # trip_wh, trip_ah, trip_soc, trip_range based on cumulative integrals instead
        self.exceptions = 0
        self.iter = 0
        self.iter_threshold = 3  # Must be odd number for accurate/low-resource Simpsons integration
        self.iter_sql = 0
        self.iter_sql_threshold = 20 # ~3 hz
        self.iter_bmsmsg_threshold = 11
        self.iter_bmsmsg = 0
        self.iter_attribute_slicer = 0
        self.iter_attribute_slicer_threshold = self.mean_length + 500  # 500 = 8 seconds; re-slice for new means each 8 sec.
        self.iter_interp_threshold = 3750  # Equivalent time vs. mean_length
        self.trip_selector = 1
        self.displayinvert_bool = False
        #self.trip_selected = True
        self.gui_dict = {}
        # Set up the GUI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint))
        self.statusBar().setVisible(False)
        #if platsys() == 'Linux':
        QtWidgets.QApplication.setOverrideCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        #QtWidgets.QApplication.setOverrideCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        # Initialize stored profile/assist states;
        # First Setup SQL and populate lifestats, send optional controls to ASI
        self.sql_conn = sqlite3.connect(os.path.abspath(os.path.dirname(__file__)) + '/' + 'ampy.db')
        self.sql = self.sql_conn.cursor()
        self.SQL_init()  # Updates ID's to latest in table, creates tables if not exists.
        # Init optional controls;
        try:
            if self.profile == -11:
                self.ui.ProfileRb1.setChecked(True)
            elif self.profile == -12:
                self.ui.ProfileRb2.setChecked(True)
            elif self.profile == -13:
                self.ui.ProfileRb3.setChecked(True)
            self.ui.AssistSlider.setValue(int(abs(self.assist_level)-1))
            #self.ui.AssistSliderLabel.setText(str('Assist: ', int(abs(self.assist_level)-1)))
            self.ui.AssistSliderLabel.setText('Assist: ' + str(abs(self.assist_level)))
            self.bacqueue.put([self.profile])  # Assist emitted later
            self.bacqueue.put([self.assist_level])
            # todo: add below to sql init table. Or, setup SQL setup to write 0 = False val = true value, then check all
            self.signalThrottleBypassAssist(self.opt_throttleAssistBool)
            #self.signalBatta(True, self.opt_battaValue)
            #self.signalFlux(True, self.opt_fluxValue)
        except Exception as e:
            print('init: ', e)
        # Connect buttons
        self.ui.OptionsBtn.clicked.connect(self.popupOptions)
        #self.ui.BMSButton.clicked.connect(self.popupBms) # Moved to bmsBasicUpdate to prevent error on early access
        self.ui.BatterySOCReset.clicked.connect(self.socreset)
        self.ui.Reverse.toggled.connect(lambda: self.signalReverse(self.ui.Reverse.isChecked()))
        #self.ui.Reverse.setStyleSheet()
        #try:
        #    self.ui.PID_Kp_Slider.valueChanged.connect(lambda: self.pid_tuner_update(self.ui.PID_Kp_Slider.value(),
        #                                                                         self.ui.PID_Ki_Slider.value(),
        #                                                                         self.ui.PID_Kd_Slider.value()))
        #    self.ui.PID_Ki_Slider.valueChanged.connect(lambda: self.pid_tuner_update(self.ui.PID_Kp_Slider.value(),
        #                                                                         self.ui.PID_Ki_Slider.value(),
        #                                                                         self.ui.PID_Kd_Slider.value()))
        #    self.ui.PID_Kd_Slider.valueChanged.connect(lambda: self.pid_tuner_update(self.ui.PID_Kp_Slider.value(),
        #                                                                         self.ui.PID_Ki_Slider.value(),
        #                                                                         self.ui.PID_Kd_Slider.value()))
        #except AttributeError:
        #    pass
        self.ui.LockButton.clicked.connect(lambda: self.signalAntitheft(True))
        #self.ui.RangeBtn.toggled.connect(lambda: self.trip_range_enable(
        #    self.ui.RangeBtn.isChecked(), self.ui.RangeSlider.value()))
        #self.ui.RangeSlider.valueChanged.connect(lambda: self.trip_range_enable(
        #    self.trip_range_enabled, self.ui.RangeSlider.value()))
        self.ui.AssistSlider.valueChanged.connect(self.signalAssistLevel)
        self.ui.AssistSlider.setMaximum(9)
        # self.ui.AssistSlider.setTickInterval(1)
        # self.ui.AssistSlider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.ui.ProfileRb1.toggled.connect(lambda: self.signalProfile(self.ui.ProfileRb1.isChecked(), -11))
        ################# Convert profile1 to integers? floop = 0? Faultreset = 10, assist = 11?
        self.ui.ProfileRb2.toggled.connect(lambda: self.signalProfile(self.ui.ProfileRb2.isChecked(), -12))
        self.ui.ProfileRb3.toggled.connect(lambda: self.signalProfile(self.ui.ProfileRb3.isChecked(), -13))
        self.ui.Trip_Selector_1.toggled.connect(lambda: self.tripselect(self.ui.Trip_Selector_1.isChecked(), 1))
        self.ui.Trip_Selector_2.toggled.connect(lambda: self.tripselect(self.ui.Trip_Selector_2.isChecked(), 2))
        self.ui.Trip_Selector_3.toggled.connect(lambda: self.tripselect(self.ui.Trip_Selector_3.isChecked(), 3))
        # self.ui.Trip_Selector_Debug.toggled.connect(lambda: self.debug(self.ui.Trip_Selector_Debug.isChecked(), 'debug'))
        # Define display widgets
        # self.ui.TripDistance.setText('\xB0'+'C')  # DegreeC. 2-byte unicode + escape\ to get special char.
        self.ui.CheckEngineButton.clicked.connect(self.popupFault)
        self.ui.CheckEngineButton.hide()

        #self.ui.SpeedGauge_Static.set_MaxValue(80)
        #self.ui.SpeedGauge_Static.set_scala_main_count(8)
        #self.ui.SpeedGauge_Static.set_gauge_color_inner_radius_factor(980)
        #self.ui.SpeedGauge_Static.set_enable_Needle_Polygon(False)
        #self.ui.SpeedGauge_Static.set_enable_CenterPoint(False)
        #self.ui.SpeedGauge_Static.set_enable_value_text(False)
        #self.ui.SpeedGauge_Static.set_total_scale_angle_size(240)
        #self.ui.SpeedGauge_Static.set_start_scale_angle(150)
        #self.ui.SpeedGauge_Static.initial_scale_fontsize = 30
        #self.ui.SpeedGauge_Static.text_radius_factor = 0.75
        #self.ui.SpeedGauge.set_enable_fine_scaled_marker(False)
        #self.ui.SpeedGauge.set_enable_big_scaled_grid(False)
        if self.units:
            self.ui.SpeedGaugeLabelUnits.setText('kmh')
        else:
            self.ui.SpeedGaugeLabelUnits.setText('mph')
        self.ui.SpeedGauge.set_enable_value_text(False)
        self.ui.SpeedGauge.set_gauge_color_inner_radius_factor(950)
        self.ui.SpeedGauge.set_scale_polygon_colors([[0.00, QtCore.Qt.red], [0.25, QtCore.Qt.yellow], [1,
                                                     QtCore.Qt.green]])
        self.ui.SpeedGauge.set_enable_filled_Polygon(True)
        #self.ui.SpeedGauge.enable
        self.ui.SpeedGauge.set_enable_barGraph(False)
        #self.ui.SpeedGauge.set_enable_ScaleText(False)
        self.ui.SpeedGauge.set_MaxValue(80)
        self.ui.SpeedGauge.set_total_scale_angle_size(240)
        self.ui.SpeedGauge.set_start_scale_angle(150)
        self.ui.SpeedGauge.set_scala_main_count(8)
        self.ui.SpeedGauge.initial_scale_fontsize = 30
        self.ui.PowerGauge.set_scale_polygon_colors([[0.00, QtCore.Qt.red], [0.15, QtCore.Qt.yellow], [1,
                                                     QtCore.Qt.green]])
        self.ui.PowerGauge.set_enable_value_text(False)
        self.ui.PowerGauge.set_gauge_color_inner_radius_factor(950)
        self.ui.PowerGauge.set_enable_filled_Polygon(False)
        self.ui.PowerGauge.set_enable_barGraph(True)
        self.ui.PowerGauge.set_MaxValue(24)
        self.ui.PowerGauge.set_total_scale_angle_size(240)
        self.ui.PowerGauge.set_start_scale_angle(150)
        self.ui.PowerGauge.set_scala_main_count(8)
        self.ui.PowerGauge.scala_subdiv_count = 3
        self.ui.PowerGauge.initial_scale_fontsize = 30

        # todo: check which one of these is adjusting stretch properly
        #for i in range(6):
        #    self.ui.TripBoxGrid.setColumnMinimumWidth(i, 200)
        self.ui.Trip_1_1.sizePolicy().setHorizontalStretch(1)
        self.ui.Trip_1_2.sizePolicy().setHorizontalStretch(1)
        self.ui.Trip_1_3.sizePolicy().setHorizontalStretch(1)
        self.ui.Trip_1_1_prefix.sizePolicy().setHorizontalStretch(1)
        self.ui.Trip_1_2_prefix.sizePolicy().setHorizontalStretch(1)
        self.ui.Trip_1_3_prefix.sizePolicy().setHorizontalStretch(1)

        # Update floop with SQL-initiated tripstat lists for first run.
        try:
            self.floop = {'Faults': [], 'Powerboard_Temperature': 0, 'Vehicle_Speed': self.list_speed[-1:],
                      'Motor_Temperature': self.list_motor_temp[-1:], 'Motor_Current': self.list_motor_amps[-1],
                      'Motor_RPM': self.list_motor_rpm[-1], 'Percent_Of_Rated_RPM': 0.0,
                      'Battery_Voltage': self.list_batt_volts[-1], 'Battery_Current': self.list_batt_amps[-1]}
        except (IndexError, ValueError):
            self.floop = {'Faults': [], 'Powerboard_Temperature': 0, 'Vehicle_Speed': 0, 'Motor_Temperature': 0,
                          'Motor_Current': 0, 'Motor_RPM': 0, 'Percent_Of_Rated_RPM': 0,
                          'Battery_Voltage': 0, 'Battery_Current': 0}
        # Run
        self.time1 = self.ms()
        self.time2 = self.ms()
        # self.timeinterval = 0.016 #
        self.displayinverter(self.displayinvert_bool) # Restore last display inversion state.
        self.show()

    @QtCore.pyqtSlot(object)
    #### Fast Loop (FLOOP) Processing ####
    def floopReceive(self, message):  # You can update the UI from here.
        self.gettime()  # Calculate msg interval, increment iterators
        # todo: gettime should be called in the BACProc or maybe emitter, to ensure accuracy in multiproc version
        if self.speedparse:
            self.floop = BAC.floop_parse(message)
        else:
            self.floop = BAC.parse(message, 'Faults')
        # attributes for this class from BAC.BACModbus, e.g. the scales/keynames, and bring bitflags function into
        # this class also. TWO THIRDS of recieve_floop time is spent on this one line!!!
        self.floopToLists()
        self.SQL_tripstat_upload()
        if self.opt_tripRangeValue:
            self.tripRangeLimiter()
        if self.iter_attribute_slicer >= self.iter_attribute_slicer_threshold:  # Every 6 minutes, cut lists to last 5 minutes.
            self.floopSlicer()
            self.iter_attribute_slicer = 0
        if self.iter >= self.iter_threshold:  # Ideally an odd number to pass even number of *intervals* to Simpsons quadratic integrator
            if self.first_floop:  # Needed so socreset(), SQL has data for first init
                # Also will compensate for any self-discharge, charge since last start.
                #todo: find a way around unitasker bool in such a frequently used loop
                self.first_floop = False
                self.floopProcessBasic()  # of last -self.iter in lists from floop_to_list()
                self.socreset()
                # self.SQL_lifestat_upload() # todo: update fxn for new table, if not bmsinitted, upload...
            else:
                self.floopProcessBasic()
                #if self.setup['gpioprofile']: # If gpioprofiles in setup.csv, set profile with SPTT switch
                #    self.checkGPIO()
                self.guiPrepare()
                self.guiUpdate()
                self.iter = 0
        if self.iter_sql >= self.iter_sql_threshold: # 3hz
            self.sql_conn.commit()  # Previously in sql_tripstat_upload but moved here for massive speedup
            self.iter_sql = 0
        if self.iter_bmsmsg >= self.iter_bmsmsg_threshold: #0.5hz
            self.SQL_update_setup()
            self.SQL_lifestat_upload_bms()
            self.floopProcessLong()
            self.iter_bmsmsg = 0
        ##################
        # Message indices:
        # [0] = 258 = Faults
        # [1] = 259 = Powerboard_Temperature
        # [2] = 260 = Vehicle_Speed
        # [3] = 261 = Motor_Temperature
        # [4] = 262 = Motor_Current
        # [5] = 263 = Motor_RPM
        # [6] = 264 = Percent_Of_Rated_RPM
        # [7] = 265 = Battery_Voltage
        # [8] = 266 = Battery_Current
    def floopToLists(self):  # save each floop to instance attribute lists for trip stats
        if self.units: # todo: use RPM/wheelcircum instead. Consider reducing unused floop_parse for cpu.
            self.list_speed.append(self.floop['Vehicle_Speed']) # 0.621371192 is Km -> Mph conversion
        else:
            self.list_speed.append(self.floop['Vehicle_Speed'] * 0.621371192)
        self.list_motor_temp.append(self.floop['Motor_Temperature'])
        self.list_motor_amps.append(self.floop['Motor_Current'])
        self.list_batt_volts.append(self.floop['Battery_Voltage'])
        self.list_batt_amps.append(self.floop['Battery_Current'])
        self.list_motor_rpm.append(self.floop['Motor_RPM'])
    def floopSlicer(self): # Occassionally trim lists (averages only need last x minutes)
        self.list_speed = self.list_speed[-self.mean_length:]
        self.list_motor_temp = self.list_motor_temp[-self.mean_length:]
        self.list_motor_amps = self.list_motor_amps[-self.mean_length:]
        self.list_batt_volts = self.list_batt_volts[-self.mean_length:]
        self.list_batt_amps = self.list_batt_amps[-self.mean_length:]
        self.list_motor_rpm = self.list_motor_rpm[-self.mean_length:]
        self.list_whmi = self.list_whmi[-self.iter_interp_threshold:]  # From integral; self.mean_length/self.iter threshold = 986.842
        self.list_floop_interval = self.list_floop_interval[-self.mean_length:]
    def floopProcessBasic(self):
        x_interval = array([sum(([(self.list_floop_interval[-self.iter:])[:i] for i in range(1, self.iter + 1, 1)])
                                [i]) for i in range(self.iter)])  # calc cumulative time from list of intervals
        try:
            y_revsec = array(
            [(self.list_motor_rpm[-self.iter:])[i] / 60 for i in range(self.iter)])  # revolutions per second to match x, detect reverse RPM (65530) clipping
        except IndexError:
            y_revsec = array([0 for i in range(len(x_interval))])
        # Integrate distance fromm speed and increment distance counter
        revolutions = simps(y_revsec, x=x_interval, even='avg')
        if isnan(revolutions):
            distance = 0
        else:
            distance = (revolutions * self.wheelcircum) / (1609344)  ## miles
        self.flt_dist += distance

        array_volts, array_amps = array(self.list_batt_volts[-self.iter:]), array(self.list_batt_amps[-self.iter:])
        y_power = [prod(array_volts[i] * array_amps[i]) for i in range(self.iter)]
        y_current = array(self.list_batt_amps[-self.iter:])

        # Integrate watt-seconds from speed and increment watt-hour counter
        wattsec = simps(y_power, x=x_interval, even='avg')
        if wattsec >= 0:
            self.flt_wh += wattsec / 3600  # /(60x60) = Watt-hour
        elif wattsec < 0:
            self.flt_wh += wattsec / 3600
            self.flt_whregen += abs(wattsec) / 3600
        # Integrate amp-seconds from speed and increment amp-hour counter
        ampsec = simps(y_current, x=x_interval, even='avg')
        if ampsec >= 0:
            self.flt_ah += ampsec / 3600
        elif ampsec < 0:
            self.flt_ah += ampsec / 3600
            self.flt_ahregen += abs(wattsec) / 3600
        self.flt_soc = ((self.battah - self.flt_ah) / self.battah) * 100  # Percent SOC from Ah (charge)
        self.list_whmi.append(self.divzero(self.flt_wh, self.flt_dist))
        self.flt_whmi_inst = mean(self.list_whmi[-3:])
        self.flt_range = self.divzero(self.flt_wh, self.flt_whmi_inst)  # Wh for range to account for eff.
        self.flt_batt_volts_drop = self.flt_batt_volts_min - self.flt_batt_volts_max
        #try:
        #    print(self.iter, 'list_whmi: ', self.list_whmi[-self.iter], 'flt_wh: ', self.flt_wh, 'flt_dist: ', self.flt_dist,
        #          'revolutions: ', revolutions, 'y_revsec: ', y_revsec, 'distance: ', distance, 'y_power: ', y_power, 'wattsec: ', wattsec,)
        #except IndexError:
        #    pass
    def floopProcessLong(self):
        self.flt_whmi_avg = mean(self.list_whmi[-self.iter_interp_threshold:])  # 18750 / 19 self.iter =
        self.flt_batt_volts = mean(self.list_batt_volts)
        self.flt_batt_volts_max = max(self.list_batt_volts)
        self.flt_batt_volts_min = min(self.list_batt_volts)
        self.flt_batt_amps_max = max(self.list_batt_amps)
        self.flt_motor_amps = mean(self.list_motor_amps[-self.mean_length:])
        self.flt_motor_temp_max = max(self.list_motor_temp)
    def guiPrepare(self):  # Prepare gui elements to avoid EOL errors during gui update
        self.gui_dict['Time'] = time.strftime('%I:%M:%S', time.localtime())
        self.gui_dict['MotorTemperatureLabel'] = '{:.0f}'.format(self.floop['Motor_Temperature']) + '\xB0' + 'C'  # 'T<sub>M</sub>:' +
        self.gui_dict['MotorTemperatureBar'] = int(self.floop['Motor_Temperature'])
        self.gui_dict['BatteryVoltageLabel'] = '{:.1f}'.format(self.floop['Battery_Voltage']) + '<sub>V</sub>'
        self.gui_dict['BatteryVoltageDropLabel'] = '{:.1f}'.format(self.flt_batt_volts_drop)
        self.gui_dict['BatteryVoltageBar'] = int(self.floop['Battery_Voltage'])
        self.gui_dict['BatterySOCLabel'] = 'SOC: ' + '{:.1f}'.format(self.flt_soc)
        self.gui_dict['BatterySOCBar'] = int(self.flt_soc)
        self.gui_dict['SpeedGaugeLabel'] = '{:.0f}'.format(self.list_speed[-1]) # todo: use RPM
        self.gui_dict['SpeedGauge'] = self.list_speed[-1]
        power = (self.floop['Battery_Current'] * self.floop['Battery_Voltage']) / 1000
        self.gui_dict['PowerGaugeLabel'] = '{:.2f}'.format(power)
        self.gui_dict['PowerGauge'] = power
        if self.units:
            self.gui_dict['WhmiLabel'] = '{:.1f}'.format(self.flt_whmi_inst) + '<sub>Wh/km</sub>'
        else:
            self.gui_dict['WhmiLabel'] = '{:.1f}'.format(self.flt_whmi_inst) + '<sub>Wh/mi</sub>'

        if self.trip_selector == 1: # populate for first schema:
            self.gui_dict['Trip_1_1'] = '{:.2f}'.format(self.flt_wh)
            self.gui_dict['Trip_1_2'] = '{:.2f}'.format(self.flt_whmi_avg)
            self.gui_dict['Trip_1_3'] = '{:.1f}'.format(self.flt_ah)
            self.gui_dict['Trip_2_1'] = '{:.0f}'.format(self.get_battwh())
            #self.gui_dict['Trip_2_2'] = '{:.1f}'.format(self.flt_whmi_inst)
            self.gui_dict['Trip_2_2'] = '{:.2f}'.format(self.flt_whmi_avg / self.get_battwh())
            self.gui_dict['Trip_2_3'] = '{:.1f}'.format(self.battah - self.flt_ah)
            self.gui_dict['Trip_3_1'] = '{:.0f}'.format(self.flt_whregen)
            self.gui_dict['Trip_3_2'] = '{:.2f}'.format(self.flt_dist)
            self.gui_dict['Trip_3_3'] = '{:.1f}'.format(self.flt_ahregen)
        if self.trip_selector == 2:
            # Get indexes where speed > 0
            moving_indexes = [i for i in range(self.iter_attribute_slicer) if self.list_speed[i] > 0]
            moving_speed_list = [self.list_speed[i] for i in moving_indexes]
            # Fill dict
            self.gui_dict['Trip_1_1'] = '{:.1f}'.format(self.flt_whmi_avg / self.get_battwh())
            self.gui_dict['Trip_1_2'] = self.strfdelta(datetime.timedelta(seconds = (self.time2 - self.start_time)), '{hours}:{minutes}')
            self.gui_dict['Trip_1_3'] = '{:.0f}'.format(max(self.list_batt_amps))
            self.gui_dict['Trip_2_1'] = '{:.1f}'.format(self.flt_whmi_inst / self.get_battwh())
            # Get indexes where speed > 0, then sum flooptime for those indexes, convert to timedelta, then format
            self.gui_dict['Trip_2_3'] = '{:.1f}'.format(self.flt_batt_volts_min)
            self.gui_dict['Trip_3_1'] = '{:.0f}'.format(self.flt_motor_temp_max)  # Intensive if long
            if len(moving_indexes) > 0:
                self.gui_dict['Trip_2_2'] = self.strfdelta(datetime.timedelta(seconds = sum([self.list_floop_interval[i]
                                            for i in moving_indexes])), '{hours}:{minutes}')
                self.gui_dict['Trip_3_2'] = '{:.0f}'.format(mean(moving_speed_list))
                self.gui_dict['Trip_3_3'] = '{:.0f}'.format(max(moving_speed_list))
            else:
                self.gui_dict['Trip_2_2'], self.gui_dict['Trip_3_2'], self.gui_dict['Trip_3_3'] = str(0), str(0), str(0)
        if self.trip_selector == 3:
            # Setup gui_dict
            self.gui_dict['Trip_1_1'] = '{:.0f}'.format(self.processEmitter.basicMsg[1]['ntc0'])
            self.gui_dict['Trip_1_2'] = '{:.0f}'.format(self.processEmitter.basicMsg[1]['ntc1'])
            self.gui_dict['Trip_1_3'] = '{:.0f}'.format(self.flt_bmsmaxtemp)
            self.gui_dict['Trip_2_1'] = '{:.0f}'.format(self.processEmitter.basicMsg[1]['ntc2'])
            self.gui_dict['Trip_2_2'] = '{:.0f}'.format(self.processEmitter.basicMsg[1]['ntc3'])
            self.gui_dict['Trip_2_3'] = '{:.2f}'.format(self.processEmitter.basicMsg[1]['pack_ma'] / 1000)
            self.gui_dict['Trip_3_1'] = '{:.3f}'.format(self.flt_bmscellvrng)
            self.gui_dict['Trip_3_2'] = '{:.2f}'.format(self.flt_bmscellvmean)
            self.gui_dict['Trip_3_3'] = '{:.2f}'.format(self.flt_bmscellvmin)
    def guiUpdate(self):  # Means are parsed within this fxn to update GUI
        self.ui.Time.setText(self.gui_dict['Time'])
        if len(self.floop['Faults']) > 0:
            self.ui.CheckEngineButton.show()
        else:
            self.ui.CheckEngineButton.hide()
        if self.trip_selector == 1:  # Update unit labels for changed trip display.
            self.ui.Trip_1_1_prefix.setText('Wh<sub>use</sub>:')
            if self.units:
                self.ui.Trip_1_2_prefix.setText('Wh/km<sub>Trip</sub>:')
            else:
                self.ui.Trip_1_2_prefix.setText('Wh/mi<sub>Trip</sub>:')
            self.ui.Trip_1_3_prefix.setText('Ah<sub>use</sub>:')
            self.ui.Trip_2_1_prefix.setText('Wh<sub>rem</sub>:')
            self.ui.Trip_2_2_prefix.setText('Range:')
            self.ui.Trip_2_3_prefix.setText('Ah<sub>rem</sub>:')
            self.ui.Trip_3_1_prefix.setText('Wh<sub>reg</sub>:')
            if self.units:
                self.ui.Trip_3_2_prefix.setText('Km:')
            else:
                self.ui.Trip_3_2_prefix.setText('Miles:')
            self.ui.Trip_3_3_prefix.setText('Ah<sub>reg</sub>:')
        elif self.trip_selector == 2:
            self.ui.Trip_1_1_prefix.setText('Rng<sub>avg</sub>:')
            self.ui.Trip_1_2_prefix.setText('T<sub>trip</sub>:')
            self.ui.Trip_1_3_prefix.setText('A<sub>max</sub>:')
            self.ui.Trip_2_1_prefix.setText('Rng<sub>inst</sub>:')
            self.ui.Trip_2_2_prefix.setText('T<sub>mov</sub>:')
            self.ui.Trip_2_3_prefix.setText('V<sub>min</sub>:')
            self.ui.Trip_3_1_prefix.setText('T<sub>max</sub>:')
            #self.ui.Trip_3_2_prefix.setText('Miles: ')
            if self.units:
                self.ui.Trip_3_2_prefix.setText('Kmh<sub>mov</sub>:')
            else:
                self.ui.Trip_3_2_prefix.setText('Mph<sub>mov</sub>:')
            if self.units:
                self.ui.Trip_3_3_prefix.setText('Kmh<sub>max</sub>:')
            else:
                self.ui.Trip_3_3_prefix.setText('Mph<sub>max</sub>:')
        elif self.trip_selector == 3:
            self.ui.Trip_1_1_prefix.setText('T1<sub>Batt</sub>:')
            self.ui.Trip_1_2_prefix.setText('T2<sub>Batt</sub>:')
            self.ui.Trip_1_3_prefix.setText('T<sub>BMax</sub>:')  # Add self.flt_battmaxtemp
            self.ui.Trip_2_1_prefix.setText('T3<sub>Batt</sub>:')
            self.ui.Trip_2_2_prefix.setText('T4<sub>Batt</sub>:')
            self.ui.Trip_2_3_prefix.setText('A<sub>acc</sub>:')
            self.ui.Trip_3_1_prefix.setText('CV<sub>rng</sub>:')
            self.ui.Trip_3_2_prefix.setText('CV<sub>avg</sub>:')
            self.ui.Trip_3_3_prefix.setText('CV<sub>min</sub>:')

        self.ui.WhmiBar.setValue(int(self.flt_whmi_inst)) # Breaking dict format style but performance wins out.
        self.ui.WhmiLabel.setText(self.gui_dict['WhmiLabel'])
        self.ui.MotorTemperatureLabel.setText(self.gui_dict['MotorTemperatureLabel'])
        self.ui.MotorTemperatureBar.setValue(self.gui_dict['MotorTemperatureBar'])
        self.ui.BatteryVoltageLabel.setText(self.gui_dict['BatteryVoltageLabel'])
        self.ui.BatteryVoltageBar.setValue(self.gui_dict['BatteryVoltageBar'])
        self.ui.BatteryVoltageDropLabel.setText(self.gui_dict['BatteryVoltageDropLabel'])  # Label written as formatted str.
        self.ui.BatterySOCLabel.setText(self.gui_dict['BatterySOCLabel'])
        self.ui.BatterySOCBar.setValue(self.gui_dict['BatterySOCBar'])
        self.ui.SpeedGauge.update_value(self.gui_dict['SpeedGauge'])
        self.ui.SpeedGaugeLabel.setText(self.gui_dict['SpeedGaugeLabel'])
        self.ui.PowerGauge.update_value(self.gui_dict['PowerGauge'])
        self.ui.PowerGaugeLabel.setText(self.gui_dict['PowerGaugeLabel'])

        self.ui.Trip_1_1.setText(self.gui_dict['Trip_1_1'])
        self.ui.Trip_1_2.setText(self.gui_dict['Trip_1_2'])
        self.ui.Trip_1_3.setText(self.gui_dict['Trip_1_3'])
        self.ui.Trip_2_1.setText(self.gui_dict['Trip_2_1'])
        self.ui.Trip_2_2.setText(self.gui_dict['Trip_2_2'])
        self.ui.Trip_2_3.setText(self.gui_dict['Trip_2_3'])
        self.ui.Trip_3_1.setText(self.gui_dict['Trip_3_1'])
        self.ui.Trip_3_2.setText(self.gui_dict['Trip_3_2'])
        self.ui.Trip_3_3.setText(self.gui_dict['Trip_3_3'])
    def checkGPIO(self):
        #Profile Signaller.
        # 22/23 for 3p switch. if A = 1, if not A and not B = 2, if B = 3
        if GPIO.event_detected(22) or GPIO.event_detected(23):
            pinA = GPIO.input(22)
            pinB = GPIO.input(23)
            print('GPIO event; pinA: ', pinA, 'pinB: ', pinB)
            if pinA:
                self.signalProfile(True, -11)
            if not pinA and not pinB:
                self.signalProfile(True, -12)
            if pinB:
                self.signalProfile(True, -13)

    #### Main Display Command Functions and BAC Signals ####
    def tripRangeEnable(self, bool, range):
        # todo: check that slider dynamically updates self.flt_range_limit
        if bool:
            self.opt_tripRangeValue = bool
            self.flt_range_limit = range
            self.pid.auto_mode = True
            self.opt_tripRangeValue = True
        elif not bool:
            self.bacqueue.put([-15])  # Code to reset range power limiter
            self.pid_auto_mode = False
            self.opt_tripRangeValue = False
        # Add var so GUI knows active profile amps. --> self.profile -11 = 1, -12 = 2...
    def tripRangeLimiter(self):
        # Check which profile is active. Wh =/= Ah but they are proportional, and no ASI pwr limit exists.
        if self.profile == -11:
            indice = ()
            #Return 1st, 2nd index in list of Setup profile tuples for 'Battery Current Limit'
            for i, tup in enumerate(self.setup['profile1']):
                print('i:', i, tup)
                for ii, string in enumerate(tup):
                    print('ii:', ii, string)
                    try:
                        if 'Battery_Current_Limit' in string:
                            indice = (i, ii+1)
                    except Exception as e:
                        print('profile1;', e)
                        pass
            max_amps = self.setup['profile1'][indice[0]][indice[1]]
        elif self.profile == -12:
            indice = 0
            for i, tup in enumerate(self.setup['profile2']):
                print('i:', i, tup)
                for ii, string in enumerate(tup):
                    print('ii:', ii, string)
                    try:
                        if 'Battery_Current_Limit' in string:
                            indice = (i, ii+1)
                    except Exception as e:
                        print('profile2;', e)
                        pass
            max_amps = self.setup['profile2'][indice[0]][indice[1]]
        elif self.profile == -13:
            indice = 0
            for i, tup in enumerate(self.setup['profile3']):
                print('i:', i, tup)
                for ii, string in enumerate(tup):
                    print('ii:', ii, string)
                    try:
                        if 'Battery_Current_Limit' in string:
                            indice = (i, ii+1)
                    except Exception as e:
                        print('profile3;', e)
                        pass
            max_amps = self.setup['profile3'][indice[0]][indice[1]]
        range_div = ((self.get_battwh()) / (self.flt_whmi_inst)) / self.flt_range_limit
        # Instantaneous range / range limit
        # Setpoint is 1, :. range / range limit = 1 is target.
        limit = self.pid.__call__(range_div, self.list_floop_interval[-1:])
        self.bacqueue.emit([int(limit * max_amps)])
    def tripReset(self, bool):
        if bool: # Reset all variables of floop_to_list, and flt.
            self.flt_batt_volts, self.flt_batt_volts_max, self.flt_batt_volts_min, self.flt_batt_amps_max, \
            self.flt_motor_temp_max, self.flt_batt_amps_max, self.flt_batt_volts_drop, self.flt_motor_amps, \
            self.flt_soc, self.flt_range, self.flt_range_limit, self.flt_whmi_avg, self.flt_whmi_inst, self.flt_dist, \
            self.flt_wh, self.flt_ah, self.flt_whregen, self.flt_ahregen, self.flt_bmscellvrng, self.flt_bmscellvmean, \
            self.flt_bmsmaxtemp, self.flt_bmscellvmin, self.flt_bmsah, self.flt_bmswh, self.flt_bmsahregen, self.flt_bmswhregen = \
                float(0), float(0), float(0), float(0), float(0), float(0), float(0), float(0), float(0), float(0), \
                float(0), float(0), float(0), float(0), float(0), float(0), float(0), float(0), float(0), float(0), \
                float(0), float(0), float(0), float(0), float(0), float(0),
            #iterators:
            self.exceptions, self.iter, self.iter_sql, self.iter_bmsmsg, self.iter_attribute_slicer = 0, 0, 0, 0, 0
            #clear lists:
            self.list_batt_amps, self.list_batt_volts, self.list_motor_amps, self.list_motor_temp, self.list_speed, \
            self.list_motor_rpm, self.list_floop_interval, self.list_whmi, \
            self.list_bms_interval, self.list_bms_amps, self.list_bms_volts = \
                [], [], [], [], [], [], [], [], [], [], []
            #reset trip timer:
            self.start_time = self.ms()
            self.first_floop = True
            #QtCore.QTimer.singleShot(1000, lambda: self.socreset())
    def tripPidUpdateTune(self, kp, ki, kd):
        self.pid_kp = kp / 200  # /200 to convert QSlider int to float coefficient
        self.pid_ki = ki / 200
        self.pid_kd = kd / 200
        print('PID tunings: ', self.pid_kp, self.pid_ki, self.pid_kd)
        self.pid.tunings = (kp, ki, kd)
        self.optpopupwindow.ui.PID_Kp_Label.setText('{:.2f}'.format(self.pid_kp))
        self.optpopupwindow.ui.PID_Ki_Label.setText('{:.2f}'.format(self.pid_ki))
        self.optpopupwindow.ui.PID_Kd_Label.setText('{:.2f}'.format(self.pid_kd))
    def signalFaultReset(self):
        self.bacqueue.put([-14]) # clear BAC faults
        self.bmsqueue.put(2) # clear BMS faults
    def signalAssistLevel(self):
        self.assist_level = -(self.ui.AssistSlider.value()+1)
        self.ui.AssistSliderLabel.setText('Assist: ' + str(self.ui.AssistSlider.value()))
        self.bacqueue.put([self.assist_level])  # Positive integers in worker reserved for trip limiter %'s
        self.SQL_update_setup()
    def signalProfile(self, button_bool, command):
        if button_bool == True:
            self.bacqueue.put([command])  # command is integer (-11 = profile1, -12 = profile2...)
        self.profile = command
        #if command == -11: # Added for GPIO, debugging recursion....
        #    self.ui.ProfileRb1.setChecked(True)
        #elif command == -12:
        #    self.ui.ProfileRb2.setChecked(True)
        #elif command == -13:
        #    self.ui.ProfileRb2.setChecked(True)
        #self.SQL_update_setup() # not needed; do each 2sec
    def signalReverse(self, bool):
        if bool:
            self.ui.Reverse.setText('R')
            self.bacqueue.put([-18])
        if not bool:
            self.ui.Reverse.setText('D')
            self.bacqueue.put([-19])
    def signalAntitheft(self, bool):
        if bool:
            # emit signal to enable antitheft
            self.popupAntitheft()
            print('Antitheft signal true, enabling antitheft...')
            self.bacqueue.put([-17])
        if not bool:
            # Emit signal here to disable antitheft
            # Close popup within number_pad.py
            print('Antitheft signal false, disabling antitheft...')
            self.bacqueue.put([-16])
    def signalTripRangeLimiter(self, bool, value):
        if bool:
            self.flt_range_limit = value
        elif not bool:
            self.flt_range_limit = 0
    def signalThrottleBypassAssist(self, bool):
        if bool:
            self.bacqueue.put([-20])
            self.opt_throttleAssistBool = True
            self.SQL_update_setup()
        if not bool:
            self.bacqueue.put([-21])
            self.opt_throttleAssistBool = False
            self.SQL_update_setup()
    def signalBatta(self, bool, value): # Bool = btn, value = slider
        if bool:
            self.bacqueue.put([-30, value])
            self.opt_battaValue = value
            self.optpopupwindow.ui.BattPowerLabel.setText('BattAmp:' + '{:.0f}'.format(value) + '%')
        if not bool or self.opt_battaValue == 0:
            self.opt_battaValue = 0
            self.optpopupwindow.ui.BattPowerBtn.setChecked(False)
            self.optpopupwindow.ui.BattPowerLabel.setText('BattAmp: 0%')
    def signalMota(self, bool, value): # Bool = btn, value = slider
        if bool:
            print('mota:', value)
            self.bacqueue.put([-34, value])
            self.opt_motaValue = value
            self.optpopupwindow.ui.MotPowerLabel.setText('MotAmp:' + '{:.0f}'.format(value)+ '<sub>A</sub>')
        if not bool or self.opt_motaValue == 0:
            self.opt_battaValue = 0
            self.optpopupwindow.ui.MotPowerBtn.setChecked(False)
            self.optpopupwindow.ui.MotPowerLabel.setText('MotAmp: 0<sub>A</sub>')
    def signalFlux(self, bool, value):
        val = value/10 #500 int -> 50.0%
        if bool:
            self.bacqueue.put([-31, val])
            self.opt_fluxValue = val #
            self.optpopupwindow.ui.FluxLabel.setText('Flux: ' + '{:.1f}'.format(val) + '%')
        if not bool or self.opt_fluxValue == 0: # and to both disable signals when slider to 0, and detect 0 for sql setup
            self.bacqueue.put([-31, 0])
            self.opt_fluxValue = 0
            self.optpopupwindow.ui.FluxBtn.setChecked(False)
            self.optpopupwindow.ui.FluxLabel.setText('Flux: 0')
    def signalBMSMsgBAC(self, soc, temp): #-32 bacqueue
        self.bacqueue.put([-32, soc, temp])
    def signalDiagnosticPoller(self, bool):
        if bool:
            self.bacqueue.put([-29])
        else:
            self.bacqueue.put([0])
    def diagnosticsReceive(self, msg):
        self.optpopupwindow.ui.DiagThrottleV.setText('{:.4f}'.format(msg['Throttle_Voltage']))
        self.optpopupwindow.ui.DiagBMSV.setText('{:.4f}'.format(msg['Throttle_Voltage']))
        self.optpopupwindow.ui.DiagBrake1V.setText('{:.4f}'.format(msg['Brake_1_Voltage']))
        self.optpopupwindow.ui.DiagBrake2V.setText('{:.4f}'.format(msg['Brake_2_Voltage']))
        self.optpopupwindow.ui.DiagEbikeFlags.setText(', '.join(msg['EbikeFlags']))
        self.optpopupwindow.ui.DiagDigitalInputs.setText(', '.join(msg['DigitalInputs']))
        self.optpopupwindow.ui.DiagWarnings.setText(', '.join(msg['Warnings']))
        self.optpopupwindow.ui.DiagSensorless.setText(msg['SensorlessState'])
    def signalHackBACAccessCode(self, bool):
        if bool:
            self.bacqueue.put([-33])
    def receiveHackBACAccessCode(self, msg):
        level = msg[0]
        val = msg[1]
        if level == 1:
            self.optpopupwindow.ui.HackAccessLabel_code1.setText(('1: ' + str(val)))
            with open((os.path.abspath((os.path.dirname(__file__)))) + '/access_codes.csv', mode='w') as file:
                writer = csv.writer(file, delimiter = ',')
                writer.writerow(['Level 1 Access Code: ' + str(val)])
                file.close()
        if level == 2:
            self.optpopupwindow.ui.HackAccessLabel_code1.setText('2: ' + str(val))
            with open((os.path.abspath((os.path.dirname(__file__)))) + '/access_codes.csv', mode='w') as file:
                writer = csv.writer(file, delimiter = ',')
                writer.writerow(['Level 2 Access Code: ' + str(val)])
                file.close()
        if level == 3:
            self.optpopupwindow.ui.HackAccessLabel_code1.setText('3: ' + str(val))
            with open((os.path.abspath((os.path.dirname(__file__)))) + '/access_codes.csv', mode='w') as file:
                writer = csv.writer(file, delimiter = ',')
                writer.writerow(['Level 3 Access Code: ' + str(val)])
                file.close()

        #self.optpopupwindow.ui.HackAccessLabel.setText('Level:', level, '#:', val)

    #### Subwindow Calls ####
    def popupFault(self):  # Check Controller indicator.
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Fault Detected")
        msg.setText('Faults detected: ' + str(self.floop['Faults']).replace('[', '').replace(']', ''))
        #todo: make a custom window instead of MessageBox. Separate BMS/BAC fault clearing.
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setStandardButtons(QtWidgets.QMessageBox.Reset | QtWidgets.QMessageBox.Ignore)
        msg.buttonClicked.connect(self.signalFaultReset)
        msg.exec_()
    def popupAntitheft(self):
        self.pinpopup = numberPopup(self.ui, self.setup['pin'], self.signalAntitheft)
        # self.pinpopup.setParent(self.ui.centralwidget)
        self.pinpopup.setStyleSheet('QPushButton {border-style: inset;border-color: dark grey;'
        'border-width: 3px;border-radius:10px;font: 40pt "Luxi Mono";font-weight: bold;padding: 0px 0px 0px 0px;} '
                                    'QPushButton::pressed{border-style: outset;}'
                                    'QLineEdit{font: 40pt "Luxi Mono";font-weight: bold;}')
        #self.pinpopup.move(self.ui.centralwidget.rect().center() + QtCore.QPoint(self.pinpopup.width()/5, 37))
        # For some reason 'numberPopup' doesn't center like other custom .ui widgets. Below fix only valid for 800x480
        self.pinpopup.move(QtCore.QPoint(0, 0))
        self.pinpopup.showMaximized()
        self.pinpopup.show()
    def popupOptions(self):  #  Independent widget
        # todo: initialize states of btns. if self.optpopupwindow: self.___set(self.___)
        #  Check if 'closing' window just hides it and if so, instead of re-intializing and re-populating just unhide
        self.optpopupwindow = optionsDialog(self.displayinvert_bool)
        self.optpopupwindow.displayinvertmsg.connect(self.displayinverter)
        self.optpopupwindow.displaybacklightcmd.connect(self.displaybacklight)
        self.optpopupwindow.ui.ThrottleBypassBtn.toggled.connect(lambda: self.signalThrottleBypassAssist(
            self.optpopupwindow.ui.ThrottleBypassBtn.isChecked()))
        self.optpopupwindow.ui.FluxSlider.valueChanged.connect(lambda: self.signalFlux(
            self.optpopupwindow.ui.FluxBtn.isChecked(), self.optpopupwindow.ui.FluxSlider.value()))
        self.optpopupwindow.ui.BattPowerSlider.valueChanged.connect(lambda: self.signalBatta(
            self.optpopupwindow.ui.BattPowerBtn.isChecked(), self.optpopupwindow.ui.BattPowerSlider.value()))
        self.optpopupwindow.ui.MotPowerSlider.valueChanged.connect(lambda: self.signalMota(
            self.optpopupwindow.ui.MotPowerBtn.isChecked(), self.optpopupwindow.ui.MotPowerSlider.value()))
        self.optpopupwindow.ui.TripReset.clicked.connect(lambda: self.tripReset(True))
        self.optpopupwindow.ui.DiagnosticsUpdateBtn.toggled.connect(lambda:
            self.signalDiagnosticPoller(self.optpopupwindow.ui.DiagnosticsUpdateBtn.isChecked()))
        self.optpopupwindow.ui.HackAccessBtn.toggled.connect(lambda:
            self.signalHackBACAccessCode(self.optpopupwindow.ui.HackAccessBtn.isChecked()))
        #self.optpopupwindow.showMaximized()
        self.optpopupwindow.show()
    def popupBms(self):  #  Inherited widget
        #self.bmspopup.bmspoll.connect(BMSSerialThread.bmspoller)
        #self.bmspopup.bmscut.connect(window.bmscutoff)
        #self.bmspopupwindow.bmscut.connect(self.bmspopEepromWrite)
        #self.bmsqueue.put(1)
        self.bmspopupwindow = bmsDialog(self.battseries)
        self.bmsbasiccmd.connect(self.bmspopupwindow.bmsBasicUpdate)
        self.bmseepromcmd.connect(self.bmspopupwindow.bmsEepromUpdate)
        self.bmspopupwindow.bmsEepromUpdate(self.processEmitter.eepromMsg)
        # Connect Btns
        self.bmspopupwindow.ui.SaveEepromBtn.clicked.connect(self.bmspopEepromWrite)
        self.bmspopupwindow.ui.ConfigBtn.clicked.connect(self.popupBmsCfg)
        self.bmspopupwindow.show()
    def popupBmsCfg(self):
        self.bmscfgpopupwindow = bmscfgDialog()
        self.bmscfgpopupwindow.ui.ExitBtn.clicked.connect(lambda: self.bmscfgpopupwindow.hide())
        self.bmscfgpopupwindow.bmscfgGuiUpdate(self.processEmitter.eepromMsg)
        self.bmscfgpopupwindow.ui.ReadEepromBtn.clicked.connect(lambda: self.bmsqueue.put(1))
        self.bmscfgpopupwindow.ui.WriteEepromBtn.clicked.connect(self.bmscfgpopEepromWrite)

        self.bmscfgpopupwindow.show()
    #### BMS FUNCTIONS #####
    # todo: add BMS EEPROM SQL backups
    def bmsCall(self):
        # 0 = Poll Basic Info, 1 = Read EEPROM, 2 = Write EEPROM
        #print('bmsCall: ', self.bmscmd)
        if self.bmscmd == 0:
            #print('called: ', self.bmscmd)
            self.bmsqueue.put(0)
        elif self.bmscmd == 1:
            self.bmsqueue.put(1)
            self.bmscmd = 0
        elif self.bmscmd == 2:
            #msg = (2, self.bmsemitter.eepromMsg[0]) # Now using len to detect write, 2 = clear faults.
            self.bmsqueue.put(2)
            self.bmscmd = 0
        elif self.bmscmd == 10:
            self.bmsqueue.put(0)
            self.bmsqueue.put(1)
            self.bmscmd = 0
    @QtCore.pyqtSlot()
    def bmsGetEeprom(self):
        self.bmscmd = 1
        self.bmsCall()
    def bmsGuiUpdate(self):
        # Get CellV's to find min/max for Range/Diff labels
        keys = ['cell0_mv', 'cell1_mv', 'cell2_mv', 'cell3_mv', 'cell4_mv', 'cell5_mv', 'cell6_mv', 'cell7_mv',
                'cell8_mv', 'cell9_mv', 'cell10_mv', 'cell11_mv', 'cell12_mv', 'cell13_mv', 'cell14_mv', 'cell15_mv',
                 'cell16_mv', 'cell17_mv', 'cell18_mv', 'cell19_mv', 'cell20_mv', 'cell21_mv', 'cell22_mv',
                'cell23_mv', 'cell24_mv']
        cellv = []
        for i in range(self.battseries):
            cellv.append(self.processEmitter.basicMsg[0][keys[i]] / 1000) # mv -> V
        cellvmin = min(cellv)
        cellvmax = max(cellv)
        self.bmspopupwindow.ui.VRangeLabel.setText('{:.2f}'.format(cellvmax) + '~' + '{:.2f}'.format(cellvmin)
                                                   + '<sub>V</sub>')
        self.bmspopupwindow.ui.VDiffLabel.setText('{:.3f}'.format(cellvmin - cellvmax))
        # Temp, Current, Power
        self.bmspopupwindow.ui.CurrentLabel.setText('{:.2f}'.format(self.processEmitter.basicMsg[1]['pack_ma'] / 1000) + '<sub>A</sub>')
        self.bmspopupwindow.ui.BattPowerLabel.setText('{:.1f}'.format(((self.processEmitter.basicMsg[1]['pack_ma'] / 1000) *
                                                                       (self.processEmitter.basicMsg[1]['pack_mv'] / 1000))) + '<sub>W</sub>')
        self.bmspopupwindow.ui.T1Bar.setValue(self.processEmitter.basicMsg[1]['ntc0'])
        self.bmspopupwindow.ui.T2Bar.setValue(self.processEmitter.basicMsg[1]['ntc1'])
        self.bmspopupwindow.ui.T3Bar.setValue(self.processEmitter.basicMsg[1]['ntc2'])
        self.bmspopupwindow.ui.T4Bar.setValue(self.processEmitter.basicMsg[1]['ntc3'])
        # Voltage Bars & Balance Labels # Interleaved to support <24s configurations), cheaper to `try` here
        try:
            self.bmspopupwindow.ui.C1Bar.setValue(self.processEmitter.basicMsg[0]['cell0_mv'])
            self.bmspopupwindow.ui.C1Balance.setChecked(self.processEmitter.basicMsg[1]['bal0'])
            self.bmspopupwindow.ui.C2Bar.setValue(self.processEmitter.basicMsg[0]['cell1_mv'])
            self.bmspopupwindow.ui.C2Balance.setChecked(self.processEmitter.basicMsg[1]['bal1'])
            self.bmspopupwindow.ui.C3Bar.setValue(self.processEmitter.basicMsg[0]['cell2_mv'])
            self.bmspopupwindow.ui.C3Balance.setChecked(self.processEmitter.basicMsg[1]['bal2'])
            self.bmspopupwindow.ui.C4Bar.setValue(self.processEmitter.basicMsg[0]['cell3_mv'])
            self.bmspopupwindow.ui.C4Balance.setChecked(self.processEmitter.basicMsg[1]['bal3'])
            self.bmspopupwindow.ui.C5Bar.setValue(self.processEmitter.basicMsg[0]['cell4_mv'])
            self.bmspopupwindow.ui.C5Balance.setChecked(self.processEmitter.basicMsg[1]['bal4'])
            self.bmspopupwindow.ui.C6Bar.setValue(self.processEmitter.basicMsg[0]['cell5_mv'])
            self.bmspopupwindow.ui.C6Balance.setChecked(self.processEmitter.basicMsg[1]['bal5'])
            self.bmspopupwindow.ui.C7Bar.setValue(self.processEmitter.basicMsg[0]['cell6_mv'])
            self.bmspopupwindow.ui.C7Balance.setChecked(self.processEmitter.basicMsg[1]['bal6'])
            self.bmspopupwindow.ui.C8Bar.setValue(self.processEmitter.basicMsg[0]['cell7_mv'])
            self.bmspopupwindow.ui.C8Balance.setChecked(self.processEmitter.basicMsg[1]['bal7'])
            self.bmspopupwindow.ui.C9Bar.setValue(self.processEmitter.basicMsg[0]['cell8_mv'])
            self.bmspopupwindow.ui.C9Balance.setChecked(self.processEmitter.basicMsg[1]['bal8'])
            self.bmspopupwindow.ui.C10Bar.setValue(self.processEmitter.basicMsg[0]['cell9_mv'])
            self.bmspopupwindow.ui.C10Balance.setChecked(self.processEmitter.basicMsg[1]['bal9'])
            self.bmspopupwindow.ui.C11Bar.setValue(self.processEmitter.basicMsg[0]['cell10_mv'])
            self.bmspopupwindow.ui.C11Balance.setChecked(self.processEmitter.basicMsg[1]['bal10'])
            self.bmspopupwindow.ui.C12Bar.setValue(self.processEmitter.basicMsg[0]['cell11_mv'])
            self.bmspopupwindow.ui.C12Balance.setChecked(self.processEmitter.basicMsg[1]['bal11'])
            self.bmspopupwindow.ui.C13Bar.setValue(self.processEmitter.basicMsg[0]['cell12_mv'])
            self.bmspopupwindow.ui.C13Balance.setChecked(self.processEmitter.basicMsg[1]['bal12'])
            self.bmspopupwindow.ui.C14Bar.setValue(self.processEmitter.basicMsg[0]['cell13_mv'])
            self.bmspopupwindow.ui.C14Balance.setChecked(self.processEmitter.basicMsg[1]['bal13'])
            self.bmspopupwindow.ui.C15Bar.setValue(self.processEmitter.basicMsg[0]['cell14_mv'])
            self.bmspopupwindow.ui.C15Balance.setChecked(self.processEmitter.basicMsg[1]['bal14'])
            self.bmspopupwindow.ui.C16Bar.setValue(self.processEmitter.basicMsg[0]['cell15_mv'])
            self.bmspopupwindow.ui.C16Balance.setChecked(self.processEmitter.basicMsg[1]['bal15'])
            self.bmspopupwindow.ui.C17Bar.setValue(self.processEmitter.basicMsg[0]['cell16_mv'])
            self.bmspopupwindow.ui.C17Balance.setChecked(self.processEmitter.basicMsg[1]['bal16'])
            self.bmspopupwindow.ui.C18Bar.setValue(self.processEmitter.basicMsg[0]['cell17_mv'])
            self.bmspopupwindow.ui.C18Balance.setChecked(self.processEmitter.basicMsg[1]['bal17'])
            self.bmspopupwindow.ui.C19Bar.setValue(self.processEmitter.basicMsg[0]['cell18_mv'])
            self.bmspopupwindow.ui.C19Balance.setChecked(self.processEmitter.basicMsg[1]['bal18'])
            self.bmspopupwindow.ui.C20Bar.setValue(self.processEmitter.basicMsg[0]['cell19_mv'])
            self.bmspopupwindow.ui.C20Balance.setChecked(self.processEmitter.basicMsg[1]['bal19'])
            self.bmspopupwindow.ui.C21Bar.setValue(self.processEmitter.basicMsg[0]['cell20_mv'])
            self.bmspopupwindow.ui.C21Balance.setChecked(self.processEmitter.basicMsg[1]['bal20'])
            self.bmspopupwindow.ui.C22Bar.setValue(self.processEmitter.basicMsg[0]['cell21_mv'])
            self.bmspopupwindow.ui.C22Balance.setChecked(self.processEmitter.basicMsg[1]['bal21'])
            self.bmspopupwindow.ui.C23Bar.setValue(self.processEmitter.basicMsg[0]['cell22_mv'])
            self.bmspopupwindow.ui.C23Balance.setChecked(self.processEmitter.basicMsg[1]['bal22'])
            self.bmspopupwindow.ui.C24Bar.setValue(self.processEmitter.basicMsg[0]['cell23_mv'])
            self.bmspopupwindow.ui.C24Balance.setChecked(self.processEmitter.basicMsg[1]['bal23'])
        except AttributeError:
            pass # Ignore missing UI elements.
    @QtCore.pyqtSlot()
    def bmspopEepromWrite(self):
        # Get bmspop eeprom values, update eeprom, send all to bmsProc
        msg = self.processEmitter.eepromMsg
        msg[0]['bal_start'] = self.bmspopupwindow.ui.BalanceLevelSlider.value()
        msg[0]['covp'] = self.bmspopupwindow.ui.ChargeLevelSlider.value()
        msg[0]['covp_release'] = self.bmspopupwindow.ui.ChargeLevelSlider.value() + 50  # +0.05V default release
        self.processEmitter.eepromMsg = msg
        print('bmspopEepromWrite: ', self.processEmitter.eepromMsg, '\n', msg)
        self.bmsqueue.put(msg)
        #self.bmsWriteEeprom()
    def bmscfgpopEepromWrite(self):
        msg = self.processEmitter.eepromMsg
        msg[0]['switch'] = self.bmscfgpopupwindow.ui.SwitchBtn.isChecked()
        msg[0]['scrl'] = self.bmscfgpopupwindow.ui.SCReleaseBtn.isChecked()
        msg[0]['balance_en'] = self.bmscfgpopupwindow.ui.BalanceEnableBtn.isChecked()
        msg[0]['chg_balance_en'] = self.bmscfgpopupwindow.ui.ChargeBalanceBtn.isChecked()
        msg[0]['led_en'] = self.bmscfgpopupwindow.ui.LEDEnableBtn.isChecked()
        msg[0]['led_num'] = self.bmscfgpopupwindow.ui.LEDNumberBtn.isChecked()
        msg[0]['ntc1'] = self.bmscfgpopupwindow.ui.NTC1Btn.isChecked()
        msg[0]['ntc2'] = self.bmscfgpopupwindow.ui.NTC2Btn.isChecked()
        msg[0]['ntc3'] = self.bmscfgpopupwindow.ui.NTC3Btn.isChecked()
        msg[0]['ntc4'] = self.bmscfgpopupwindow.ui.NTC4Btn.isChecked()
        msg[0]['ntc5'] = self.bmscfgpopupwindow.ui.NTC5Btn.isChecked()
        msg[0]['ntc6'] = self.bmscfgpopupwindow.ui.NTC6Btn.isChecked()
        msg[0]['ntc7'] = self.bmscfgpopupwindow.ui.NTC7Btn.isChecked()
        msg[0]['ntc8'] = self.bmscfgpopupwindow.ui.NTC8Btn.isChecked()
        # Balance and Misc Configuration
        msg[0]['bal_start']  = self.bmscfgpopupwindow.ui.BalanceStartSpin.value() * 1000
        msg[0]['bal_window'] = self.bmscfgpopupwindow.ui.BalanceWindowSpin.value()
        msg[0]['shunt_res'] = self.bmscfgpopupwindow.ui.ShuntSpin.value()
        msg[0]['cycle_cnt'] = self.bmscfgpopupwindow.ui.CycleCountSpin.value()
        msg[0]['design_cap'] = self.bmscfgpopupwindow.ui.DesignCapSpin.value() * 1000
        msg[0]['cycle_cap'] = self.bmscfgpopupwindow.ui.CycleCapSpin.value() * 1000
        msg[0]['cap_100'] = self.bmscfgpopupwindow.ui.SOC100Spin.value()
        msg[0]['cap_80'] = self.bmscfgpopupwindow.ui.SOC80Spin.value()
        msg[0]['cap_60'] = self.bmscfgpopupwindow.ui.SOC60Spin.value()
        msg[0]['cap_40'] = self.bmscfgpopupwindow.ui.SOC40Spin.value()
        msg[0]['cap_20'] = self.bmscfgpopupwindow.ui.SOC20Spin.value()
        msg[0]['cap_0'] = self.bmscfgpopupwindow.ui.SOC0Spin.value()
        msg[0]['dsg_rate'] = self.bmscfgpopupwindow.ui.SelfDschgSpin.value()
        msg[0]['fet_ctrl'] = self.bmscfgpopupwindow.ui.FETControlSpin.value()
        msg[0]['led_timer'] = self.bmscfgpopupwindow.ui.LEDTimerSpin.value()
        msg[0]['cell_cnt'] = self.bmscfgpopupwindow.ui.CellCntSpin.value()
        # Protection Configuration
        msg[0]['covp'] = self.bmscfgpopupwindow.ui.COVPSpin.value() * 1000
        msg[0]['cuvp'] = self.bmscfgpopupwindow.ui.CUVPSpin.value() * 1000
        msg[0]['povp'] = self.bmscfgpopupwindow.ui.POVPSpin.value() * 1000
        msg[0]['puvp'] = self.bmscfgpopupwindow.ui.PUVPSpin.value() * 1000
        msg[0]['chgot'] = self.bmscfgpopupwindow.ui.CHGOTSpin.value()
        msg[0]['chgut'] = self.bmscfgpopupwindow.ui.CHGUTSpin.value()
        msg[0]['dsgot'] = self.bmscfgpopupwindow.ui.DSGOTSpin.value()
        msg[0]['dsgut'] = self.bmscfgpopupwindow.ui.DSGUTSpin.value()
        msg[0]['chgoc'] = self.bmscfgpopupwindow.ui.CHGOCSpin.value() * 1000
        msg[0]['dsgoc'] = self.bmscfgpopupwindow.ui.DSCHOCSpin.value() * 1000
        msg[0]['covp_rel'] = self.bmscfgpopupwindow.ui.COVPReleaseSpin.value() * 1000
        msg[0]['cuvp_rel'] = self.bmscfgpopupwindow.ui.CUVPReleaseSpin.value() * 1000
        msg[0]['povp_rel'] = self.bmscfgpopupwindow.ui.POVPReleaseSpin.value() * 1000
        msg[0]['puvp_rel'] = self.bmscfgpopupwindow.ui.PUVPReleaseSpin.value() * 1000
        msg[0]['chgot_rel'] = self.bmscfgpopupwindow.ui.CHGOTReleaseSpin.value()
        msg[0]['chgut_rel'] = self.bmscfgpopupwindow.ui.CHGUTReleaseSpin.value()
        msg[0]['dsgot_rel'] = self.bmscfgpopupwindow.ui.DSGOTReleaseSpin.value()
        msg[0]['dsgut_rel'] = self.bmscfgpopupwindow.ui.DSGUTReleaseSpin.value()
        msg[0]['chgoc_rel'] = self.bmscfgpopupwindow.ui.CHGOCReleaseSpin.value()
        msg[0]['dsgoc_rel'] = self.bmscfgpopupwindow.ui.DSCHOCReleaseSpin.value()
        msg[0]['covp_delay'] = self.bmscfgpopupwindow.ui.COVPDelaySpin.value()
        msg[0]['cuvp_delay'] = self.bmscfgpopupwindow.ui.CUVPDelaySpin.value()
        msg[0]['povp_delay'] = self.bmscfgpopupwindow.ui.POVPDelaySpin.value()
        msg[0]['puvp_delay'] = self.bmscfgpopupwindow.ui.PUVPDelaySpin.value()
        msg[0]['chgot_delay'] = self.bmscfgpopupwindow.ui.CHGOTDelaySpin.value()
        msg[0]['chgut_delay'] = self.bmscfgpopupwindow.ui.CHGUTDelaySpin.value()
        msg[0]['dsgot_delay'] = self.bmscfgpopupwindow.ui.DSGOTDelaySpin.value()
        msg[0]['dsgut_delay'] = self.bmscfgpopupwindow.ui.DSGUTDelaySpin.value()
        msg[0]['chgoc_delay'] = self.bmscfgpopupwindow.ui.CHGOCDelaySpin.value()
        msg[0]['dsgoc_delay'] = self.bmscfgpopupwindow.ui.DSCHOCDelaySpin.value()
        # Finally, send updated eeprom to bms.
        self.bmsqueue.put(msg)
    def bmsProcessBasic(self):
        x_interval = array([sum(([(self.list_bms_interval[-self.iter_bmsmsg_threshold:])[:i]
                                  for i in range(1, self.iter_bmsmsg_threshold + 1, 1)])
                                [i]) for i in range(self.iter_bmsmsg_threshold)])
        ampsec = simps(array(self.list_bms_amps[-self.iter_bmsmsg_threshold:]), x=x_interval, even='avg')
        power = array(self.list_bms_amps[-self.iter_bmsmsg_threshold:]) * \
                array(self.list_bms_volts[-self.iter_bmsmsg_threshold:])
        wattsec = simps(power, x=x_interval, even='avg')
        #print('bms: ', ampsec, wattsec, '\n', ampsec/3600, wattsec/3600, '\n', power)
        #todo: Wh used/rem counter is still reversed during charging.
        #  bmshah/bmswh/__regen vars used for nothing.
        #  FIXED: TripReset doesn't reset Time<sub>trip</sub> in #2 parameter display.
        #  FIXED: Or CV<sub>min</sub>
        #  FIXED: Options Pane BatAmp/MotAmp labels don't update on slider toggle.
        #  FIXED: When button pressed, BattAmp slider updates MotorAmp label!
        #  FIXED: MotAmp still doesn't with button.
        #  Update options pane with values from profile or with special controller cmd.
        #  Range label doesn't update.
        #  FIXEDFlux label always updates to Flux: 0
        #  FIXED: Check PrintScrn for slider fault error
        if ampsec <= 0:
            self.flt_ah -= ampsec / 3600
            self.flt_bmsah -= ampsec / 3600
            self.chargestate = False
        elif ampsec > 0:
            self.flt_ah -= ampsec / 3600
            self.flt_bmsah -= ampsec / 3600
            self.flt_bmsahregen += abs(ampsec / 3600)
            # Set chargestarted to detect end of charge, and create new row in SQL lifestats to mark cycle.
            self.chargestate = True
            self.SQL_lifestat_upload_bms()
        if wattsec <= 0:
            self.flt_wh -= wattsec / 3600
            self.flt_bmswh -= wattsec / 3600
        elif wattsec > 0:
            self.flt_wh -= wattsec / 3600
            self.flt_bmswh -= wattsec / 3600
            self.flt_bmswhregen += abs(wattsec / 3600)
        if not self.chargestate: # todo verify correct boolean
            self.SQL_lifestat_upload_bms()
    @QtCore.pyqtSlot()
    def bmsReceiveBasic(self):
        self.iter_bmsmsg += 1
        # Store data for couloumb counting
        self.list_bms_interval.append(self.processEmitter.basicMsg[3])
        self.list_bms_amps.append(self.processEmitter.basicMsg[1]['pack_ma'] / 1000)
        self.list_bms_volts.append(self.processEmitter.basicMsg[1]['pack_mv'] / 1000)

        # Process cellV's, if new low minimum, store
        keys = self.processEmitter.basicMsg[0].keys()
        cellv = []
        for i in keys:
            cellv.append(self.processEmitter.basicMsg[0][i] / 1000)
        cellvmin = min(cellv)
        cellvmax = max(cellv)
        self.flt_bmscellvrng = (cellvmax - cellvmin)
        self.flt_bmscellvmean = mean(cellv)
        if cellvmin < self.flt_bmscellvmin:
            self.flt_bmscellvmin = cellvmin
        if self.flt_bmscellvmin == 0:
            self.flt_bmscellvmin = cellvmin

        # Process NTC temp, if new max, store
        self.bmstemps = [self.processEmitter.basicMsg[1]['ntc0'], self.processEmitter.basicMsg[1]['ntc1'],
                         self.processEmitter.basicMsg[1]['ntc2'], self.processEmitter.basicMsg[1]['ntc3']]
        try:
            if max(self.bmstemps) > self.flt_bmsmaxtemp:
                self.flt_bmsmaxtemp = max(self.bmstemps)
        except TypeError:
            pass
        # Update Main BatteryTemperatureBar
        maxtemp = int(max(self.bmstemps))
        self.ui.BatteryTemperatureBar.setValue(maxtemp)
        # Process pack_ma to detect charging, accessory current drain.
        # todo: detect here whether pack_ma is negative, use to open bmspop, set charge bool and store SOC,
        #  then when not negative, use QTimer.singleShot(5000?) to store %SOC charged after ~stable voltage.
        #  Additionally interpolate

        try:
            if self.bmspopupwindow.isVisible():
                self.bmsbasiccmd.emit(self.processEmitter.basicMsg)
        except AttributeError:
            pass
        # 11 ~= 2 seconds
        if self.iter_bmsmsg >= self.iter_bmsmsg_threshold:
            self.bmsProcessBasic()
            mincellsoc = int(BAC.socmapper(cellvmin))
            self.signalBMSMsgBAC(mincellsoc, maxtemp)
            #self.bacqueue.put([-32, int(self.flt_soc), maxtemp])
            self.iter_bmsmsg = 0

        if self.processEmitter.basicMsg[1]['covp_err']:
            self.bmsExceptionReceive('BMS: Cell Overvoltage Protection:' + str(self.processEmitter.basicMsg[1]['covp_err']))
        elif self.processEmitter.basicMsg[1]['cuvp_err']:
            self.bmsExceptionReceive('BMS: Cell Undervoltage Protection:' + str(self.processEmitter.basicMsg[1]['cuvp_err']))
        elif self.processEmitter.basicMsg[1]['povp_err']:
            self.bmsExceptionReceive('BMS: Pack Overvoltage Protection:' + str(self.processEmitter.basicMsg[1]['povp_err']))
        elif self.processEmitter.basicMsg[1]['puvp_err']:
            self.bmsExceptionReceive('BMS: Pack Undervoltage Protection:' + str(self.processEmitter.basicMsg[1]['puvp_err']))
        elif self.processEmitter.basicMsg[1]['chgot_err']:
            self.bmsExceptionReceive('BMS: Charge Overtemperature Protection:' + str(self.processEmitter.basicMsg[1]['chgot_err']))
        elif self.processEmitter.basicMsg[1]['chgut_err']:
            self.bmsExceptionReceive('BMS: Charge Undertemperature Protection:' + str(self.processEmitter.basicMsg[1]['chgut_err']))
        elif self.processEmitter.basicMsg[1]['dsgot_err']:
            self.bmsExceptionReceive('BMS: Discharge Overtemperature Protection:' + str(self.processEmitter.basicMsg[1]['dsgot_err']))
        elif self.processEmitter.basicMsg[1]['dsgut_err']:
            self.bmsExceptionReceive('BMS: Discharge Undertemperature Protection:' + str(self.processEmitter.basicMsg[1]['dsgut_err']))
        elif self.processEmitter.basicMsg[1]['chgoc_err']:
            self.bmsExceptionReceive('BMS: Charge Overcurrent Protection:' + str(self.processEmitter.basicMsg[1]['chgoc_err']))
        elif self.processEmitter.basicMsg[1]['dsgoc_err']:
            self.bmsExceptionReceive('BMS: Discharge Overcurrent Protection:', str(self.processEmitter.basicMsg[1]['dsgoc_err']))
        elif self.processEmitter.basicMsg[1]['sc_err']:
            self.bmsExceptionReceive('BMS: High SC Protection:' + str(self.processEmitter.basicMsg[1]['sc_err']))
        elif self.processEmitter.basicMsg[1]['afe_err']:
            self.bmsExceptionReceive('BMS: AFE Protection:' + str(self.processEmitter.basicMsg[1]['afe_err']))
        elif self.processEmitter.basicMsg[1]['software_err']:
            self.bmsExceptionReceive('BMS: Software Error!' + str(self.processEmitter.basicMsg[1]['software_err']))
    @QtCore.pyqtSlot()
    def bmsReceiveEeprom(self):
        print('window.receive_eeprom_msg: ', self.processEmitter.eepromMsg)
        try:
            self.bmspopupwindow.bmsEepromUpdate(self.processEmitter.eepromMsg)
        except AttributeError as e:
            print('BMSReceiveEeprom1:', e)
            pass
        try:
            #self.bmscfgeepromcmd.emit(self.bmsemitter.eepromMsg)
            self.bmscfgpopupwindow.bmscfgGuiUpdate(self.processEmitter.eepromMsg)
        except AttributeError as e:
            print('BMSReceiveEeprom2:', e)
            pass
        if self.bmseeprom_initter:  # Now that EEPROM/Basic are read, allow BMS window popup.
            print('MainWindow has received BMS intialization data from subprocess.')
            self.ui.BMSButton.clicked.connect(self.popupBms)
            self.bmseeprom_initter = False
    @QtCore.pyqtSlot(str)
    def bmsExceptionReceive(self, val):
        isfaulted = len(self.floop['Faults'])
        if isfaulted > 0 and isfaulted < 20: # To prevent overrun with repeat errors.
            #self.floop['Faults'] = self.floop['Faults'].append(val)
            self.floop['Faults'].append(val)
        else:
            self.floop['Faults'] = val
    @QtCore.pyqtSlot(int)
    def displaybacklight(self, val):
        self.pwm.ChangeDutyCycle(val)
        self.pwm.ChangeDutyCycle(val)
    @QtCore.pyqtSlot(int)
    def displayinverter(self, bool):
        # Dark Theme. Apply shiteload of stylesheets:
        self.displayinvert_bool = bool
        if self.displayinvert_bool:
            self.ui.centralwidget.setStyleSheet("QWidget#centralwidget{background: solid black}")
            self.ui.SpeedGauge.set_NeedleColor(255, 255, 255, 255)
            self.ui.SpeedGauge.set_ScaleValueColor(255, 255, 255, 255)
            self.ui.SpeedGauge.set_DisplayValueColor(255, 255, 255, 255)
            self.ui.SpeedGauge.black = QtGui.QColor(255, 255, 255, 255)
            self.ui.PowerGauge.set_NeedleColor(255, 255, 255, 255)
            self.ui.PowerGauge.set_ScaleValueColor(255, 255, 255, 255)
            self.ui.PowerGauge.set_DisplayValueColor(255, 255, 255, 255)
            self.ui.PowerGauge.black = QtGui.QColor(255, 255, 255, 255)
            self.ui.SpeedGaugeLabel.setStyleSheet("QLabel{font: 70pt \"Luxi Mono\"; font-weight: bold; color: white}")
            self.ui.SpeedGaugeLabelUnits.setStyleSheet("QLabel{font: 16pt \"Luxi Mono\"; font-weight: bold; color: white}")
            self.ui.PowerGaugeLabel.setStyleSheet("QLabel{font: 48pt \"Luxi Mono\"; font-weight: bold; color: white}")
            self.ui.PowerGaugeLabelUnits.setStyleSheet("QLabel{font: 16pt \"Luxi Mono\"; font-weight: bold; color: white}")
            self.ui.TripBox.setStyleSheet("QGroupBox{background: solid black; border: 5px solid gray;\n"
            "    border-radius: 10px; margin-top: 50px;}\n"
            "QGroupBox::title {subcontrol-origin: margin; subcontrol-position: top left; left: 25px;\n"
            "    padding: -25 0px 0 0px;}"
            "QLabel{font: 18pt \"Luxi Mono\"; font-weight: bold; color: white}\n"
            "QCheckBox::indicator {width: 60px; height: 60px;}"
            "QPushButton{background: black; font: 48pt \"Luxi Mono\"; font-weight: bold; color: white;\n"
            "border-style: inset; border-color: light grey; border-width: 4px; border-radius 20px;}\n"
            "QPushButton::pressed{border-style: outset}")
            self.ui.BatteryVoltageBar.setStyleSheet("QProgressBar::chunk {background-color: black;}\n"
            "QProgressBar {border-style: solid; border-color: gray; background-color: gray; border-width: 3px; border-radius: 6px}")
            self.ui.BatteryVoltageLabel.setStyleSheet("QLabel{font: 25pt \"Luxi Mono\";font-weight: bold;\n"
            "color: white}")
            self.ui.BatteryVoltageDropLabel.setStyleSheet("QLabel{font: 16pt \"Luxi Mono\";font-weight: bold;\n"
            "color: white}")
            self.ui.BatteryVoltageLine.setStyleSheet("QObject{color:white}")
            self.ui.BatterySOCBar.setStyleSheet("QProgressBar::chunk {background-color: black;}\n"
            "QProgressBar {border-style: solid; border-color: gray; background-color: gray; border-width: 3px; border-radius: 6px}")
            self.ui.BatterySOCLabel.setStyleSheet("QLabel{font: 25pt \"Luxi Mono\";font-weight: bold;\n"
            "color: white}")
            self.ui.MotorTemperatureLine.setStyleSheet("QObject{color:white}")
            self.ui.MotorTemperatureLine_2.setStyleSheet("QObject{color:white}")
            self.ui.MotorTemperatureBar.setStyleSheet("QProgressBar::chunk {margin-top: 3px; margin-bottom: 3px; background-color: white;}\n"
            "QProgressBar {border-style: solid; border-color: black; background-color: gray; border-width: 3px; border-radius: 6px}")
            self.ui.BatteryTemperatureBar.setStyleSheet(" QProgressBar::chunk {\n"
                                                     "     background-color: black;}\n"
                                                     "QProgressBar {\n"
                                                     "     background-color: gray;\n"
                                                     "    border-style: solid;\n"
                                                     "    border-color: gray;\n"
                                                     "    border-width: 3px;\n"
                                                     "border-radius: 6px")
            self.ui.MotorTemperatureLabel.setStyleSheet("QLabel{font: 25pt \"Luxi Mono\";font-weight: bold;\n"
            "color: white}")
            self.ui.WhmiBar.setStyleSheet("QProgressBar::chunk {background-color: white;}\n"
            "QProgressBar {border-style: solid; border-color: gray; background-color: gray; border-width: 3px; border-radius: 6px}")
            self.ui.WhmiLabel.setStyleSheet("QLabel{font: 25pt \"Luxi Mono\";font-weight: bold; color: white}")
            self.ui.Time.setStyleSheet("QLabel{font: 36pt \"Luxi Mono\";font-weight: bold; color: white}")
            self.ui.AssistSliderLabel.setStyleSheet("QLabel{font: 25pt \"Luxi Mono\";font-weight: bold; color: white}")
            self.ui.AssistSlider.setStyleSheet("QSlider {border-style: none; border-color: gray; border-width: 4px;\n"
            "border-radius: 18px; height: 80px}\n"
            "QSlider::handle:horizontal{background-color: white; border: 5px solid; border-radius: 12px;\n"
            "width: 30px; margin: 0px 0px;}\n"
            "QSlider::groove:horizontal{border: 4px solid gray; border-radius: 18px; height: 28px}")
            self.ui.Profile1Label.setStyleSheet("QLabel{font: 16pt \"Luxi Mono\";font-weight: bold; color: white}")
            self.ui.Profile2Label.setStyleSheet("QLabel{font: 16pt \"Luxi Mono\";font-weight: bold; color: white}")
            self.ui.Profile3Label.setStyleSheet("QLabel{font: 16pt \"Luxi Mono\";font-weight: bold; color: white}")
            self.ui.ProfileRb1.setStyleSheet("QPushButton{border: none; background: transparent;}")
            self.ui.ProfileRb2.setStyleSheet("QPushButton{border: none; background: transparent;}")
            self.ui.ProfileRb3.setStyleSheet("QPushButton{border: none; background: transparent;}")
            self.ui.TripBox.setStyleSheet("QGroupBox{background: solid white; border: 5px solid black; border-radius: 10px; margin-top: 50px;}"
                                        "QGroupBox::title {subcontrol-origin: margin; subcontrol-position: top left; left: 25px;"
                                        "padding: -25 0px 0 0px;}"
                                        "QLabel{font: 18pt \"Luxi Mono\"; font-weight: bold; color: white} " \
                                        "QCheckBox::indicator {width: 60px; height: 60px; } " \
                                        "QSlider::groove:horizontal {border: 1px solid; height: 30px; margin: 0px;}" \
                                        "QSlider::handle:horizontal {background-color: black; border: 5px solid; "
                                        "height: 100px; width: 70px; margin: 0px 0px;}"
                                        "QPushButton { background: white; font: 48pt \"Luxi Mono\"; font-weight: bold;"
                                        "color: black; border-style: inset; border-color: dark grey; border-width: 4px;"
                                        "border-radius:20px;} "
                                        "QPushButton::pressed {border-style:outset;}")
        else: # Light Theme
            self.ui.centralwidget.setStyleSheet("QWidget#centralwidget{background: solid white; }")
            self.ui.SpeedGaugeLabel.setStyleSheet("QLabel{font: 70pt \"Luxi Mono\"; font-weight: bold; color: black}")
            self.ui.SpeedGaugeLabelUnits.setStyleSheet(
                "QLabel{font: 16pt \"Luxi Mono\"; font-weight: bold; color: black}")
            self.ui.PowerGaugeLabel.setStyleSheet("QLabel{font: 48pt \"Luxi Mono\"; font-weight: bold; color: black}")
            self.ui.PowerGaugeLabelUnits.setStyleSheet(
                "QLabel{font: 16pt \"Luxi Mono\"; font-weight: bold; color: black}")
            self.ui.SpeedGauge.set_NeedleColor(50, 50, 50, 255)
            self.ui.SpeedGauge.set_ScaleValueColor(50, 50, 50, 255)
            self.ui.SpeedGauge.set_DisplayValueColor(50, 50, 50, 255)
            self.ui.SpeedGauge.black = QtGui.QColor(0, 0, 0, 255)
            self.ui.PowerGauge.set_NeedleColor(50, 50, 50, 255)
            self.ui.PowerGauge.set_ScaleValueColor(50, 50, 50, 255)
            self.ui.PowerGauge.set_DisplayValueColor(50, 50, 50, 255)
            self.ui.SpeedGauge.black = QtGui.QColor(0, 0, 0, 255)
            self.ui.TripBox.setStyleSheet("QGroupBox{background: solid white; border: 5px solid black;\n"
            "    border-radius: 10px; margin-top: 50px;}\n"
            "QGroupBox::title{subcontrol-origin: margin; subcontrol-position: top left; left: 25px;\n"
            "    padding: -25 0px 0 0px;}"
            "QLabel{font: 18pt \"Luxi Mono\"; font-weight: bold; color: black}\n"
            "QCheckBox::indicator {width: 60px; height: 60px;}"
            "QPushButton{background: transparent; font: 48pt \"Luxi Mono\"; font-weight: bold; color: black;\n"
            "border-style: inset; border-color: dark grey; border-width: 4px; border-radius 20px;}\n"
            "QPushButton::pressed{border-style: outset}")
            self.ui.BatteryVoltageBar.setStyleSheet("QProgressBar::chunk {background-color: black;}\n"
            "QProgressBar {border-style: solid; border-color: gray; border-width: 3px; border-radius: 6px}")
            self.ui.BatteryVoltageLabel.setStyleSheet("QLabel{font: 25pt \"Luxi Mono\";font-weight: bold;\n"
            "color: black}")
            self.ui.BatteryVoltageDropLabel.setStyleSheet("QLabel{font: 16pt \"Luxi Mono\";font-weight: bold;\n"
            "color: black}")
            self.ui.BatteryVoltageLine.setStyleSheet("QObject{color:black}")
            self.ui.BatterySOCBar.setStyleSheet("QProgressBar::chunk {background-color: black;}\n"
            "QProgressBar {border-style: solid; border-color: gray; border-width: 3px; border-radius: 6px}")
            self.ui.BatterySOCLabel.setStyleSheet("QLabel{font: 25pt \"Luxi Mono\";font-weight: bold;\n"
            "color: black}")
            self.ui.MotorTemperatureLine.setStyleSheet("QObject{color:black}")
            self.ui.MotorTemperatureLine_2.setStyleSheet("QObject{color:black}")
            self.ui.MotorTemperatureBar.setStyleSheet("QProgressBar::chunk {background-color: black; margin-top: 3px; margin-bottom: 3px;}\n"
            "QProgressBar {border-style: solid; border-color: gray; border-width: 3px; border-radius: 6px}")
            self.ui.BatteryTemperatureBar.setStyleSheet(" QProgressBar::chunk {\n"
                                                     "     background-color: rgba(0,0,0,150);}\n"
                                                     "QProgressBar {\n"
                                                     "     background-color: rgba(0,0,0,0);\n"
                                                     "    border-style: solid;\n"
                                                     "    border-color: white;\n"
                                                     "    border-width: 3px;\n"
                                                     "border-radius: 6px")
            self.ui.MotorTemperatureLabel.setStyleSheet("QLabel{font: 25pt \"Luxi Mono\";font-weight: bold;\n"
            "color: black}")
            self.ui.MotorTemperatureLine.setStyleSheet("QObject{color:black}")
            self.ui.WhmiBar.setStyleSheet("QProgressBar::chunk {background-color: black;}\n"
            "QProgressBar {border-style: solid; border-color: gray; border-width: 3px; border-radius: 6px}")
            self.ui.WhmiLabel.setStyleSheet("QLabel{font: 25pt \"Luxi Mono\";font-weight: bold; color: black}")
            self.ui.Time.setStyleSheet("QLabel{font: 36pt \"Luxi Mono\";font-weight: bold; color: black}")
            self.ui.AssistSliderLabel.setStyleSheet("QLabel{font: 25pt \"Luxi Mono\";font-weight: bold; color: black}")
            self.ui.AssistSlider.setStyleSheet("QSlider {border-style: none; border-color: gray; border-width: 4px;\n"
            "border-radius: 18px; height: 80px}\n"
            "QSlider::handle:horizontal {background-color: black; border: 5px solid; border-radius: 12px;\n"
            "width: 30px; margin: 0px 0px;}\n"
            "QSlider::groove:horizontal {border: 4px solid gray; border-radius: 18px; height: 28px}")
            self.ui.Profile1Label.setStyleSheet("QLabel{font: 16pt \"Luxi Mono\";font-weight: bold; color: black}")
            self.ui.Profile2Label.setStyleSheet("QLabel{font: 16pt \"Luxi Mono\";font-weight: bold; color: black}")
            self.ui.Profile3Label.setStyleSheet("QLabel{font: 16pt \"Luxi Mono\";font-weight: bold; color: black}")
            self.ui.ProfileRb1.setStyleSheet("QPushButton{border: none; background: transparent;}")
            self.ui.ProfileRb2.setStyleSheet("QPushButton{border: none; background: transparent;}")
            self.ui.ProfileRb3.setStyleSheet("QPushButton{border: none; background: transparent;}")
            self.ui.TripBox.setStyleSheet("QGroupBox{background: solid white; border: 5px solid black; border-radius: 10px; margin-top: 50px;}"
                                        "QGroupBox::title {subcontrol-origin: margin; subcontrol-position: top left; left: 25px;"
                                        "padding: -25 0px 0 0px;}"
                                        "QLabel{font: 18pt \"Luxi Mono\"; font-weight: bold; color: black} " \
                                        "QCheckBox::indicator {width: 60px; height: 60px; } " \
                                        "QSlider::groove:horizontal {border: 1px solid; height: 30px; margin: 0px;}" \
                                        "QSlider::handle:horizontal {background-color: black; border: 5px solid; "
                                        "height: 100px; width: 70px; margin: 0px 0px;}"
                                        "QPushButton { background: white; font: 48pt \"Luxi Mono\"; font-weight: bold;"
                                        "color: black; border-style: inset; border-color: dark grey; border-width: 4px;"
                                        "border-radius:20px;} "
                                        "QPushButton::pressed {border-style:outset;}")
    def tripselect(self, button_bool, command):
        print('Trip Selector ' + str(command) + ' is: ' + str(button_bool))
        if button_bool == True:
            self.trip_selector = command
            #self.trip_selected = True
    #### SQL LOGGING FUNCTIONS ####
    def SQL_init(self):
        # Ensure tables exist, then update lifeID
        self.sql.execute('CREATE TABLE IF NOT EXISTS lifestat (id integer PRIMARY KEY, '
                         'datetime string, ah_used float, ah_charged float, ahregen float, wh float, whregen float, '
                         'bmsah float, bmsahregen float, bmswh float, bmswhregen float, dist float, cycle int)')  # Cycle int is bool for perserving columns.
        self.sql.execute('CREATE TABLE IF NOT EXISTS tripstat (id integer PRIMARY KEY, '
                         'batt_amps float, batt_volts float, motor_amps float, motor_temp float, '
                         'speed float, motor_rpm float, floop_interval float)')
        self.sql.execute('CREATE TABLE IF NOT EXISTS bmsstat (id integer PRIMARY KEY, '
                         'bms_interval float, bms_amps float, bms_volts float)')
        # Not used, could compute again from tripstat
        #                 'interp_interval float, whmi float)')
        self.sql.execute('CREATE TABLE IF NOT EXISTS setup (id integer PRIMARY KEY, '  # Identifier/key
                         'profile integer, assist integer, range_enabled integer, '  # Display/control parameters
                         'ah float, ahregen float, wh float, whregen float, bmsah float, bmsahregen float, '
                         'bmswh float, bmswhregen float, dist float, iter integer, chargestate integer, '
                         'triprange integer, throttleassist integer, batta integer, flux integer, displayinvert integer)')  # Trip counters

        lfs = []
        self.sql.execute('select max(id), total(ah_used), total(ah_charged), total(ahregen), total(wh), '
                         'total(whregen), total(dist) from lifestat')
        for i in self.sql:
            lfs.append(i)
        if lfs[0][0] == None:
            lfs[0] = 0  # If new table, else;
        else:
            self.lifestat_iter_ID, self.lifestat_ah_used, self.lifestat_ah_charged, self.lifestat_ahregen, \
            self.lifestat_wh, self.lifestat_whregen, self.lifestat_dist = \
                lfs[0][0], lfs[0][1], lfs[0][2], lfs[0][3], lfs[0][4], lfs[0][5], lfs[0][6]

        stp = []
        self.sql.execute('SELECT * FROM setup')  # Replace into ID = 0 on update
        for i in self.sql:
            stp.append(i)
        if len(stp) > 0:
            self.profile, self.assist_level, self.opt_tripRangeValue, self.flt_ah, self.flt_ahregen, \
            self.flt_wh, self.flt_whregen, self.flt_bmsah, self.flt_bmsahregen, self.flt_bmswh, self.flt_bmswhregen, \
            self.flt_dist, self.iter_attribute_slicer, self.chargestate, self.opt_tripRangeValue, self.opt_throttleAssistBool,\
            self.opt_battaValue, self.opt_fluxValue, self.displayinvert_bool = \
                stp[0][1], stp[0][2], stp[0][3], stp[0][4], stp[0][5], stp[0][6], stp[0][7], stp[0][8], stp[0][9], \
                stp[0][10], stp[0][11], stp[0][12], stp[0][13], stp[0][14], stp[0][15], stp[0][16], stp[0][17], \
                stp[0][18], stp[0][19]

        # todo: add bms list stats to new table with this format. Update if-not-exists SQL inits above.
        self.sql.execute('select * from tripstat')
        for x in self.sql.fetchall():
            self.list_batt_amps.append(x[1])
            self.list_batt_volts.append(x[2])
            self.list_motor_amps.append(x[3])
            self.list_motor_temp.append(x[4])
            self.list_speed.append(x[5])
            self.list_motor_rpm.append(x[6])
            self.list_floop_interval.append(x[7])

        # Get max ID from tripstats: using iter_attribute_slicer
        # self.sql.execute('select max(id) from tripstat')  # Just use self.iter_attribute_slicer instead?
        # ID = self.sql.fetchone()[0]
        # if ID == None:
        #    self.iter_sql_tripID = 0
        # else:
        #    self.iter_sql_tripID = ID
        # self.iter_sql_tripID = [i[0] for i in self.sql][0]
    def SQL_update_setup(self):
        self.sql.execute('replace into setup values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
         (0, self.profile, self.assist_level, self.opt_tripRangeValue, self.flt_ah, self.flt_ahregen,
          self.flt_wh, self.flt_whregen, self.flt_bmsah, self.flt_bmsahregen, self.flt_bmswh, self.flt_bmswhregen,
          self.flt_dist, self.iter_attribute_slicer, self.chargestate, self.opt_tripRangeValue, self.opt_throttleAssistBool,
          self.opt_battaValue, self.opt_fluxValue, self.displayinvert_bool))
    def SQL_tripstat_upload(self):
        # Committed every iter_threshold (integration) interval in receive_floop.
        payload = (self.iter_attribute_slicer, self.floop['Battery_Current'], self.floop['Battery_Voltage'],
                   self.floop['Motor_Current'], self.floop['Motor_Temperature'], self.floop['Vehicle_Speed'],
                   self.floop['Motor_RPM'], self.list_floop_interval[-1:][0])
        #print('sql_tripstat_upload payload: ', payload)
        self.sql.execute('replace into tripstat values (?,?,?,?,?,?,?,?)', payload)
    def SQL_bmsstat_upload(self):
        payload = (self.iter_bmsmsg, self.list_bms_interval[-1:], self.list_bms_amps[-1:], self.list_bms_volts[-1:])
        self.sql.execute('replace into tripstat values (?,?,?,?)', payload)
    def SQL_lifestat_upload(self):
        # On SOC reset, take Ah and compare to last row to determine if you have charged or discharged.
        # If you have charged, create new row with cycle bool = True to ensure it is preserved and sortable.
        # If you have discharged, and last row was not charged (cycle = True) then it is replaced with updated values.
        # self.sql.execute('SELECT datetime FROM lifestat ORDER BY id DESC LIMIT 1')
        try:  # in case table is new/empty:
            #last_time = self.sql.fetchone()[0]
            current_datetime = datetime.datetime.strftime(datetime.datetime.now(), '%D, %I:%M:%S')
            #dif_time = datetime.datetime.strptime(last_time, '%m/%d/%y, %I:%M:%S') - datetime.datetime.now()
            #delta_time = datetime.timedelta(minutes=5)  # Minimum time between updating lifestat database.
            self.sql.execute('SELECT * FROM lifestat ORDER BY id DESC LIMIT 1')
            lastrow = self.sql.fetchall()[0]
            dif_ah = self.flt_ah - lastrow[3]
            if dif_ah < -0.01:  # If difference between current Ah_used and last is negative (+ noise margin)
                # you have just charged. A new row is created, with total Ah charged as negative float.
                # cycle bool = True, to ensure this row is not replaced in discharged elif condition below.
                self.lifestat_iter_ID += 1
                payload = (self.lifestat_iter_ID, current_datetime, self.flt_ah, dif_ah, self.flt_ahregen,
                       self.flt_wh, self.flt_whregen, self.flt_bmsah, self.flt_bmsahregen,
                       self.flt_bmswh, self.flt_bmswhregen, self.flt_dist, True)
                self.sql.execute('insert into lifestat values (?,?,?,?,?,?,?,?,?,?,?,?,?)', payload)
            elif dif_ah >= -0.01 and lastrow[7] == True:  # If difference is positive, you have discharged.
                # If last row was finalized with charge data, create new row.
                self.lifestat_iter_ID += 1
                payload = (self.lifestat_iter_ID, current_datetime, self.flt_ah, 0, self.flt_ahregen,
                       self.flt_wh, self.flt_whregen, self.flt_bmsah, self.flt_bmsahregen,
                       self.flt_bmswh, self.flt_bmswhregen, self.flt_dist, False)
                self.sql.execute('insert into lifestat values (?,?,?,?,?,?,?,?,?,?,?,?,?)', payload)
            elif dif_ah >= -0.01:
                # If last row was not finalized, update it instead:
                payload = (self.lifestat_iter_ID, current_datetime, self.flt_ah, 0, self.flt_ahregen,
                       self.flt_wh, self.flt_whregen, self.flt_bmsah, self.flt_bmsahregen,
                       self.flt_bmswh, self.flt_bmswhregen, self.flt_dist, False)
                self.sql.execute('replace into lifestat values (?,?,?,?,?,?,?,?,?,?,?,?,?)', payload)

        except (TypeError, IndexError):  # In case of new/empty table, initialize:
            print('SQL Lifestats empty. Initializing...')
            current_datetime = datetime.datetime.strftime(datetime.datetime.now(), '%D, %I:%M:%S')
            payload = (self.lifestat_iter_ID, current_datetime, self.flt_ah, 0, self.flt_ahregen,
                       self.flt_wh, self.flt_whregen, self.flt_bmsah, self.flt_bmsahregen,
                       self.flt_bmswh, self.flt_bmswhregen, self.flt_dist, False)
            self.sql.execute('insert into lifestat values (?,?,?,?,?,?,?,?,?,?,?,?,?)', payload)
    def SQL_lifestat_upload_bms(self):
        try:
            current_datetime = datetime.datetime.strftime(datetime.datetime.now(), '%D, %I:%M:%S')
            self.sql.execute('SELECT * FROM lifestat ORDER BY id DESC LIMIT 1')
            lastrow = self.sql.fetchall()[0]
            charging = lastrow[12]
            dif_ah = self.flt_ah - lastrow[3]
            if not charging and not self.chargestate:  # if not/weren't charging, update only
                payload = (self.lifestat_iter_ID, current_datetime, self.flt_ah, dif_ah, self.flt_ahregen,
                           self.flt_wh, self.flt_whregen, self.flt_bmsah, self.flt_bmsahregen,
                           self.flt_bmswh, self.flt_bmswhregen, self.flt_dist, False)
                self.sql.execute('replace into lifestat values (?,?,?,?,?,?,?,?,?,?,?,?,?)', payload)
            elif not charging and self.chargestate:  # if now/weren't charging, iterate and update
                self.lifestat_iter_ID += 1
                payload = (self.lifestat_iter_ID, current_datetime, self.flt_ah, 0, self.flt_ahregen,
                           self.flt_wh, self.flt_whregen, self.flt_bmsah, self.flt_bmsahregen,
                           self.flt_bmswh, self.flt_bmswhregen, self.flt_dist, True)
                self.sql.execute('insert into lifestat values (?,?,?,?,?,?,?,?,?,?,?,?,?)', payload)
            elif charging and self.chargestate:  # if now/were charging, update only
                payload = (self.lifestat_iter_ID, current_datetime, self.flt_ah, 0, self.flt_ahregen,
                           self.flt_wh, self.flt_whregen, self.flt_bmsah, self.flt_bmsahregen,
                           self.flt_bmswh, self.flt_bmswhregen, self.flt_dist, True)
                self.sql.execute('replace into lifestat values (?,?,?,?,?,?,?,?,?,?,?,?,?)', payload)
        except(TypeError, IndexError):  # In case of new/empty table, initialize:
            print('SQL Lifestats TypeError or IndexError. Is this your first run? Initializing database...')
            current_datetime = datetime.datetime.strftime(datetime.datetime.now(), '%D, %I:%M:%S')
            payload = (self.lifestat_iter_ID, current_datetime, self.flt_ah, 0, self.flt_ahregen,
                       self.flt_wh, self.flt_whregen, self.flt_bmsah, self.flt_bmsahregen,
                       self.flt_bmswh, self.flt_bmswhregen, self.flt_dist, False)
            self.sql.execute('insert into lifestat values (?,?,?,?,?,?,?,?,?,?,?,?,?)', payload)
    #### HELPER FUNCTIONS ####
    def socreset(self):
        if self.iter > 938:
            val = 938
        else:
            val = self.iter
        self.flt_ah = self.battah * (
                    1 - (0.01 * BAC.socmapper(mean(self.list_batt_volts[-val:]))))  # battah * SOC used coefficient
    def ms(self):  # helper function; nanosecond-scale time in milli units, for comparisons
        return time.time_ns() / 1000000000  # Returns time to nanoseconds in units seconds
    def gettime(self):  #
        self.iter_attribute_slicer += 1
        self.iter += 1
        self.iter_sql += 1
        #self.iter_bmsmsg += 1
        self.time2 = self.ms()
        self.list_floop_interval.append(self.time2 - self.time1)
        #print('gettime:', self.time2 - self.time1)
        self.time1 = self.ms()
        # self.lastfloop = self.floop  # Deprecated
    def divzero(self, n, d):  # Helper to convert division by zero to zero
        return n / d if d else 0
    def get_battwh(self):  # For non Li-NMC or typical lithium, derive curve experimentally.
        # Many cell experiments are listed on https://lygte-info.dk/,
        # and can be digitzed with https://automeris.io/WebPlotDigitizer/
        if self.flt_ah > 0:
            return BAC.whmap.interp1d(BAC.wh_a2v_map.interp1d(self.flt_ah / self.battparallel))*self.battseries*self.battparallel
        elif self.flt_ah == 0:
            return BAC.whmap.interp1d(4.2)*self.battseries*self.battparallel
    def strfdelta(self, tdelta, fmt): # Print formatted time from timedelta object, desired format
        d = {"days": tdelta.days}
        d["hours"], rem = divmod(tdelta.seconds, 3600)
        d["minutes"], d["seconds"] = divmod(rem, 60)
        return fmt.format(**d)



if __name__ == '__main__':
    # Logging for debugging Modbus
    #logger = modbus_tk.utils.create_logger("console", level=logging.DEBUG)
    #logging.basicConfig(level='INFO')
    """# Cmdline **kwargs for key vehicle stats  # Final release; my defaults --> required= True
    parser = argparse.ArgumentParser(description='Vehicle Settings')
    parser.add_argument('-battseries', '-bs', action='store', required=True, type=int, dest='bs',
                        help='Number of series battery groups')
    parser.add_argument('-battparallel', '-bp', action='store', required=True, type=int, dest='bp',
                        help='Number of parallel battery cells per group')
    parser.add_argument('-battah', '-bah', '-ba', action='store', required=True, type=int, dest='ba',
                        help='Total amp-hours of battery')
    parser.add_argument('-wheelcircumference', '-wheel', '-whl', '-wheelcircum', action='store', default=1927.225,
                        type=float, dest='whl', required=True,
                        help='Circumference of wheel in mm to convert revolutions to speed, distance, range, etc')
    parser.add_argument('-lockpin', '-lp', '-pin', '-lock', action='store', default=0000,
                        type=int, dest='lockpin', help='PIN code to unlock antitheft.')
    parser.add_argument('-speedparse', '-spd', '-sp', action='store_false', default=True, dest='sp',
                        help='Reduce CPU time considerably by assuming v6.++ parameter addresses in fastloop.')
    parser.add_argument('-controlport', '-cpt', '-bacport', action='store', dest='bacport', required=True,
                        type=str, help='Serial port for controller, e.g. /dev/ttyUSB0, /dev/TTYAMA0, COM4, etc')
    parser.add_argument('-bmsport', '-bpt', action='store', dest='bmsport', type=str,
                        help='Serial port for BMS, e.g. /dev/ttyUSB0, /dev/TTYAMA0, COM4, etc')
    args = parser.parse_args()"""
    #BAC = BACModbus.BACModbus(args.bacport)
    # print('args inside of main:', args.bs, args.bp, args.ba, args.whl, args.sp)
    setup = read_setup(os.path.abspath((os.path.dirname(__file__))) + '/setup.csv') # setup.csv dict
    BAC = BACModbus.BACModbus(setup['cpt'])
    app = QtWidgets.QApplication([])

    # Communication lines:
    window_bms_pipe, bms_process_pipe = Pipe()
    window_bac_pipe, bac_process_pipe = Pipe()
    bmsqueue = Queue()
    bacqueue = Queue()

    #bacThread = BACSerialThread(setup)
    BMSEmitter = BMSProcessEmitter(window_bms_pipe)
    BACEmitter = BACProcessEmitter(window_bac_pipe)
    bacProc = BACSerialProcess(setup, bac_process_pipe, bacqueue, BAC)
    bmsProc = BMSSerialProcess(setup['bpt'], bms_process_pipe, bmsqueue)
    #window = AmpyDisplay(setup['battery'][0], setup['battery'][1], setup['battery'][2], setup['wheel'], True, setup['pin'], bmsqueue, processManager)
    #window = AmpyDisplay(args.bs, args.bp, args.ba, args.whl, args.sp, args.lockpin, queue, bmsThread)
    window = AmpyDisplay(setup, bacqueue, bmsqueue, BMSEmitter)

    # todo: setup cfg to enable GPIO e.g. -makerplaneGPIO
    #  Setup cfg for changing units from mph/kph
    #bacThread.bac_msg.connect(window.floopReceive)
    #bacThread.hack_msg.connect(window.receiveHackBACAccessCode)
    BACEmitter.bac_msg.connect(window.floopReceive)
    BACEmitter.diag_msg.connect(window.diagnosticsReceive)
    BACEmitter.hack_msg.connect(window.receiveHackBACAccessCode)
    # todo: save received access codes to file
    #  replace this signal regular bac_msg = -33
    #bmsProc.bms_basic_msg.connect(window.receive_bms_basic)
    #bmsProc.bms_eeprom_msg.connect(window.receive_bms_eeprom)
    #bmsProc.bms_exception.connect(window.receive_bms_exception)
    BMSEmitter.bms_exception.connect(window.bmsExceptionReceive)
    BMSEmitter.bms_eeprom_msg.connect(window.bmsReceiveEeprom)
    BMSEmitter.bms_basic_msg.connect(window.bmsReceiveBasic)

    #window.workmsg.connect(processManager.workercommandsetter)
    #window.powercmd.connect(processManager.powercommandsetter)
    #window.fluxcmd.connect(processManager.fluxcommandsetter)
    #window.bmsmsg_bac.connect(processManager.bmsupdatesetter)
    #window.hackaccesscmd.connect(processManager.hackaccesscommandsetter)
    #bacThread.start()
    BMSEmitter.start()
    BACEmitter.start()
    bmsProc.start()
    bacProc.start()
    #bmsProc.join()
    exit(app.exec_())
