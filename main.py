from PyQt5 import QtCore, QtWidgets, QtGui
from sys import exit
#from os import getpid
import time
import datetime
import BACModbus
from ampy import Ui_MainWindow
import serial
#import modbus_tk
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu
from scipy import integrate, interpolate
#from scipy.stats import linregress
from numpy import mean, isnan, array, prod, argmin, abs
#import logging
# import pdb  # pdb.set_trace() to add breakpoint
import simple_pid as pid
# import psutil # Only needed for debugging/logging memory
import sqlite3
import argparse
from number_pad import numberPopup
from options_dialog import optionsDialog
from ampy_options import Ui_OptDialog

# Process = psutil.Process(getpid()) # To get memory

# todo: consider serial control of walk mode for 'zero RR' riding assist. ~50W?
#  Verify 'Regeneration_battery_current_limit' parameter behavior. Currently controller reports
#  calculated battery current braking limit parameter = system voltage *  Rated motor power (Race mode PAS power)
#  1. Does assist level affect regeneration current?
#  2. Does PAS power actually control regen current with Throttle bypass assist level = 1?
#  3. Does Race mode PAS power actually scale regen current with Alternate speed/power limit disabled?
#  4. 'Rated battery voltage' is supposed to be peak battery voltage...? I prefer average/shallow DoD...
#  Also test the Overload_..._current/time values (Addr 99-104) after ferrofluid mod.
#  Set up progressbar as series of lines with multiple slices of lists… will form arrow scaling to the rate of change.
#  Perhaps design progressbar to shuffle list values down from recent center to distant sides, automatically?
# Throttle bypass assist level: 6.015+ Features3 Bit0 enable, to ignore assist level and use 100% throttle input.
# Human Power Assist Standard: If enabled: https://support.accelerated-systems.com/KB/?p=2175
# Full Pedelec Assistance Speed: Point at which foldback on Max Pedelec Assistance Gain terminates.
# Pedelec gain = 0 when speed = Vehicle_Maximum_Speed (for assistance only, addr 1920)
# re
# PFS/Cruise/Headlight input setting via Modbus, for Antitheft without GPIO!
# HW Configuration Vector: Bit12, PFS Pullup; Bit13, Cruise Pullup, Bit15, Headlight Pullup

# KNOWN ISSUES / TO IMPLEMENT
# In order to accurately integrate distance, will have to use RPM instead of speed. Thus, need to program wheel diam.
# BAC original programmed wheel diameter:367mm?! this was tune with gps!?
# Meaured circumference: 75.875" or 1927.225mm
# Actual diameter: 613.454770401mm
# Consider making a setup.csv for wheel diameter, battwh, battah, etc

# Can fit at least 5, perhaps 6 rows in Trip window with current Magneto profile.

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


# Time: 0.015978574752807617, Memory: 197459968, SOC: 32.14144076550766, Wh: 302.5065789770374, Battvolt: 74.81587986111111, MotAmps: 0.5220652777777778, Dist: 1.0, Itercount: 1457531, Faults: []
# Time: 0.015969038009643555, Memory: 197459968, SOC: 32.23330976354521, Wh: 302.5068175465986, Battvolt: 74.81587986111111, MotAmps: 0.5220701388888889, Dist: 1.0, Itercount: 1457532, Faults: []
# Time: 0.016027450561523438, Memory: 197459968, SOC: 32.14144076550766, Wh: 302.50707255366723, Battvolt: 74.81587951388889, MotAmps: 0.5220729166666667, Dist: 1.0, Itercount: 1457533, Faults: []
# Time: 0.01602458953857422, Memory: 197459968, SOC: 32.14144076550766, Wh: 302.50730670202756, Battvolt: 74.81587951388889, MotAmps: 0.522075, Dist: 1.0, Itercount: 1457534, Faults: []
# Time: 0.016001462936401367, Memory: 197459968, SOC: 32.14144076550766, Wh: 302.5075145335286, Battvolt: 74.81587951388889, MotAmps: 0.5220770833333334, Dist: 1.0, Itercount: 1457535, Faults: []
# Time: 0.015944480895996094, Memory: 197459968, SOC: 32.14144076550766, Wh: 302.507731979501, Battvolt: 74.81587951388889, MotAmps: 0.5220798611111112, Dist: 1.0, Itercount: 1457536, Faults: []
# Time: 0.016041040420532227, Memory: 197459968, SOC: 32.14144076550766, Wh: 302.507987202793, Battvolt: 74.81587951388889, MotAmps: 0.522084375, Dist: 1.0, Itercount: 1457537, Faults: []
# Time: 0.015958309173583984, Memory: 197459968, SOC: 32.14144076550766, Wh: 302.5082411097776, Battvolt: 74.81587951388889, MotAmps: 0.5220885416666666, Dist: 1.0, Itercount: 1457538, Faults: []
# Time: 0.016000986099243164, Memory: 197459968, SOC: 32.23330976354521, Wh: 302.5084956957796, Battvolt: 74.81587951388889, MotAmps: 0.5220930555555555, Dist: 1.0, Itercount: 1457539, Faults: []
# Time: 0.016033172607421875, Memory: 197459968, SOC: 32.14144076550766, Wh: 302.50876641214126, Battvolt: 74.81587916666666, MotAmps: 0.5220944444444444, Dist: 1.0, Itercount: 1457540, Faults: []

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

class AmpyDisplay(QtWidgets.QMainWindow):
    workmsg = QtCore.pyqtSignal(int)
    def __init__(self, bs, bp, ba, whl, sp, lockpin, *args, **kwargs,):
        self.battseries = bs
        self.battparallel = bp
        self.battah = ba
        self.wheelcircum = whl  # In mm
        self.speedparse = sp  # Assume V6 parameter addresses, scales in fastloop for ~17% less total cpu time
        self.lockpin = str(lockpin)
        super().__init__(*args, **kwargs)
        # DISPLAY AND VEHICLE VARIABLES
        # Todo: Initialize floop from sql.

        self.message = {}
        self.profile = 0
        self.assist_level = 0
        self.trip_range_enabled = False  # Check Wh/mi every interval with floop/lastfloop for Range fxn only

        # For floop_to_list
        self.list_batt_amps, self.list_batt_volts, self.list_motor_amps, self.list_motor_temp, self.list_speed, \
        self.list_motor_rpm, self.list_floop_interval, self.list_interp_interval, self.list_whmi = \
            [], [], [], [], [], [], [], [], []

        # For floop_process
        self.flt_batt_volts, self.flt_batt_volts_max, self.flt_batt_volts_min, self.flt_batt_amps_max, \
        self.flt_motor_temp_max, self.flt_batt_amps_max, self.flt_batt_volts_drop, self.flt_motor_amps, \
        self.flt_soc, self.flt_range, self.flt_range_limit, self.flt_whmi_avg, self.flt_whmi_inst, self.flt_dist, \
        self.flt_wh, self.flt_ah, self.flt_whregen, self.flt_ahregen, = \
            float(0), float(0), float(0), float(0), float(0), float(0), float(0), float(0), float(0), \
            float(0), float(0), float(0), float(0), float(0), float(0), float(0), float(0), float(0)

        # For lifestats:
        self.lifestat_iter_ID = 0
        # Todo: update on SQL_init_setup to display lifestats; update lifestats, from trip on socreset.
        self.lifestat_ah_used, self.lifestat_ah_charged, self.lifestat_ahregen, self.lifestat_wh, self.lifestat_whregen, \
        self.lifestat_dist, self.lifestat_Rbatt = \
            float(0), float(0), float(0), float(0), float(0), float(0), float(0)

        # Setup SQL databases and populate lifestats attributes;
        self.sql_conn = sqlite3.connect(r'ampy.db')
        self.sql = self.sql_conn.cursor()
        self.SQL_init()  # Updates ID's to latest in table, creates tables if not exists.
        self.workmsg.emit(self.profile)  # Assist emitted later

        # PID:
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
        # Positive motoring torque ramp = 100ms (6.25 cycles)

        # self.inst_whmi = float(0)          # Generate from interp(v*a, interp_interval) each prepare_gui
        # self.trip_whmi = float(0)          # Generate from wh used, distance each prepare_gui
        # self.dist = []
        # self.trip_dist = float(1)          # Generate from interp(pop(self.dist), self.interp_interval) each prepare_gui
        # self.trip_wh = float(0)            # += from positive interp(pop(batt_volts)*pop(batt_amps), interp_interval)
        # self.trip_ah = float(0)            # += from positive interp(pop(batt_amps), interp_interval
        # self.trip_whregen = float(0)       # First subdivide the volt*amps X interval array into pos/neg segments
        # before interp, to accurately catch regen current (60 cycles = 1 sec
        # self.trip_ahregen = float(0)
        # self.trip_floop_interval = []      # Pop and sum values into self.interp_interval each prepare_gui

        # Iterators and thresholds for averaging, interpolation, etc
        self.mean_length = 18750  # Average for trip_ floats over last 5 minutes (300s / 16ms)
        # trip_wh, trip_ah, trip_soc, trip_range based on cumulative integrals instead
        self.exceptions = 0
        self.first_floop = True
        self.iter = 0
        self.iter_threshold = 19  # Must be odd number for accurate/low-resource Simpsons integration
        self.iter_attribute_slicer = 0
        self.iter_attribute_slicer_threshold = self.mean_length + 500  # 500 = 8 seconds; re-slice for new means each 8 sec.
        self.iter_interp_threshold = int(self.mean_length / self.iter_threshold)  # Equivalent time vs. mean_length
        self.trip_selector = 1
        #self.trip_selected = True
        self.gui_dict = {}
        # Set up the GUI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint))
        self.statusBar().setVisible(False)
        QtWidgets.QApplication.setOverrideCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        #QtWidgets.QApplication.setOverrideCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        # Connect buttons
        self.ui.OptionsBtn.clicked.connect(self.optionspopup)
        self.ui.BatterySOCReset.clicked.connect(self.socreset)
        self.ui.Reverse.toggled.connect(lambda: self.signal_reverse(self.ui.Reverse.isChecked()))
        #self.ui.Reverse.setStyleSheet()
        try:
            self.ui.PID_Kp_Slider.valueChanged.connect(lambda: self.pid_tuner_update(self.ui.PID_Kp_Slider.value(),
                                                                                 self.ui.PID_Ki_Slider.value(),
                                                                                 self.ui.PID_Kd_Slider.value()))
            self.ui.PID_Ki_Slider.valueChanged.connect(lambda: self.pid_tuner_update(self.ui.PID_Kp_Slider.value(),
                                                                                 self.ui.PID_Ki_Slider.value(),
                                                                                 self.ui.PID_Kd_Slider.value()))
            self.ui.PID_Kd_Slider.valueChanged.connect(lambda: self.pid_tuner_update(self.ui.PID_Kp_Slider.value(),
                                                                                 self.ui.PID_Ki_Slider.value(),
                                                                                 self.ui.PID_Kd_Slider.value()))
        except AttributeError:
            pass
        self.ui.LockButton.clicked.connect(lambda: self.signal_antitheft(True))
        #self.ui.RangeBtn.toggled.connect(lambda: self.trip_range_enable(
        #    self.ui.RangeBtn.isChecked(), self.ui.RangeSlider.value()))
        #self.ui.RangeSlider.valueChanged.connect(lambda: self.trip_range_enable(
        #    self.trip_range_enabled, self.ui.RangeSlider.value()))
        self.ui.AssistSlider.valueChanged.connect(self.signal_assist_level)
        self.ui.AssistSlider.setMaximum(9)
        # self.ui.AssistSlider.setTickInterval(1)
        # self.ui.AssistSlider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.ui.ProfileRb1.toggled.connect(lambda: self.signal_profile(self.ui.ProfileRb1.isChecked(), -11))
        ################# Convert profile1 to integers? floop = 0? Faultreset = 10, assist = 11?
        self.ui.ProfileRb2.toggled.connect(lambda: self.signal_profile(self.ui.ProfileRb2.isChecked(), -12))
        self.ui.ProfileRb3.toggled.connect(lambda: self.signal_profile(self.ui.ProfileRb3.isChecked(), -13))
        self.ui.Trip_Selector_1.toggled.connect(lambda: self.tripselect(self.ui.Trip_Selector_1.isChecked(), 1))
        self.ui.Trip_Selector_2.toggled.connect(lambda: self.tripselect(self.ui.Trip_Selector_2.isChecked(), 2))
        # self.ui.Trip_Selector_3.toggled.connect(lambda: self.tripselect(self.ui.Trip_Selector_3.isChecked(), 3))
        # self.ui.Trip_Selector_Debug.toggled.connect(lambda: self.debug(self.ui.Trip_Selector_Debug.isChecked(), 'debug'))
        # Define display widgets
        # self.ui.TripDistance.setText('\xB0'+'C')  # DegreeC. 2-byte unicode + escape\ to get special char.
        self.ui.CheckEngineButton.clicked.connect(self.faultpopup)
        self.ui.CheckEngineButton.hide()

        # Setup analoggaugewidget, with static for the scale and separate needle-only widget, to reduce resources
        # Disable BarGraph Marker: Unchecked
        # Show BarGraph: Checked
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
        self.ui.SpeedGauge.set_enable_value_text(False)
        self.ui.SpeedGauge.set_gauge_color_inner_radius_factor(950)
        self.ui.SpeedGauge.set_scale_polygon_colors([[0.00, QtCore.Qt.red], [0.25, QtCore.Qt.yellow], [1,
                                                     QtCore.Qt.green]])
        self.ui.SpeedGauge.set_enable_filled_Polygon(False)
        self.ui.SpeedGauge.set_enable_barGraph(True)
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
        self.start_time = self.ms()
        self.time1 = self.ms()
        self.time2 = None
        self.show()

    @QtCore.pyqtSlot(object)
    def receive_floop(self, message):  # You can update the UI from here.
        self.gettime()  # Calculate msg interval, increment iterators
        if self.speedparse:
            self.floop = BAC.floop_parse(message)
        else:
            self.floop = BAC.parse(message, 'Faults')
        # attributes for this class from BAC.BACModbus, e.g. the scales/keynames, and bring bitflags function into
        # this class also. TWO THIRDS of recieve_floop time is spent on this one line!!!
        self.floop_to_list()
        self.SQL_tripstat_upload()
        if self.trip_range_enabled:
            self.trip_range_limiter()
        if self.iter_attribute_slicer >= self.iter_attribute_slicer_threshold:  # Every 6 minutes, cut lists to last 5 minutes.
            self.attribute_slicer()
            self.iter_attribute_slicer = 0
        if self.iter >= self.iter_threshold:  # Ideally an odd number to pass even number of *intervals* to Simpsons quadratic integrator
            if self.first_floop:  # Needed so socreset(), SQL has data for first init
                # Also will compensate for any self-discharge, charge since last start.
                self.first_floop = False
                self.floop_process()
                self.socreset()
            else:
                self.floop_process()
                self.SQL_update_setup()
                self.sql_conn.commit()  # Previously in sql_tripstat_upload but moved here for massive speedup
                self.prepare_gui()
                self.update_gui()
                self.iter = 0
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
    def floop_to_list(self):  # iterates floop into instance attribute lists
        self.list_speed.append(self.floop['Vehicle_Speed'] * 0.621371192)  # 0.621371192 is Km -> Mph conversion
        self.list_motor_temp.append(self.floop['Motor_Temperature'])
        self.list_motor_amps.append(self.floop['Motor_Current'])
        self.list_batt_volts.append(self.floop['Battery_Voltage'])
        self.list_batt_amps.append(self.floop['Battery_Current'])
        self.list_motor_rpm.append(self.floop['Motor_RPM'])
    def attribute_slicer(self):
        self.list_speed = self.list_speed[-self.mean_length:]
        self.list_motor_temp = self.list_motor_temp[-self.mean_length:]
        self.list_motor_amps = self.list_motor_amps[-self.mean_length:]
        self.list_batt_volts = self.list_batt_volts[-self.mean_length:]
        self.list_batt_amps = self.list_batt_amps[-self.mean_length:]
        self.list_motor_rpm = self.list_motor_rpm[-self.mean_length:]
        self.list_whmi = self.list_whmi[
                         -self.iter_interp_threshold:]  # From integral; self.mean_length/self.iter threshold = 986.842
    def floop_process(self):
        # Prepare floop list data for Simpsons-method quadratic integration
        self.list_interp_interval.append(sum(self.list_floop_interval[-self.iter:]))  # May not be needed

        x_interval = array([sum(([(self.list_floop_interval[-self.iter:])[:i] for i in range(1, self.iter + 1, 1)])
                                [i]) for i in range(self.iter)])  # calc cumulative time from list of intervals

        y_revsec = array(
            [(self.list_motor_rpm[-self.iter:])[i] / 60 for i in range(self.iter)])  # revolutions per second
        # Integrate distance fromm speed and increment distance counter
        revolutions = integrate.simps(y_revsec, x=x_interval, even='avg')
        if isnan(revolutions):
            distance = 0
        else:
            distance = (revolutions * self.wheelcircum) / (1609344)  ## miles
        self.flt_dist += distance

        array_volts, array_amps = array(self.list_batt_volts[-self.iter:]), array(self.list_batt_amps[-self.iter:])
        y_power = [prod(array_volts[i] * array_amps[i]) for i in range(self.iter)]
        y_current = array(self.list_batt_amps[-self.iter:])

        # Integrate watt-seconds from speed and increment watt-hour counter
        wattsec = integrate.simps(y_power, x=x_interval, even='avg')
        if wattsec >= 0:
            self.flt_wh += wattsec / 3600  # /(60x60) = Watt-hour
        elif wattsec < 0:
            self.flt_wh += wattsec / 3600  # This line will reduce used Wh by regen value
            self.flt_whregen += abs(wattsec)
        # Integrate amp-seconds from speed and increment amp-hour counter
        ampsec = integrate.simps(y_current, x=x_interval, even='avg')
        if ampsec >= 0:
            self.flt_ah += ampsec / 3600
        elif ampsec < 0:
            self.flt_ah += ampsec / 3600
            self.flt_ahregen += abs(wattsec)

        # todo: try to move to prepare_gui, probably only needed for gui refresh EXCEPT for flt_range, whmi_inst
        self.flt_soc = ((self.battah - self.flt_ah) / self.battah) * 100  # Percent SOC from Ah (charge)
        self.list_whmi.append(self.divzero(self.flt_wh, self.flt_dist))
        self.flt_whmi_avg = mean(self.list_whmi[-self.iter_interp_threshold:])  # 18750 / 19 self.iter =
        # self.flt_whmi_inst = self.divzero((wattsec/3600), distance)  # Too erratic esp. at low speed
        self.flt_whmi_inst = mean(self.list_whmi[-3:])  # Approximately 1-sec rolling mean
        self.flt_range = self.divzero((self.get_battwh()), self.flt_whmi_inst)  # Wh for range to account for eff.
        self.flt_batt_volts = mean(self.list_batt_volts)
        self.flt_batt_volts_max = max(self.list_batt_volts)
        self.flt_batt_volts_min = min(self.list_batt_volts)
        self.flt_batt_volts_drop = self.flt_batt_volts_min - self.flt_batt_volts_max
        self.flt_batt_amps_max = max(self.list_batt_amps)
        self.flt_motor_amps = mean(self.list_motor_amps[-self.mean_length:])
        self.flt_motor_temp_max = max(self.list_motor_temp)
    def prepare_gui(self):  # Prepare gui elements to avoid EOL errors during gui update
        # todo: fix label spacing. Consider making prefixes suffixes, and in either case
        #  separate each third of Trip Layout into lined panes. Fill labels with displayed text and place by hand.
        #  Simply not possible to place uniformly in a grid layout.
        self.gui_dict['Time'] = time.strftime('%I:%M:%S', time.localtime())
        self.gui_dict['MotorTemperatureLabel'] = '{:.0f}'.format(
            self.floop['Motor_Temperature']) + '\xB0' + 'C'  # 'T<sub>M</sub>:' +
        self.gui_dict['MotorTemperatureBar'] = int(self.floop['Motor_Temperature'])
        self.gui_dict['BatteryVoltageLabel'] = '{:.1f}'.format(self.floop['Battery_Voltage']) + '<sub>V</sub>'
        self.gui_dict['BatteryVoltageDropLabel'] = '{:.1f}'.format(self.flt_batt_volts_drop)
        self.gui_dict['BatteryVoltageBar'] = int(self.floop['Battery_Voltage'])
        # self.gui_dict['BatteryVoltageDropLabel'] = '| ' + self.batt_vdrop
        self.gui_dict['BatterySOCLabel'] = 'SOC: ' + '{:.1f}'.format(self.flt_soc)
        self.gui_dict['BatterySOCBar'] = int(self.flt_soc)
        self.gui_dict['SpeedGaugeLabel'] = '{:.0f}'.format(self.floop['Vehicle_Speed'])
        self.gui_dict['PowerGaugeLabel'] = '{:.2f}'.format((self.floop['Battery_Current'] *
                                                            self.floop['Battery_Voltage']) / 1000)
        self.gui_dict['SpeedGauge'] = self.floop['Vehicle_Speed']
        self.gui_dict['PowerGauge'] = self.floop['Battery_Current'] * self.floop['Battery_Voltage']

        if self.trip_selector == 1: # populate for first schema:
            self.gui_dict['Trip_1_1'] = '{:.2f}'.format(self.flt_wh)
            self.gui_dict['Trip_1_2'] = '{:.2f}'.format(self.flt_whmi_avg)
            self.gui_dict['Trip_1_3'] = '{:.1f}'.format(self.flt_ah)
            self.gui_dict['Trip_2_1'] = '{:.0f}'.format(self.get_battwh())
            # For remaining wh, consider using socmap_soc *0.03 = ah_rem/cell and simps over volts
            self.gui_dict['Trip_2_2'] = '{:.1f}'.format(self.flt_whmi_inst)
            self.gui_dict['Trip_2_3'] = '{:.1f}'.format(self.battah - self.flt_ah)
            self.gui_dict['Trip_3_1'] = '{:.0f}'.format(self.flt_whregen)
            self.gui_dict['Trip_3_2'] = '{:.0f}'.format(self.flt_dist)
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

            ## New trip 2
            # Range-rem avg   | Trip Time    | Amp-max                # Tmax to MotTempLabel
            # Range-rem inst  | Move-time    | Vmin
            # Tmax            | Avg movspd*  | Spd-max

            # avg movspd*     |Move-time  | Vmin
        ###### New Trip Pane:
        # Trip_Selector_1...4 sets self.tripselector
        # Trip_col#_row# for trip labels, 3col 4row
        # When preparing GUI, check self.tripselector to determine strings.
        #### New trip 1??
        # Watt hours used |Wh/mi_avg  | Amp-hours used
        # Wh remaining    |Wh/mi_Inst | Amp-hours remaining
        # Regen wh gained |dist-travel| Amp-hours regen

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
        #if self.trip_selected:  # Ready for new Trip windows.
        if self.trip_selector == 1:  # Update unit labels for changed trip display.
            self.ui.Trip_1_1_prefix.setText('Wh<sub>use</sub>: ')
            self.ui.Trip_1_2_prefix.setText('Wh/mi<sub>Trip</sub>:')
            self.ui.Trip_1_3_prefix.setText('Ah<sub>use</sub>: ')
            self.ui.Trip_2_1_prefix.setText('Wh<sub>rem</sub>: ')
            self.ui.Trip_2_2_prefix.setText('Wh/mi<sub>Inst</sub>:')
            self.ui.Trip_2_3_prefix.setText('Ah<sub>rem</sub>: ')
            self.ui.Trip_3_1_prefix.setText('Wh<sub>reg</sub>: ')
            self.ui.Trip_3_2_prefix.setText('Miles: ')
            self.ui.Trip_3_3_prefix.setText('Ah<sub>regen</sub>: ')

        ## New trip 2
        # Range-rem avg   | Trip Time    | Amp-max                # Tmax to MotTempLabel
        # Range-rem inst  | Move-time    | Vmin
        # Tmax            | Avg movspd*  | Spd-max
        elif self.trip_selector == 2:
            self.ui.Trip_1_1_prefix.setText('Rng<sub>avg</sub>: ')
            self.ui.Trip_1_2_prefix.setText('T<sub>trip</sub>: ')
            self.ui.Trip_1_3_prefix.setText('A<sub>max</sub>: ')
            self.ui.Trip_2_1_prefix.setText('Rng<sub>inst</sub>: ')
            self.ui.Trip_2_2_prefix.setText('T<sub>mov</sub>:')
            self.ui.Trip_2_3_prefix.setText('V<sub>min</sub>: ')
            self.ui.Trip_3_1_prefix.setText('T<sub>max</sub>: ')
            #self.ui.Trip_3_2_prefix.setText('Miles: ')
            self.ui.Trip_3_2_prefix.setText('Mph<sub>mov</sub>:')
            self.ui.Trip_3_3_prefix.setText('Mph<sub>max</sub>: ')
        elif self.trip_selector == 3:
            pass

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
        #if self.trip_selector == 2:
        #    self.ui.Trip_4_1.setText(self.gui_dict['Trip_4_1'])
        #    self.ui.Trip_4_2.setText(self.gui_dict['Trip_4_2'])
        #    self.ui.Trip_4_3.setText(self.gui_dict['Trip_4_3'])
        #    self.ui.Trip_5_1.setText(self.gui_dict['Trip_5_1'])
        #    self.ui.Trip_5_2.setText(self.gui_dict['Trip_5_2'])
        #    self.ui.Trip_5_3.setText(self.gui_dict['Trip_5_3'])
        # print('Gui updated!')
    def trip_range_enable(self, bool, range):
        # todo: check that slider dynamically updates self.flt_range_limit
        if bool:
            self.trip_range_enabled = bool
            self.flt_range_limit = range
            self.pid.auto_mode = True
            self.trip_range_enabled = True
        elif not bool:
            self.workmsg.emit(-15)  # Code to reset range power limiter
            self.pid_auto_mode = False
            self.trip_range_enabled = False
        # Add var so GUI knows active profile amps. --> self.profile -11 = 1, -12 = 2...
    def trip_range_limiter(self):
        # Check which profile is active. Wh =/= Ah but they are proportional, and no ASI pwr limit exists.
        if self.profile == -11:
            max_amps = 300
        elif self.profile == -12:
            max_amps = 200
        elif self.profile == -13:
            max_amps = 15
        range_div = ((self.get_battwh()) / (self.flt_whmi_inst)) / self.flt_range_limit
        # Instantaneous range / range limit
        # Setpoint is 1, :. range / range limit = 1 is target.
        limit = self.pid.__call__(range_div, self.list_floop_interval[-1:])
        self.workmsg.emit(int(limit * max_amps))
    def pid_tuner_update(self, kp, ki, kd):
        self.pid_kp = kp / 200  # /200 to convert QSlider int to float coefficient
        self.pid_ki = ki / 200
        self.pid_kd = kd / 200
        print('PID tunings: ', self.pid_kp, self.pid_ki, self.pid_kd)
        self.pid.tunings = (kp, ki, kd)
        self.ui.PID_Kp_Label.setText('{:.2f}'.format(self.pid_kp))
        self.ui.PID_Ki_Label.setText('{:.2f}'.format(self.pid_ki))
        self.ui.PID_Kd_Label.setText('{:.2f}'.format(self.pid_kd))
    def faultpopup(self):  # Check Controller indicator.
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Controller Fault Detected")
        msg.setText('Faults detected: ' + str(self.floop['Faults']).replace('[', '').replace(']', ''))
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setStandardButtons(QtWidgets.QMessageBox.Reset | QtWidgets.QMessageBox.Ignore)
        msg.buttonClicked.connect(self.signal_faultreset)
        msg.exec_()
    def signal_faultreset(self):
        self.workmsg.emit('faultreset')
        # print('Button: ', i)
        # pdb.set_trace()
    def signal_assist_level(self):
        level = self.ui.AssistSlider.value()
        # print('Assist State is now ', level)
        # title = 'Assist: ' + str(level)
        self.ui.AssistSliderLabel.setText('Assist: ' + str(level))  # Probably best to leave command-related gui updates in their callers,
        # as this way the elements are only updated when needed instead of repeatedly repainted.
        self.workmsg.emit(-level)  # Positive integers in worker reserved for trip limiter %'s
        # self.ui.SpeedGauge.update_value(level)  # Test couple assist level to speedo
        # self.ui.SpeedGaugeLabel.setText(str(level))
    def signal_profile(self, button_bool, command):
        if button_bool == True:  # only if toggled on, then:
            self.workmsg.emit(command)  # command is integer (-11 = profile1, -12 = profile2...)
        self.profile = command
    def signal_reverse(self, bool):
        if bool:
            self.ui.Reverse.setText('R')
            self.workmsg.emit(-18)
        if not bool:
            self.ui.Reverse.setText('D')
            self.workmsg.emit(-19)
    def signal_antitheft(self, bool):
        if bool:
            # emit signal to enable antitheft
            self.antitheftpopup()
            print('Antitheft signal true, enabling antitheft...')
            self.workmsg.emit(-17)
        if not bool:
            # Emit signal here to disable antitheft
            # Close popup within number_pad.py
            print('Antitheft signal false, disabling antitheft...')
            self.workmsg.emit(-16)
    def antitheftpopup(self):
        self.pinpopup = numberPopup(self.ui, self.lockpin, self.signal_antitheft)
        # self.pinpopup.setParent(self.ui.centralwidget)
        self.pinpopup.setStyleSheet('QPushButton {border-style: inset;border-color: dark grey;'
        'border-width: 3px;border-radius:10px;font: 40pt "Magneto";padding: 0px 0px 0px 0px;} '
                                    'QPushButton::pressed{border-style: outset;}'
                                    'QLineEdit{font: 40pt "Magneto";}')
        # todo: Can't center without hardcoding, need another strategy for universal layout compatibility.
        self.pinpopup.move(self.ui.centralwidget.rect().center() + QtCore.QPoint(self.pinpopup.width()/5, 37))
        self.pinpopup.show()

    def optionspopup(self):
        self.optpopup = optionsDialog(self.ui)
        self.optpopup.show()
    def tripselect(self, button_bool, command):
        print('Trip Selector ' + str(command) + ' is: ' + str(button_bool))
        if button_bool == True:
            self.trip_selector = command
            #self.trip_selected = True
    def socreset(self):
        self.flt_ah = self.battah * (
                    1 - (0.01 * BAC.socmapper(mean(self.list_batt_volts) / 21)))  # battah * SOC used coefficient
        self.SQL_lifestat_upload()
    def ms(self):  # helper function; nanosecond-scale time in milli units, for comparisons
        return time.time_ns() / 1000000000  # Returns time to nanoseconds in units seconds
    def gettime(self):  # Helper function for iterators, time comparison attributes in receive_floop
        self.iter_attribute_slicer += 1
        self.iter += 1
        self.time2 = self.ms()
        self.list_floop_interval.append(self.time2 - self.time1)
        self.time1 = self.ms()
        # self.lastfloop = self.floop  # Deprecated
    def divzero(self, n, d):  # Helper to convert division by zero to zero
        return n / d if d else 0
    def SQL_init(self):
        # Ensure tables exist, then update lifeID
        self.sql.execute('CREATE TABLE IF NOT EXISTS lifestat (id integer PRIMARY KEY, '
                         'datetime string, ah_used float, ah_charged float, ahregen float, wh float, whregen float, '
                         'dist float, cycle int)')  # Cycle int is bool for perserving columns.
        self.sql.execute('CREATE TABLE IF NOT EXISTS tripstat (id integer PRIMARY KEY, '
                         'batt_amps float, batt_volts float, motor_amps float, motor_temp float, '
                         'speed float, motor_rpm float, floop_interval float)')
        # Not used, could compute again from tripstat
        #self.sql.execute('CREATE TABLE IF NOT EXISTS interpstat (id integer PRIMARY KEY, '
        #                 'interp_interval float, whmi float)')
        self.sql.execute('CREATE TABLE IF NOT EXISTS setup (id integer PRIMARY KEY, '  # Identifier/key
                         'profile integer, assist integer, range_enabled integer, '  # Display/control parameters
                         # 'battseries integer, battparallel float, battah float, wheelcircum float, '  # Batt/veh parms
                         'ah float, ahregen float, wh float, whregen float, dist float, iter integer)')  # Trip counters

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
            self.profile, self.assist_level, self.trip_range_enabled, self.flt_ah, self.flt_ahregen, \
            self.flt_wh, self.flt_whregen, self.flt_dist, self.iter_attribute_slicer = \
                stp[0][1], stp[0][2], stp[0][3], stp[0][4], stp[0][5], stp[0][6], stp[0][7], stp[0][8], stp[0][9]

        self.sql.execute('select * from tripstat')
        for x in self.sql.fetchall():
            self.list_batt_amps.append(x[1])
            self.list_batt_volts.append(x[2])
            self.list_motor_amps.append(x[3])
            self.list_motor_temp.append(x[4])
            self.list_speed.append(x[5])
            self.list_motor_rpm.append(x[6])
            self.list_floop_interval.append(x[7])

        # Get max ID from tripstats: Possible deprecate; using iter_attribute_slicer
        # self.sql.execute('select max(id) from tripstat')  # Just use self.iter_attribute_slicer instead?
        # ID = self.sql.fetchone()[0]
        # if ID == None:
        #    self.iter_sql_tripID = 0
        # else:
        #    self.iter_sql_tripID = ID
        # self.iter_sql_tripID = [i[0] for i in self.sql][0]
    def SQL_init_setup_deprecated(self):
        #
        input = []
        self.sql.execute('select max(id), total(ah), total(ahregen), total(wh), '
                         'total(whregen), total(dist) from lifestat')
        for i in self.sql:
            input.append(i)
    def SQL_update_setup(self):
        self.sql.execute('replace into setup values (?,?,?,?,?,?,?,?,?,?)', (0, self.profile, self.assist_level,
            int(self.trip_range_enabled), self.flt_ah, self.flt_ahregen, self.flt_wh, self.flt_whregen,
            self.flt_dist, self.iter_attribute_slicer))
    def SQL_tripstat_upload_deprecated(self):
        # Call this after attribute_slicer to update trip database log.
        payload = []
        for count in range(self.iter_threshold):
            payload.append(((self.iter_attribute_slicer - count), self.list_batt_amps[count],
                            self.list_batt_volts[count], self.list_motor_amps[count],
                            self.list_motor_temp[count], self.list_speed[count], self.list_motor_rpm[count],
                            self.list_floop_interval[count]))
        for i in payload:
            self.sql.execute('replace into tripstat values (?,?,?,?,?,?,?,?)', i)
    def SQL_tripstat_upload(self):
        # Committed every iter_threshold (integration) interval in receive_floop.
        payload = (self.iter_attribute_slicer, self.floop['Battery_Current'], self.floop['Battery_Voltage'],
                   self.floop['Motor_Current'], self.floop['Motor_Temperature'], self.floop['Vehicle_Speed'],
                   self.floop['Motor_RPM'], self.list_floop_interval[-1:][0])
        print('sql_tripstat_upload payload: ', payload)
        self.sql.execute('replace into tripstat values (?,?,?,?,?,?,?,?)', payload)
    def SQL_lifestat_upload(self):
        # On SOC reset, take Ah and compare to last row to determine if you have charged or discharged.
        # If you have charged, create new row with cycle bool = True to ensure it is preserved and sortable.
        # If you have discharged, and last row was not charged (cycle = True) then it is replaced with updated values.

        # todo: Code comments below leftover from deprecated time-comparison-- consider re-implementing as
        #  spamming socreset() can result in dif_ah < 0 from noise if dif_time is low
        #  Figure out why sometimes, this still writes a second row. Seems to be on start.
        #  Possibly the exception case is running when not intended.
        # self.sql.execute('SELECT datetime FROM lifestat ORDER BY id DESC LIMIT 1')
        try:  # in case table is new/empty:
            #last_time = self.sql.fetchone()[0]
            current_datetime = datetime.datetime.strftime(datetime.datetime.now(), '%D, %I:%M:%S')
            #dif_time = datetime.datetime.strptime(last_time, '%m/%d/%y, %I:%M:%S') - datetime.datetime.now()
            #delta_time = datetime.timedelta(minutes=5)  # Minimum time between updating lifestat database.
            self.sql.execute('SELECT * FROM lifestat ORDER BY id DESC LIMIT 1')
            lastrow = self.sql.fetchall()[0]
            dif_ah = self.flt_ah - lastrow[2]
            if dif_ah < -0.01:  # If difference between current Ah_used and last is negative (+ noise margin)
                # you have just charged. A new row is created, with total Ah charged as negative float.
                # cycle bool = True, to ensure this row is not replaced in discharged elif condition below.
                self.lifestat_iter_ID += 1
                payload = (self.lifestat_iter_ID, current_datetime, self.flt_ah, dif_ah, self.flt_ahregen,
                       self.flt_wh, self.flt_whregen, self.flt_dist, True)
                self.sql.execute('insert into lifestat values (?,?,?,?,?,?,?,?,?)', payload)
            elif dif_ah >= -0.01 and lastrow[7] == True:  # If difference is positive, you have discharged.
                # If last row was finalized with charge data, create new row.
                self.lifestat_iter_ID += 1
                payload = (self.lifestat_iter_ID, current_datetime, self.flt_ah, 0, self.flt_ahregen,
                       self.flt_wh, self.flt_whregen, self.flt_dist, False)
                self.sql.execute('insert into lifestat values (?,?,?,?,?,?,?,?,?)', payload)
            elif dif_ah >= -0.01:
                # If last row was not finalized, update it instead:
                payload = (self.lifestat_iter_ID, current_datetime, self.flt_ah, 0, self.flt_ahregen,
                       self.flt_wh, self.flt_whregen, self.flt_dist, False)
                self.sql.execute('replace into lifestat values (?,?,?,?,?,?,?,?,?)', payload)

        except (TypeError, IndexError):  # In case of new/empty table, initialize:
            print('SQL Lifestats empty. Initializing...')
            current_datetime = datetime.datetime.strftime(datetime.datetime.now(), '%D, %I:%M:%S')
            payload = (self.lifestat_iter_ID, current_datetime, self.flt_ah, 0, self.flt_ahregen,
                       self.flt_wh, self.flt_whregen, self.flt_dist, False)
            self.sql.execute('insert into lifestat values (?,?,?,?,?,?,?,?,?)', payload)
    def get_battwh(self):  # For non Li-NMC or typical lithium, derive curve experimentally.
        # Many cell experiments are listed on https://lygte-info.dk/,
        # and can be digitzed with https://automeris.io/WebPlotDigitizer/
        return BAC.whmap(BAC.wh_a2v_map(self.flt_ah / self.battparallel))*self.battseries*self.battparallel
    def strfdelta(self, tdelta, fmt):
        d = {"days": tdelta.days}
        d["hours"], rem = divmod(tdelta.seconds, 3600)
        d["minutes"], d["seconds"] = divmod(rem, 60)
        return fmt.format(**d)


class QThreader(QtCore.QThread):
    msg = QtCore.pyqtSignal(object)

    # cmd = QtCore.pyqtSignal(object)
    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)
        # self.msg.connect(callback)
        self.workercmd = 0
        self.newcmd = False
        self.running = True
        self.client = modbus_rtu.RtuMaster(serial.Serial(port=BAC.port, baudrate=BAC.baudrate, bytesize=BAC.bytesize,
                                                         parity=BAC.parity, stopbits=BAC.stopbits))
        self.client.set_timeout(1)
        # self.client.connect()
        # self.client.set_debug(True)
        # self.client.strict = False  # Use MODBUS interchar spacing as timeout... MODBUSIOException err
        # self.client.inter_char_timeout = 3.5 *

    @QtCore.pyqtSlot(int)
    def workercommand(self, command):
        # thread1.running = False
        # time.sleep(0.02)
        self.workercmd = command
        # thread1.running = True
        # thread1.start()

    def run(self):  # Executed via .start() method on instance, NOT .run()! Method name MUST be run. Probably.
        while self.running:
            # print('worker: ', self.workercmd)
            # time.sleep(.2)
            # Workmsg: 0 = floop, -1 to -9 = assist, -11 to -13 = profile, -14 = faultreset, >0 = Range limiter batt amps
            if self.workercmd == 0:  # If..elif faster than dict comprehension when first element(s) usually taken
                # output = self.client.read_holding_registers(BAC.ObdicAddress['Faults'], count=9, unit=self.unit)
                self.msg.emit(self.reads('Faults', 9))
            elif self.workercmd > 0:
                print('Rangelimiter received val: ', self.workercmd)
                # self.write('Remote_Maximum_Battery_Current_Limit', self.workercmd)  # Enable to limit
                self.msg.emit(self.reads('Faults', 9))
            elif self.workercmd == -11:
                # Possibly scale up Maximum braking torque/Maximum braking current parameters
                # which are a % of rated motor current, for consistent regen braking across profiles.
                # Currently both are 1229 / 40.96 = 30%!
                # 84 amps would be a conservative limit. Target; 100, still ~1/3rd of peak power...
                #
                self.write_scaled('Maximum_Field_Weakening_Current', 50)
                self.write_scaled('Rated_Motor_Current', 450)
                self.write_scaled('Remote_Maximum_Battery_Current_Limit', 300)
                self.write_scaled('Maximum_Braking_Current', (100 / 450))  # Percent of Rated Motor Current
                self.write_scaled('Maximum_Braking_Torque', (100 / 450))  # Percent of Rated Motor Current
                self.workercmd = 0
                print('profile 1 called')
            elif self.workercmd == -12:
                self.write_scaled('Maximum_Field_Weakening_Current', 0)  # 40.96 scalar
                self.write_scaled('Rated_Motor_Current', 220)  #
                self.write_scaled('Remote_Maximum_Battery_Current_Limit', 200)
                self.write_scaled('Maximum_Braking_Current', (100 / 220))  # Percent of Rated Motor Current
                self.write_scaled('Maximum_Braking_Torque', (100 / 220))  # Percent of Rated Motor Current
                self.workercmd = 0
                print('profile 2 called')
            elif self.workercmd == -13:
                self.write_scaled('Maximum_Field_Weakening_Current', 0)
                self.write_scaled('Rated_Motor_Current', 220)
                self.write_scaled('Remote_Maximum_Battery_Current_Limit', 15)
                self.write_scaled('Maximum_Braking_Current', (100 / 220))  # Percent of Rated Motor Current
                self.write_scaled('Maximum_Braking_Torque', (100 / 220))  # Percent of Rated Motor Current
                self.workercmd = 0
                print('profile 3 called')
            elif self.workercmd < 0 and self.workercmd > -10: # -1 to -9 for Assist Levels 1-9
                self.write_scaled('Remote_Assist_Mode', -self.workercmd)  # -(-x) = positive x
                self.workercmd = 0
            elif self.workercmd == -14:  # Clear Fault codes
                self.client.execute(BAC.address, cst.WRITE_MULTIPLE_REGISTERS, 508, output_value=[1])
                self.workercmd = 0
            elif self.workercmd == -15:
                self.write('Remote_Maximum_Battery_Current_Limit', 0)  # Reset range power limiter
                self.workercmd = 0
            elif self.workercmd == -16:  # Antitheft disable
                # intelligent bit-parsing for conditional switching;
                #modbit(n, p, b):  # mod byte at bit p in n to b
                #    mask = 1 << p
                #    return (n & ~mask) | ((b << p) & mask)
                modbyte = (self.read('Features3') & ~(1 << 3)) | ((1 << 3)) & (1 << 3)
                self.write('Features3', modbyte)  # 8 = 4th binary bit
                self.workercmd = 0
            elif self.workercmd == -17:  # Antitheft enable
                modbyte = (self.read('Features3') & ~(1 << 3)) | ((0 << 3)) & (1 << 3)
                self.write('Features3', modbyte)
                self.workercmd = 0
            elif self.workercmd == -18:  # Reverse (cruise input) enable
                modbyte = (self.read('Features3') & ~(1 << 4)) | ((0 << 4)) & (1 << 4)
                self.write('Features3', modbyte)  # 16 = 5th binary bit
                self.workercmd = 0
            elif self.workercmd == -19:  # Reverse (cruise input) disable
                modbyte = (self.read('Features3') & ~(0 << 4)) | ((1 << 4)) & (1 << 4)
                self.write('Features3', modbyte)
                self.workercmd = 0

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

    def write(self, address, value):  # Helper function
        self.client.execute(BAC.address, cst.WRITE_MULTIPLE_REGISTERS, BAC.ObdicAddress[address], output_value=[value])

    def write_scaled(self, address, value):  # Helper function
        write = int(value * BAC.ObdicScale[BAC.ObdicAddress[address]])
        self.client.execute(BAC.address, cst.WRITE_MULTIPLE_REGISTERS, BAC.ObdicAddress[address], output_value=[write])


if __name__ == '__main__':
    # Logging for debugging Modbus
    #logger = modbus_tk.utils.create_logger("console")
    #logging.basicConfig(level='INFO')

    # Cmdline **kwargs for key vehicle stats  # Final release; my defaults --> required= True
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
    parser.add_argument('-speedparse', '-spd', '-sp', action='store_true', default=False, dest='sp',
                        help='Reduce CPU time considerably by assuming v6.++ parameter addresses in fastloop.')
    args = parser.parse_args()
    # print('args inside of main:', args.bs, args.bp, args.ba, args.whl, args.sp)
    app = QtWidgets.QApplication([])
    window = AmpyDisplay(args.bs, args.bp, args.ba, args.whl, args.sp, args.lockpin)
    thread1 = QThreader()

    thread1.msg.connect(window.receive_floop)
    window.workmsg.connect(thread1.workercommand)

    # window.show()
    # window.socreset()  # Was not starting before first floop when put into gui class __init__...
    thread1.start()
    exit(app.exec_())
