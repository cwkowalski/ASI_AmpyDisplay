import os
import queue
import threading
import time
import tkinter as tk
import tkinter.font as tkFont
import numpy
from scipy import interpolate as interp
import BACModbus
import csv

from ampy import Ui_MainWindow
import ampy_rc
# =========================
# INITIAL SETUP & Global Functions, Variables
# =========================
battseries = 21
battwh = 3000

def ms(): # function for nanosecond-scale time in milli units, for comparisons
    return time.time_ns()/1000000000  # Returns time to nanoseconds in units seconds
thisflooptime = ms()


# Convert trip logging/reading functions to class, and import instead.
# use resource = list[-N:] to slice last N elements of list (~18750 elements for last 5 minutes of data)
#class Log:

def tripreset():
    global trip_dist
    global trip_wh
    global trip_whregen
    trip_dist = trip_wh = trip_whregen = 0
    with open('triplog.csv', mode='w') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow([0, 0, 0])
    file.close()

def tripwrite():
    global trip_dist
    global trip_wh
    global trip_whregen
    with open('triplog.csv', mode='w') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow([trip_dist, trip_wh, trip_whregen])
    file.close()

def tripread():
    global trip_dist
    global trip_wh
    global trip_whregen
    with open('triplog.csv', mode='r') as file:
        reader = csv.reader(file, delimiter=',')
        list = next(reader)
        # print(list)
        trip_dist, trip_wh, trip_whregen = [float(list[i]) for i in (0,1,2)]
        # print('dist: ', trip_dist, 'wh: ', trip_wh, 'regen: ', trip_whregen)
    file.close()

BAC = BACModbus.BACModbus()
floopdic = BAC.reads('Faults',9)

socmap_volts = []
socmap_soc = []
reader = csv.reader(open('socmap_ahv.csv', mode='r'))
for row in reader:
    socmap_volts.append(float(row[1]))
    socmap_soc.append(float(row[2]))
x = numpy.array(socmap_volts)
y = numpy.array(socmap_soc)
socmap = interp.interp1d(x, y, kind='cubic')

tripread()
if trip_wh == None or trip_whregen == None or trip_dist == None:
    trip_wh = trip_whregen = trip_dist = float(0)

#ah = 0
#distance = 0

#c = csv.writer(csvOpen, dialect='excel')
#c.writerows([['TripWh', 'TripAh', 'TripDistance'],[wh,ah,distance]])

class GuiPart:
    def __init__(self, master, queue, endCommand):
        self.queue = queue
        # Set up the GUI
        BigFont = tkFont.Font(family='Arial Bold', size='32', weight='bold')
        FrameFont = tkFont.Font(family='Helvetica', size='16')

        # Read fastloop/core variables to labelframe # Update with list and use for loops to generate... DRY!!!
        DisplayFrame = tk.LabelFrame(root, text="Fastloop Variables", font=FrameFont, padx=5, pady=5, relief='ridge',
                                     borderwidth=6, bg='white')
        # Text label display list: Each element generates a prefix and suffix label ID, and requires a specific suffix unit
        # Text labels are updated by writing to TextLabel+Var e.g. VehicleSpeedVar and updating element in Tkinter
        TextLabel = ['VehicleSpeed', 'MotorTemp', 'MotorCurrent', 'BatteryVoltage', 'BatteryCurrent', 'BatterySOC']
        TextLabelVars = [label + 'Var' for label in TextLabel]
        for label in TextLabelVars:  # Everyone says not to do this and use a dict instead. BUT I DO WHAT I WANT!
            vars()[label] = tk.IntVar()  # This function generates global Tkinter intvars from TextLabelVars strings
        TextLabelPrefix = [label + 'Prefix' for label in TextLabel]
        TextLabelPrefixTxt = [label + ':' for label in TextLabel]
        TextLabelSuffix = [label + 'Suffix' for label in TextLabel]
        TextLabelSuffixTxt = ['MPH', u'\N{DEGREE SIGN}C', 'A', 'V', 'A', '%']
        # Other Tkinter variables
        ProfileSelectVar = tk.IntVar(0)
        AssistSelectVar = tk.IntVar(0)

        # Generate Tkinter text label prefixes
        for col in range(len(TextLabelPrefix)):
            # noinspection PyTypeChecker
            TextLabelPrefix[col] = tk.Label(root, text=TextLabelPrefixTxt[col], font=BigFont,
                                            padx=5, pady=5, bg='white')
            TextLabelPrefix[col].grid(column=0, row=col, sticky=tk.E)
        # Generate Tkinter text labels
        for col in range(len(TextLabel)):
            TextLabel[col] = tk.Label(root, textvariable=TextLabelVars[col], font=BigFont,
                                      padx=5, bg='white', width=4, anchor='e')
            TextLabel[col].grid(column=1, row=col, sticky=tk.E)
        # Generate Tkinter text label suffixes
        for col in range(len(TextLabelSuffix)):
            # noinspection PyTypeChecker
            TextLabelSuffix[col] = tk.Label(root, text=TextLabelSuffixTxt[col], font=BigFont,
                                            padx=5, bg='white', anchor='w')
            TextLabelSuffix[col].grid(column=2, row=col, sticky=tk.W)

        # Profiles widget
        ProfileFrame = tk.LabelFrame(root, text="Global Profiles", font=FrameFont, padx=5, pady=5, relief='ridge',
                                     borderwidth=6, bg='white')
        ProfileFrame.grid()

        # Profile selection buttons (Could iterate these and be DRY)
        button_profile1 = tk.Radiobutton(ProfileFrame, text="1", bg='white', highlightcolor='white',
                                         highlightbackground='black', padx=30, pady=25, font=BigFont,
                                         indicatoron=0, value=1, variable='ProfileSelectVar',
                                         command=lambda: BAC.profile(1))
        button_profile2 = tk.Radiobutton(ProfileFrame, text="2", bg='white', highlightcolor='white',
                                         highlightbackground='black', padx=30, pady=25, font=BigFont,
                                         indicatoron=0, value=2, variable='ProfileSelectVar',
                                         command=lambda: BAC.profile(2))
        button_profile3 = tk.Radiobutton(ProfileFrame, text="3", bg='white', highlightcolor='white',
                                         highlightbackground='black', padx=30, pady=25, font=BigFont,
                                         indicatoron=0, value=3, variable='ProfileSelectVar',
                                         command=lambda: BAC.profile(3))
        button_profile1.pack(side="left")
        button_profile2.pack(side="left")
        button_profile3.pack(side="left")
        # When adding control functionality, create function to set active profile to 'sunken' border and others to 'raised'

        # Digital assist widget
        AssistFrame = tk.LabelFrame(root, text="Assist Profiles", font=FrameFont, padx=5, pady=5, relief='ridge',
                                    borderwidth=6, bg='white')

        # Digital assist scale widget
        AssistScaleY = 55
        AssistScaleX = 200  # Define all scale factors and group together up in #Setup
        AssistScale = tk.Scale(AssistFrame, font=BigFont, orient=tk.HORIZONTAL, from_=0, to=9,
                               length=AssistScaleX, width=AssistScaleY, variable=AssistSelectVar,
                               command=BAC.assist, bg='white', highlightbackground='white')

        # Digital assist increment buttons (Look for image in this folder)
        DownbtnFilepath = os.path.abspath(os.path.join('', 'L.png'))
        Downbtn = tk.PhotoImage(file=DownbtnFilepath)
        UpbtnFilepath = os.path.abspath(os.path.join('', 'R.png'))
        Upbtn = tk.PhotoImage(file=UpbtnFilepath)
        AssistDownbtn = tk.Button(AssistFrame, image=Downbtn, border=0, bg='white',
                                  command=lambda: AssistScale.set(AssistScale.get() - 1))
        AssistUpbtn = tk.Button(AssistFrame, image=Upbtn, border=0, bg='white',
                                command=lambda: AssistScale.set(AssistScale.get() + 1))

        AssistDownbtn.pack(side='left', anchor=tk.S)
        AssistScale.pack(side='left')
        AssistUpbtn.pack(side='left', anchor=tk.S)

        ProfileFrame.grid(column=0, row=0)
        # ProfileFrame.place(relx=0.5, rely=0.5, anchor = tk.CENTER)
        AssistFrame.grid(column=3, row=2)
        DisplayFrame.grid(column=0, row=1, columnspan=2)

    def processIncoming(self):
        """Handle all messages currently in the queue, if any."""
        while self.queue.qsize(  ):
            try:
                floopmsg = self.queue.get(0)
                # Add range function using new socmap()
                global trip_dist
                global trip_wh
                global trip_whregen
                global battseries
                global battwh
                trip_dist = numpy.trapz(floopmsg['y_speed'], x=None, dx=(floopmsg['x_time'])) # Integrate mile/sec by second
                wattsec = (numpy.trapz(floopmsg['y_power'], x=None, dx=floopmsg['x_time']))  # Integrate watts (V*A/s) by second
                if wattsec >= 0:
                    trip_wh += (wattsec / 3600)  # Increment watt-hour global counter
                elif wattsec < 0:
                    trip_whregen += abs(wattsec/3600)
                numpy.seterr(invalid='raise')  # Raises exception in case initial value is invalid-- low float precis.
                try:
                    trip_whmi = trip_wh/trip_dist
                except FloatingPointError:
                    trip_whmi = 0
                soc = socmap((floopmsg['BatteryVoltage']/battseries)) # Exists as NParray; makes range = inf when dividing by zero. Instead of converting to float, perhaps use numpy for whmi?
                range = (soc*battwh) / trip_whmi
                # SOC * max wh = remaining Wh. Wh / wh/mi = mi
                try:
                    whmi_instant = (wattsec)/(3600*(0.621371 * floopdic[260]))  # defines local instantaneous wh/mi
                except FloatingPointError:
                    whmi_instant = 0
                display = {
                    'faults': floopmsg['Faults'],
                    'speed': floopmsg['VehicleSpeed'],
                    'motortemp': floopmsg['MotorTemp'],
                    'motorcurrent': floopmsg['MotorCurrent'],
                    'batteryvoltage': floopmsg['BatteryVoltage'],
                    'batterycurrent': floopmsg['BatteryCurrent'],
                    'batterypower': floopmsg['BatteryPower'],
                    'soc': soc,
                    'range': range,
                    'whmi_instant': whmi_instant,
                    'trip_dist': trip_dist,
                    'trip_wh': trip_wh,
                    'trip_whmi': trip_whmi,
                    'trip_whregen': trip_whregen}
                # Faults, Speed, Motor Temp, Motor Current, Battery Voltage, Battery Current, Battery SOC, Battery Power, soc, range, whmi_instant, & update trip globals trip: dist, wh, whregen
                print(display)
            except queue.Empty:
                # just on general principles, although we don't
                # expect this branch to be taken in this case
                pass

class ThreadedClient:
    """
    Launch the main part of the GUI and the worker thread. periodicCall and
    endApplication could reside in the GUI part, but putting them here
    means that you have all the thread controls in a single place.
    """
    def __init__(self, master):
        """
        Start the GUI and the asynchronous threads. We are in the main
        (original) thread of the application, which will later be used by
        the GUI as well. We spawn a new thread for the worker (I/O).
        """
        self.master = master

        # Create the queue
        self.queue = queue.Queue()

        # Set up the GUI part
        self.gui = GuiPart(root, self.queue, self.endCommand)

        # Set up the thread to do asynchronous I/O
        # More threads can also be created and used, if necessary
        self.running = 1
        self.thread1 = threading.Thread(target=self.workerThread1)
        self.thread1.start()

        # Start the periodic call in the GUI to check if the queue contains
        # anything
        self.periodicCall()

    def periodicCall(self):
        """
        Check every 200 ms if there is something new in the queue.
        """
        self.gui.processIncoming()
        if not self.running:
            pass
        self.master.after(200, self.periodicCall)

    def workerThread1(self): # Transfer all possible processing data into dict, send to processIncoming GUI thread for calculations.
        """
        This is where we handle the asynchronous I/O. For example, it may be
        a 'select(  )'. One important thing to remember is that the thread has
        to yield control pretty regularly, by select or otherwise.
        """
        while self.running:
            global floopdic
            lastfloopdic = floopdic.copy()
            global thisflooptime
            lastflooptime = thisflooptime # Check if this is the same object or actually copied!
            thisflooptime = ms()
            floopdic = BAC.reads('Faults', 9)  # Updates RegsDic with reads
            x = thisflooptime - lastflooptime  # Use last loop read values, last loop time to integrate current
            y_power = [(lastfloopdic[265] * lastfloopdic[266])/3600, (floopdic[265] * floopdic[266])/3600] #Miles per second
            y_speed = [(0.621371192* lastfloopdic[260]), (0.621371192* floopdic[260])]
            floopmsg = {
                'Faults': floopdic[258],
                'VehicleSpeed': 0.621371192 * floopdic[260],
                'MotorTemp': floopdic[261],
                'MotorCurrent': floopdic[262],
                'BatteryVoltage': floopdic[265],
                'BatteryCurrent': floopdic[266],
                'BatteryPower': (floopdic[266]*floopdic[265]),
                'x_time': x,
                'y_power': y_power,
                'y_speed': y_speed}
            # flooptime = "Flooptime: {:.9f}"
            # abstime = "Abstime: {:.9f}"
            # floopmsg = (flooptime.format(ms()), abstime.format(x), 'Wh: ', wh, 'Wh/Mi: ', whmi, 'Dict: ', floopdic)
            # for index, value in enumerate ()
                # Send tkinter variables as dictionary

            #VehicleSpeedVar.set(int(round(0.621371 * RegsDic[260], 0)))  # Km/h to MPH conversion is 0.621371
            #MotorTempVar.set(RegsDic[261])
            #MotorCurrentVar.set(round(RegsDic[262], 1))
            #BatteryVoltageVar.set(round(RegsDic[265], 2))
            #BatteryCurrentVar.set(round(RegsDic[266], 1))
            self.queue.put(floopmsg)
        #Test else statement:
        else:
            print('Floop self.running was false.')
        # Add Else statement here to retry floop when other I/O takes over, and self.running = false... 50ms?
    def endCommand(self):
        self.running = 0

# Create second worker thread for sloop.
# Use this in sloop to open/create and write 1st row headers and 2nd row values for trip statistics.

root = tk.Tk()
client = ThreadedClient(root)
root.mainloop()