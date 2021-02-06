# ASI_AmpyDisplay
This project aims to improve the functionality of the incredibly high-performance field-oriented controllers created by Accelerated Systems. Most EV hotrodders using these controllers have plenty of tinkering abilities but the programming skills required for amateurs to fully utilize the abilities of this controller, which is designed as a base system for commercial development, are nontrivial. Generic displays like Kingmeter don't display or control all relevant information, while more versatile universal displays like Justin Le's phenomenal CycleAnalyst require an external shunt instead of reading this controllers internal shunt values. The current branch in open Python is intended for use with piCore from Tinycore Linux and has been tested on a Raspberry Pi4 successfully. RPi was chosen since it has enough headroom for not only these display functions, but many other potential functions in future revisions. Upcoming features in order of importance are complete JBD bms integration to more intelligently detect charging cycles and set charging thresholds right on the display, GPS navigation powered by Marble with low-power lowjack logging and periodic IoT updates with push notifications as an alarm, control of lighting relays, a dashcam logger, and finally route-based trip simulations to predict energy required to reach a destination  and allocate power limits according to elevation/wind/vehicle physics/speed limits and maintain a consistent speed, 

Discussion and suggestions here: https://endless-sphere.com/forums/viewtopic.php?f=2&t=108580

Display example with descriptions (800x480): https://i.imgur.com/HzOMMDx.jpg
older 1872x1404 example: https://i.imgur.com/vq930iW.png

State-of-charge map if not using Li-NCA or similar Lithium chemistry should be replaced. This map is used because it is far more accurate than the linear approximation performed by the controller itself. https://lygte-info.dk/ and https://automeris.io/WebPlotDigitizer/ can be used to generate profiles for specific cells, but cells within a chemistry should be suitable enough. 

Vehicle-specific parameters needed for calculations include battery series groups, parallel cells per group, total Amp-hours, and wheel circumference in millimeters; these can be specified as command-line arguments e.g. python main.py -battseries 21 -battparallel 14 -battah 42.0 -wheel 1972.0
An additional argument -speedparse/-sp reduces CPU use meaningfully (~9% total) by assuming V6.xxx parameter addresses. In the future this will be amended to use a var cache and get the best of both. If you use a older V5.xxx or newer than 6.015 version firmware you must include the AsiParameterDictionary.xml provided with your copy of ASI's BacDoor application and firmware to ensure the right addresses are called.

Key display elements:
1. Time of day
2. Battery SOC -- derived from Simpsons-integrated Ah, and reset with the battery charge button after charging from a cubic fit of a high-resolution voltage:state-of-charge array that can be swapped out for different chemistries. 
4. Controller fault codes -- Check controller button appears when fault is detected, that creates popup to check and optionally clear fault codes. 
5. Trip statistics -- Various combinations of the following parameters can be displayed in the Trip pane, the 800x480 ui is setup to display 
  Instantaneous Wh/mi
  |Average Wh/mi
  |Wh used
  |Wh remaining
  |Amp-hours used
  |Amp-hours remaining
  |Regenerative braking Wh gained
  |Regenerative braking Ah gained
  |Distance
  |Range remaining
  |Total trip time
  |Moving time
  |Average moving speed
  |Max current
  |Minimum voltage
  |Max motor temperature
  |Battery internal resistance
  |Lifetime battery cycles
  |Lifetime Ah discharged
  |Lifetime Wh discharged
  |Lifetime distance
6. Speed gauge (mph default, analog gauge + text)
7. Power gauge (kW, analog gauge + text)
8. Minimum range slider -- Enable and drag to minimum miles of range needed, to enable a PID control loop that will limit maximum battery current when instantaneous Wh/mi exceeds what would be required for minimum range. This limit is recalculated and updated in <20 milliseconds intervals; initial PID parameters are tuned for my own build, an extra display UI is provided with Kp/Ki/Kd sliders for initial tuning on other setups.
9. Profile selector-- Retune any number of controller variables, between three or more profiles. For example, to enable/disable field weakening or adjust phase current from a reasonable thermal limit for max power, down to the stator saturation limit for better efficiency, or yet lower for street-legal power levels. 
10. Digital assist level selector -- If using torque sensor or PAS, allows you to control the digital assist level from the display. Power limits can be set for each of 9 levels, regardless of the system/throttle power set in each profile; the smallest of the two determines the torque/PAS limit while the profile limit determines the throttle limit.
11. Antitheft lock -- Tap lock button to enable antitheft and display PIN input dialog to unlock. This requires an additional hardware connection to the 'Pedal-First-Sensor' and either a 3.3v to 5V level shifter OR transistor gate to supply PFS with 5V when enabled, unless you have the very latest 6.015+ firmware which enables setting pullup resistors for this and Cruise input via MODBUS serial I/O.
12. ACID-compliant SQL logging of all stats. A rolling database is used for trip statistics that produce incremental counters, and incremental counters are either updated into a row of lifetime statistics for the current discharge cycle, then when a charge is detected a new is created. Thus depth of discharge, regen stats, distance, dates, and other information can be checked for every past discharge cycle while keeping the database very small even for tens of thousands of cycles. 
IN DEVELOPMENT:
13. Extended options and diagnostics pane, to control display backlight, themes, apply further tweaks on selected profile like % power, % field weakening, adjusting the PID parameters for the current trip range limiter, viewing all sensor voltages and input state flags, etc
14. BMS configuration pane, to reprogram any JBD compatible BMS and quickly adjust charge thresholds. This will be a tabbed window first opening to an 'overview' pane automatically opened when charging is detected. If you do not bypass your BMS for charge/discharge you may have to disable this setting as the system will not be able to discriminate between charging and regenerative current. I use my BMS only for powering accessories, cell balancing, and charging-- with integrated measures and controls of the BMS and controller it is recommended to connect your battery directly to the controller through a breaker or contactor.

Bill of Materials:
All you need is a Raspberry Pi, at least one UART/usb serial output for the controller or two for BMS integration, and a display. If not using an 800x480 display you'll have to tweak the GUI widgets to fit your display with the easy-to-use standalone Qt Designer application.
1. Raspberry Pi 4B 8gb (overkill, for future development headroom)
2. Kingston microSD Canvas Go (~170mb/s-- fast card desirable for fast boot time)
3. FTDI TTL-232r-5v-WE USB-Serial Adapter (could likely use Pi UART's with a level shifter instead-- recommend optoisolators in that case)
4. UH401-2KV USB Isolator (not strictly necessary, ensures safe/reliable serial connection)
5. Makerplane 5" 1100-nit IPS 800x480 HDMI, single-point capacitive touch GPIO display
    http://store.makerplane.org/5-sunlight-readable-touchscreen-hdmi-display-for-raspberry-pi/
    To fit in my case model, I used HDMI ribbon cables and plug/jacks from Adafruit:
    https://www.adafruit.com/product/3549
    https://www.adafruit.com/product/3553
    https://www.adafruit.com/product/3560
6. Case: https://www.thingiverse.com/thing:4752509

Installation:
On Raspbian you should be able to get all dependencies via pip or apt-get. Then add a script to open main.py on startup e.g. add file containing the line `sudo -H python3 /path/to/project/main.py -bs <cell-series-number> -bp <cell-parallel-groups> -ba <pack amp-hours> -whl <wheel circumference in millimeters> -sp` in .X.d directory to run after starting Xorg. I reccomend piCore for its supreme stability and have spent a lot of time compiling a full extension set for it-- however, I'm still working on stripping the binaries and trimming all unneeded files from these extensions to optimize boot time, so far from 75 to 25 seconds, once that's perfect I'll post them here but if you're interested in using piCore, contact me and I can share a recent fully configured image. 

Development Notes
* The GUI refresh is tied directly to the serial updates which are a 16ms interval, since it does not make sense to update the GUI without any new information. Since a few parameters including Watt-hour calculation require at least 3 updates for Simpsons-method integration this results in approximately 21fps. This update rate, the SQL update rate, the number of updates used for averages, etc can be changed with the MainWindow iterator thresholds in main.py. For example, if tripling CPU usage is not a problem for your device and you want to update the speedo and power gauges at ~60fps.
* Any JBD/JBLTools/xiaoxiang compatible 'smart bms' of which there are many on Alibaba should work with the BMS protocol. Specifically, those using TI BQ76940 controller(s) connected to an Atmel 8 bit microcontroller. If bypassing BMS for main but not accessory power discharging, and connecting to both the controller and BMS, it is possible to discriminate between main discharge/regen, accessory discharge, and recharging simultaneously. This integration is still in progress.
* Couloumb counting is overall an excellent method to estimate SOC although it can be imperfect and suffer long-term drift if it's not occassionaly reset with another reference. Great care was taken to use the most accurate methods for these functions, but to avoid drift, the class init of the display in main.py calls 'self.socreset()' on start since presumably the bike has been at rest and this is the best time to get an accurate reading. This can be disabled which may then require occassional resetting of SoC with the battery icon in the options window. SoC is mapped from voltage with a high-resolution state of charge array for Samsung 18650-30Q cells, which should be valid for other Li-NMC. Data was extracted from one of innumerable experiments on lygte-info.dk and could be replaced with a profile for your specific manufactured cell if desired.
* It is necessary to use 6.015+ ASI firmware to take advantage of certain features e.g. enabling antitheft, and toggling forward/reverse via display require serial to control the input pullups built into the controller. These could be controlled by connecting GPIO pins to the controller through a logic-level shifter but this is not implemented. 
* Users can easily construct or theme the existing .ui file using Qt Designer standalone gui application, and pyuic5 command-line converter (e.g. >pyuic5 ampy.ui -o ampy.py) to draw from these existing widgets as desired for any type of display. 
