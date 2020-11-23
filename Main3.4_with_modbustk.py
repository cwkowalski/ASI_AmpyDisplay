from PyQt5 import QtCore, QtWidgets, QtGui
import sys
import os
import time
import BACModbus
from ampy import Ui_MainWindow
#from pymodbus.client.sync import ModbusSerialClient as ModbusClient
#from pymodbus.exceptions import ModbusIOException
import serial
import modbus_tk
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu
from scipy import interpolate as interp
from numpy import trapz, seterr, mean, array, array2string
import logging
import pdb  # pdb.set_trace() to add breakpoint
import psutil
Process = psutil.Process(os.getpid())



# KNOWN ISSUES / TO IMPLEMENT
# Keeps crashing with too many gui updates, failing paint events. Perhaps, need to move the floop slot to
# a separate class/thread and then send processed data to the GUI class.

# Condense class attributes into a single dict;
# one for trip lists, one for instance calcs from floop

# Missing function to store/update trip list data via .csv, reset trip data
# Maybe refactor GUI attributes so all trip_ are avg'd values, others are lists sliced for the avgs?

# Range Update 'Range:' box text with predicted range from trip meter,
# set 'range' slider to perhaps even 4x more that (80wh/mi -> 20wh/mi?) with increment btns, enable/disable btns

# Generate 'lifetime' trip statistics for .csv, e.g. total miles, total ah, total cycles, original vs. current Rbattery.

# Set screen full refresh (solid black to white) during mid-iterator while the device is saving .csv!
# This may avoid write corruption, and will be useful signal that it's writing.

# Would be cool to wire in one of the spare BMS temperature sensors (ask them on alibaba for model?)
# in order to measure battery temperature at its center. Would help judge when max power is too much...
# For now, VDrop Motor Temperature progressbars.
# Idea; >2 progressbars with different time averages to illustrate trend of temp? Maybe resource intensive...

# SOC currently mapped straight to Battery Voltage.
# Instead, setup wh to increment by interpolating N elements of list, and map SOC from Wh.
# Watt-hours still off by ~1.3% when incrementing every floop;
# Time: 599.8939490318298, SOC: 24.638614508283645, Wh: 14.259588060093241, Battvolt: 73.32322134387351, MotAmps: 1.1686784448684748, Dist: 0.0, Itercount: 36685, Faults: ['Motor_Hall_Sensor_Fault']
# Consider using sum(self.create_a_new_floop_interval_list[self.short_iterator:]) and means to avoid
# the rounding errors of floats on very small values.
# Longer check:F


# Time: 4009.671501159668, SOC: 22.3330409497473, Wh: 84.53262326053611, Battvolt: 72.3760017361111, MotAmps: 0.9644607638888889, Dist: 0.0, Itercount: 146411, Faults: ['Motor_Hall_Sensor_Fault']
# Time: 4009.7035009860992, SOC: 22.3330409497473, Wh: 84.53325626491517, Battvolt: 72.37600104166667, MotAmps: 0.9644597222222222, Dist: 0.0, Itercount: 146412, Faults: ['Motor_Hall_Sensor_Fault']
# Time: 4009.735501050949, SOC: 22.235890078533643, Wh: 84.5338492175057, Battvolt: 72.37600069444444, MotAmps: 0.9644597222222222, Dist: 0.0, Itercount: 146413, Faults: ['Motor_Hall_Sensor_Fault']
# Time: 4009.7675008773804, SOC: 22.3330409497473, Wh: 84.53454280749364, Battvolt: 72.37600069444444, MotAmps: 0.9644621527777778, Dist: 0.0, Itercount: 146414, Faults: ['Motor_Hall_Sensor_Fault']
# Time: 4009.7995007038116, SOC: 22.3330409497473, Wh: 84.5352362629337, Battvolt: 72.376, MotAmps: 0.9644597222222222, Dist: 0.0, Itercount: 146415, Faults: ['Motor_Hall_Sensor_Fault']
# Time: 4009.83150100708, SOC: 22.3330409497473, Wh: 84.53587869335125, Battvolt: 72.37599930555555, MotAmps: 0.9644572916666667, Dist: 0.0, Itercount: 146416, Faults: ['Motor_Hall_Sensor_Fault']
# Time: 4009.862512111664, SOC: 22.235890078533643, Wh: 84.53656029999972, Battvolt: 72.37599861111111, MotAmps: 0.9644548611111111, Dist: 0.0, Itercount: 146417, Faults: ['Motor_Hall_Sensor_Fault']
# Time: 4009.894509077072, SOC: 22.3330409497473, Wh: 84.537263575315, Battvolt: 72.37599826388889, MotAmps: 0.96445625, Dist: 0.0, Itercount: 146418, Faults: ['Motor_Hall_Sensor_Fault']
# Time: 4009.926501750946, SOC: 22.3330409497473, Wh: 84.53789643820578, Battvolt: 72.37599756944445, MotAmps: 0.9644538194444444, Dist: 0.0, Itercount: 146419, Faults: ['Motor_Hall_Sensor_Fault']
# Time: 4009.9585020542145, SOC: 22.3330409497473, Wh: 84.53845911714943, Battvolt: 72.375996875, MotAmps: 0.9644503472222222, Dist: 0.0, Itercount: 146420, Faults: ['Motor_Hall_Sensor_Fault']



# Self. vars used only for labels should be updated as formatted string, instead of np_float64's.

# use resource = list[-N:] to slice last N elements of list (~18750 elements for last 5 minutes of data)
BAC = BACModbus.BACModbus()

# trip = BACModbus.trip()  # Class instantiate
# trip.read()  # Class method

# Redirect print to file  # Not recommended
# orig_stdout = sys.stdout
# f = open('out.txt', 'w')
# sys.stdout = f
# sys.stdout = orig_stdout
# f.close()

class AppWindow(QtWidgets.QMainWindow):
    workmsg = QtCore.pyqtSignal(str)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # DISPLAY DATA VARIABLES
        self.lastfloop = {}
        self.floop = {'Faults': [], 'Powerboard_Temperature': 0, 'Vehicle_Speed': 0.0, 'Motor_Temperature': 0, 'Motor_Current': 0, 'Motor_RPM': 0.0, 'Percent_Of_Rated_RPM': 0.0, 'Battery_Voltage': 0, 'Battery_Current': 0}
        self.message = {}
        self.battseries = 21
        self.battwh = 3000
        self.battah = 42
        self.trip_batt_volts = float(0)
        self.batt_max_volts = float(0)
        self.batt_min_volts = float(0)
        self.batt_vdrop = float(0)
        self.batt_volts = []
        self.batt_amps = []
        self.motor_amps = []
        self.motor_temp = []
        # self.motor_temp = float(0)  # self.floop['Motor_Temperature']
        self.trip_motor_amps = float(0)
        self.soc = []
        self.trip_soc = float(0)
        self.trip_range = float(0)
        self.trip_range_limit = float(0)
        self.whmi = []
        self.trip_whmi = float(0)
        self.dist = []
        self.trip_dist = float(0)
        self.trip_wh = float(0)
        self.trip_ah = float(0)
        self.trip_whregen = float(0)
        self.trip_ahregen = float(0)
        self.trip_floop_interval = []
        self.start_time = self.ms()
        self.time1 = self.ms()
        self.time2 = None
        self.floop_interval = None
        self.floop_interval_hours = None

        self.exceptions = 0
        self.iterator_floop = 0
        self.iterator_gui_refresh = 0
        self.trip_selector = 1
        self.gui_dict = {}
        self.mean_length = 90000
        # Set up the GUI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #self.ui.FaultCodes.setFont(QtGui.QFont('Arial', 30))  # No effect?

        self.ui.AssistSlider.valueChanged.connect(self.assiststate)
        self.ui.AssistSlider.setMaximum(9)
        self.ui.ProfileRb1.toggled.connect(lambda: self.profilestate(self.ui.ProfileRb1.isChecked(), 'profile1'))
        self.ui.ProfileRb2.toggled.connect(lambda: self.profilestate(self.ui.ProfileRb2.isChecked(), 'profile2'))
        self.ui.ProfileRb3.toggled.connect(lambda: self.profilestate(self.ui.ProfileRb3.isChecked(), 'profile3'))

        # Define display widgets
        # self.ui.TripDistance.setText('\xB0'+'C')  # DegreeC. 2-byte unicode + escape\ to get special char.
        self.ui.CheckEngineButton.clicked.connect(self.faultpopup)
        self.ui.CheckEngineButton.hide()

        self.ui.SpeedGauge.set_MaxValue(80)
        self.ui.SpeedGauge.set_scala_main_count(8)
        # self.ui.SpeedGauge.set_gauge_color_inner_radius_factor(7000)
        # self.ui.SpeedGauge.set_enable_Needle_Polygon(False)
        # self.ui.SpeedGauge.set_enable_CenterPoint(False)
        self.ui.SpeedGauge.set_enable_value_text(False)
        # self.ui.SpeedGauge.set_enable_barGraph(True)
        self.ui.SpeedGauge.set_total_scale_angle_size(240)
        self.ui.SpeedGauge.set_start_scale_angle(150)

        self.ui.PowerGauge.set_MaxValue(24)
        self.ui.PowerGauge.set_scala_main_count(12)
        # self.ui.PowerGauge.set_gauge_color_inner_radius_factor(1000)
        # self.ui.PowerGauge.set_enable_Needle_Polygon(False)
        # self.ui.PowerGauge.set_enable_CenterPoint(False)
        self.ui.PowerGauge.set_enable_value_text(False)
        self.ui.PowerGauge.set_total_scale_angle_size(240)
        self.ui.PowerGauge.set_start_scale_angle(150)
        self.ui.PowerGauge.scala_subdiv_count = 4

        self.show()

#    def assiststate(self, value):
    @QtCore.pyqtSlot(object)
    def receive_floop(self, message): # You can update the UI from here.
        self.gettime()  # Calculate msg interval, increment iterators
        self.floop = BAC.floop_parse(message)
        self.floop_to_list_attributes()
        if self.iterator_floop == 20:
            self.attribute_slicer()
        print('Time: {}, Memory: {}, SOC: {}, Wh: {}, Battvolt: {}, MotAmps: {}, Dist: {}, Itercount: {}, Faults: {}'.format(
            (self.floop_interval), Process.memory_info()[0], self.trip_soc, self.trip_wh, self.trip_batt_volts, self.trip_motor_amps,
            self.trip_dist, self.iterator_floop, self.floop['Faults']))  # self.time1 - self.start_time for time-since-start
        if self.iterator_gui_refresh == 60:
            self.prepare_gui()
            self.update_gui()
            self.iterator_gui_refresh = 0
        # time.sleep(1)
        # print(BAC.floop_parse(message), '\n', 'time: ', self.trip_floop_interval)
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
        # Functions to add:
        # ObidcAddress['Fault_Clear'] = 508, write nonzero val to clear faults. Tap fault label?

    def ms(self):  # function for nanosecond-scale time in milli units, for comparisons
        return time.time_ns() / 1000000000  # Returns time to nanoseconds in units seconds

    def gettime(self):
        self.iterator_floop += 1
        self.iterator_gui_refresh += 1
        self.time2 = self.ms()
        self.floop_interval = self.time2 - self.time1
        # self.floop_interval_hours = self.floop_interval
        self.trip_floop_interval.append(self.floop_interval)
        self.time1 = self.ms()
        self.lastfloop = self.floop

    def floop_to_list_attributes(self): # Make short function which iterates floop into attribute lists, then calcs other list attributes.
        self.soc.append(BAC.socmapper((self.floop['Battery_Voltage'] / self.battseries)))
        self.batt_volts.append(self.floop['Battery_Voltage'])
        self.motor_amps.append(self.floop['Motor_Current'])
        y_speed = [self.lastfloop['Vehicle_Speed'] * 0.621371192,
                   self.floop['Vehicle_Speed'] * 0.621371192]
        y_power = [self.lastfloop['Battery_Voltage'] * self.lastfloop['Motor_Current'],  # Removed /3600 from current
                   self.floop['Battery_Voltage'] * self.floop['Motor_Current']]  # Switch to battery after testing
        distance = (trapz(y_speed, x=None, dx=self.floop_interval))
        # self.dist.append(distance)
        self.trip_dist += distance
        wattsec = trapz(y_power, x=None, dx=self.floop_interval) # Consider update less often, from averages?
                                                                # Currently ~0.5% accuracy due to float rounding
        if wattsec >= 0:
            self.trip_wh += wattsec / 3600 # 60x60 = Watt-hour
        elif wattsec < 0:
            # self.trip_wh += wattsec / 3600  # This line will reduce used Wh by regen value
            self.trip_whregen += abs(wattsec)
        seterr(invalid='raise')  # Triggers FloatingPointError with near-zero values
        # From hereon, generate means from lists:
        # optionally separate for performance e.g. trip_attributer()?
        try:  # trip_whmi now float, derived from trip_dist and trip_wh as already set
            self.trip_whmi = (self.trip_wh/self.trip_dist)
        except FloatingPointError:
            self.trip_whmi = 0

        if len(self.soc) < self.mean_length:
            self.trip_soc = mean(self.soc)
        else:
            self.trip_soc = mean(self.soc[-self.mean_length])
        self.trip_range = (self.trip_soc * self.battwh) / self.trip_whmi

        if len(self.batt_volts) < self.mean_length:
            self.trip_batt_volts = mean(self.batt_volts)
            self.batt_max_volts = max(self.batt_volts)
            self.batt_min_volts = min(self.batt_volts)
        else:
            self.trip_batt_volts = mean(self.batt_volts[-self.mean_length:])
            self.batt_max_volts = max(self.batt_volts[-self.mean_length:]) # Float obj not iterable batt_volts
            self.batt_min_volts = min(self.batt_volts[-self.mean_length:])
        self.batt_vdrop = '{:.1f}'.format(self.batt_min_volts - self.batt_max_volts)

        if len(self.motor_amps) < self.mean_length:
            self.trip_motor_amps = mean(self.motor_amps)
        else:
            self.trip_motor_amps = mean(self.motor_amps[-self.mean_length:])

    def attribute_slicer(self):
        pass
        #  Slice last -18750 entries (5 min)?
    def prepare_gui(self):  # Prepare gui elements to avoid EOL errors during gui update
        self.gui_dict['Time'] = time.strftime('%I:%M:%S', time.localtime())
        self.gui_dict['MotorTemperatureLabel'] = 'Motor: ' + '{:.0f}'.format(self.floop['Motor_Temperature']) + '\xB0'+'C'
        self.gui_dict['MotorTemperatureBar'] = int(self.floop['Motor_Temperature'])
        self.gui_dict['BatteryVoltageLabel'] = 'V:' + '{:.1f}'.format(self.floop['Battery_Voltage'])
        self.gui_dict['BatteryVoltageBar'] = int(self.floop['Battery_Voltage'])
        self.gui_dict['BatteryVoltageDropLabel'] = 'V<sub>d</sub>:' + self.batt_vdrop
        self.gui_dict['BatterySOCLabel'] = 'SOC: ' + '{:.1f}'.format(self.trip_soc)
        self.gui_dict['BatterySOCBar'] = int(self.trip_soc)
        self.gui_dict['SpeedGaugeLabel'] = '{:.0f}'.format(self.floop['Vehicle_Speed'])
        self.gui_dict['PowerGaugeLabel'] = '{:.2f}'.format((self.floop['Battery_Current']*
                                                            self.floop['Battery_Voltage'])/1000)
        self.gui_dict['SpeedGauge'] = self.floop['Vehicle_Speed']
        self.gui_dict['PowerGauge'] = self.floop['Battery_Current']*self.floop['Battery_Voltage']
        if self.trip_selector == 1:
            self.gui_dict['Trip_1_1'] = 'Wh <sub>use</sub>: ' + '{:.0f}'.format(self.trip_wh)
            self.gui_dict['Trip_1_2'] = 'Wh/mi<sub>Trip</sub>: ' + '{:.1f}'.format(self.trip_whmi)
            self.gui_dict['Trip_1_3'] = 'Ah<sub>use</sub>: ' + '{:.1f}'.format(self.trip_ah)
            self.gui_dict['Trip_2_1'] = 'Wh<sub>rem</sub>: ' + '{:.0f}'.format(self.battwh - self.trip_wh)
            # self.gui_dict['Trip_2_2'] = 'Wh/mi<sub>Inst</sub>: ' + '{:.1f}'.format(self.whmi[-1:])
            self.gui_dict['Trip_2_3'] = 'Ah<sub>rem</sub>: ' + '{:.1f}'.format(self.battah - self.trip_ah)
            self.gui_dict['Trip_3_1'] = 'Wh<sub>regen</sub>: ' + '{:.0f}'.format(self.trip_whregen)
            self.gui_dict['Trip_3_2'] = 'Distance: ' + '{:.0f}'.format(self.trip_dist)
            self.gui_dict['Trip_3_3'] = 'Ah<sub>regen</sub>: ' + '{:.1f}'.format(self.trip_ahregen)
            #self.gui_dict['Trip_4_1'] = 'T<sub>max</sub>: ' + '{:.0f}'.format(max(self.motor_temp))  # Intensive if long
            #self.gui_dict['Trip_4_2'] = 'V<sub>min</sub>: ' + '{:.0f}'.format(min(self.batt_volts))
            #self.gui_dict['Trip_4_3'] = 'A<sub>max</sub>: ' + '{:.0f}'.format(max(self.batt_amps))
            ###### New Trip Pane:
        # Trip_Selector_1...4 sets self.tripselector
        # Trip_col#_row# for trip labels, 3col 4row
        # When preparing GUI, check self.tripselector to determine strings.
        #### Trip 1
        # Watt hours used |Wh/mi_T    | Amp-hours used
        # Wh remaining    |Wh/mi_I    | Amp-hours remaining
        # Regen wh gained | Dist      | Amp-hours regen
        # Tmax            | Vmin      | Amp-max
        #### Trip 2
        # Rbatt           | Cycles    | Lifetime Ah
        # Trip dist       |TotDist    | Lifetime Wh
        # Trip max speed  |avg mov Spd| Moving Time
        # Tmax            | Tavg      | Trip Time (while on, since last reset)
        #### Trip 3 Diagnostics?
        # This would require changing floop worker to run extra reads, and indicate e.g.
        # hall positions, input sensor voltages, Features bits, last detected fault(s), etc
        # Probably requires an extra signal, to set a diagnostic bool.
    def update_gui(self):  # Means are parsed within this fxn to update GUI
                            # Unstable; create prepare_gui for dict to update elements.
        self.ui.Time.setText(self.gui_dict['Time'])
        # self.ui.FaultCodes.setText('Faults: ' + str(self.floop['Faults']))
        if len(self.floop['Faults']) > 0:
            self.ui.CheckEngineButton.show()
        else:
            self.ui.CheckEngineButton.hide()
        self.ui.MotorTemperatureLabel.setText(self.gui_dict['MotorTemperatureLabel'])
        self.ui.MotorTemperatureBar.setValue(self.gui_dict['MotorTemperatureBar'])
        self.ui.BatteryVoltageLabel.setText(self.gui_dict['BatteryVoltageLabel'])
        self.ui.BatteryVoltageBar.setValue(self.gui_dict['BatteryVoltageBar'])
        self.ui.BatteryVoltageDropLabel.setText(self.gui_dict['BatteryVoltageDropLabel'])  # Label written as formatted str.
        self.ui.BatterySOCLabel.setText(self.gui_dict['BatterySOCLabel'])
        #self.ui.MotorTemperatureBar.setValue(self.gui_dict['BatterySOCBar'])
        self.ui.BatterySOCBar.setValue(self.gui_dict['BatterySOCBar'])
        self.ui.SpeedGauge.update_value(self.gui_dict['SpeedGauge'])
        self.ui.SpeedGaugeLabel.setText(self.gui_dict['SpeedGaugeLabel'])
        self.ui.PowerGauge.update_value(self.gui_dict['PowerGauge'])
        self.ui.PowerGaugeLabel.setText(self.gui_dict['PowerGaugeLabel'])

        self.ui.Trip_1_1 = self.gui_dict['Trip_1_1']
        self.ui.Trip_1_2 = self.gui_dict['Trip_1_2']
        self.ui.Trip_1_3 = self.gui_dict['Trip_1_3']
        self.ui.Trip_2_1 = self.gui_dict['Trip_2_1']
        # self.ui.Trip_2_2 = self.gui_dict['Trip_2_2']
        self.ui.Trip_2_3 = self.gui_dict['Trip_2_3']
        self.ui.Trip_3_1 = self.gui_dict['Trip_3_1']
        self.ui.Trip_3_2 = self.gui_dict['Trip_3_2']
        self.ui.Trip_3_3 = self.gui_dict['Trip_3_3']
        #self.ui.Trip_4_1 = self.gui_dict['Trip_4_1']
        #self.ui.Trip_4_2 = self.gui_dict['Trip_4_2']
        #self.ui.Trip_4_3 = self.gui_dict['Trip_4_3']


    def faultpopup(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Controller Fault Detected")
        msg.setText('Faults detected: ' + str(self.floop['Faults']).replace('[', '').replace(']', ''))
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setStandardButtons(QtWidgets.QMessageBox.Reset|QtWidgets.QMessageBox.Ignore)
        msg.buttonClicked.connect(self.faultreset)
        msg.exec_()

    def faultreset(self):
        self.workmsg.emit('faultreset')
        #print('Button: ', i)
        #pdb.set_trace()

    def assiststate(self):
        level = self.ui.AssistSlider.value()
        # print('Assist State is now ', level)
        title = 'Assist: ' + str(level)
        self.ui.AssistBox.setTitle(title)  # Probably best to leave command-related gui updates in their callers,
        # as this way the elements are only updated when needed instead of repeatedly repainted.
        self.workmsg.emit('assist')
        #self.ui.SpeedGauge.update_value(level)  # Test couple assist level to speedo
        #self.ui.SpeedGaugeLabel.setText(str(level))

    def profilestate(self, button_bool, command):
        if button_bool == True:  # only if toggled on, then:
            self.workmsg.emit(command)  # command is string in lambdas

class QThreader(QtCore.QThread):
    msg = QtCore.pyqtSignal(object)
    # cmd = QtCore.pyqtSignal(object)
    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)
        # self.msg.connect(callback)
        self.workercmd = 'floop'
        self.newcmd = False
        self.running = True
        self.client = modbus_rtu.RtuMaster(serial.Serial(port=BAC.port, baudrate=BAC.baudrate, bytesize=BAC.bytesize,
                                            parity=BAC.parity, stopbits=BAC.stopbits))
        self.client.set_timeout(1)
        #self.client.connect()
        # self.client.set_debug(True)
        # self.client.strict = False  # Use MODBUS interchar spacing as timeout... MODBUSIOException err
        # self.client.inter_char_timeout = 3.5 *

    @QtCore.pyqtSlot(str)
    def workercommand(self, command):
        #thread1.running = False
        #time.sleep(0.02)
        self.workercmd = command
        #thread1.running = True
        #thread1.start()

    def run(self):  # Executed via .start() method on instance, NOT .run()! Method name MUST be run. Probably.
        while self.running:
            # print('worker: ', self.workercmd)
            # time.sleep(.2)
            if self.workercmd == 'floop':
                #output = self.client.read_holding_registers(BAC.ObdicAddress['Faults'], count=9, unit=self.unit)
                output = self.reads('Faults', 9)  # Address-specific parser to handle bitflags, scales
                self.msg.emit(output)
            elif self.workercmd == 'profile1':
                self.write_scaled('Maximum_Field_Weakening_Current', 50)
                self.write_scaled('Rated_Motor_Current', 450)
                self.write_scaled('Remote_Maximum_Battery_Current_Limit', 300)
                self.workercmd = 'floop'
            elif self.workercmd == 'profile2':
                self.write_scaled('Maximum_Field_Weakening_Current', 0)  # 40.96 scalar
                self.write_scaled('Rated_Motor_Current', 220)  #
                self.write_scaled('Remote_Maximum_Battery_Current_Limit', 200)
                self.workercmd = 'floop'
            elif self.workercmd == 'profile3':
                self.write_scaled('Maximum_Field_Weakening_Current', 0)
                self.write_scaled('Rated_Motor_Current', 220)
                self.write_scaled('Remote_Maximum_Battery_Current_Limit', 15)
                self.workercmd = 'floop'
            elif self.workercmd == 'assist':
                self.write_scaled('Remote_Assist_Mode', window.ui.AssistSlider.value())
                print('Assist command ran')
                self.workercmd = 'floop'
            elif self.workercmd == 'faultreset':
                self.client.execute(BAC.address, cst.WRITE_MULTIPLE_REGISTERS, 508, output_value=[1])
                self.workercmd = 'floop'

    def read(self, address):
        output = self.client.execute(BAC.address, cst.READ_HOLDING_REGISTERS, BAC.ObdicAddress[address], 1)
        return output[0]

    def reads(self, address, registers):
        return self.client.execute(BAC.address, cst.READ_HOLDING_REGISTERS, BAC.ObdicAddress[address], registers)

    def read_scaled(self, address):
        val = (self.client.execute(BAC.address, cst.READ_HOLDING_REGISTERS, BAC.ObdicAddress[address], 1))
        scalar = BAC.ObdicScale[BAC.ObdicAddress[address]]
        output = tuple([x / scalar for x in val])
        return output[0]

    def reads_scaled(self, address, registers):
        val = (self.client.execute(BAC.address, cst.READ_HOLDING_REGISTERS, BAC.ObdicAddress[address], registers))
        scalar = BAC.ObdicScale[BAC.ObdicAddress[address]]
        output = tuple([x / scalar for x in val])
        return output

    def write(self, address, value): # Helper function
        self.client.execute(BAC.address, cst.WRITE_MULTIPLE_REGISTERS, BAC.ObdicAddress[address], output_value=[value])

    def write_scaled(self, address, value): # Helper function
        write = int(value * BAC.ObdicScale[BAC.ObdicAddress[address]])
        self.client.execute(BAC.address, cst.WRITE_MULTIPLE_REGISTERS, BAC.ObdicAddress[address], output_value=[write])


if __name__ == '__main__':
    logger = modbus_tk.utils.create_logger("console")
    logging.basicConfig(level='INFO')

    app = QtWidgets.QApplication([])
    window = AppWindow()
    thread1 = QThreader()

    thread1.msg.connect(window.receive_floop)
    window.workmsg.connect(thread1.workercommand)

    window.show()
    thread1.start()
    sys.exit(app.exec_())