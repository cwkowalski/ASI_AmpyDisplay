# ASI_AmpyDisplay
This project aims to improve the functionality of the incredibly high-performance field-oriented controllers created by Accelerated Systems. Most EV hotrodders using these controllers have plenty of tinkering abilities but the programming skills required for amateurs to fully utilize the abilities of this controller, which is designed as a base system for commercial development, are nontrivial. Generic displays like Kingmeter don't display or control all relevant information, while more versatile universal displays like Justin Le's phenomenal CycleAnalyst require an external shunt instead of reading this controllers internal shunt values. The current branch in open Python is intended for use with piCore from Tinycore Linux and has been tested on a Raspberry Pi4 successfully. RPi was chosen since it has enough headroom for not only these display functions, but many other potential functions in future revisions. Planned future feature additions include GPS navigation powered by Marble with low-power lowjack logging and periodic IoT updates with push notifications as an alarm, GPIO control of lighting relays, a dashcam logger, and finally route-based trip simulations to predict energy required to reach a destination  and allocate power limits according to elevation/wind/vehicle physics/speed limits and maintain a consistent speed, 

Discussion and suggestions here: https://endless-sphere.com/forums/viewtopic.php?f=2&t=108580

Display example with descriptions (800x480): https://i.imgur.com/HzOMMDx.jpg

1872x1404 example: https://i.imgur.com/vq930iW.png

## Display Elements
1. Time of day
2. Battery SOC -- derived from Simpsons-integrated Ah, and reset with the battery charge button after charging from a cubic fit of a high-resolution voltage:state-of-charge array that can be swapped out for different chemistries. 
4. Controller fault codes -- A warning button appears when fault is detected, replacing the Reverse button by default, that when pressed creates popup listing all controller and BMS fault codes with the option to clear them.
5. Trip statistics -- Various trip statistics are displayed in the Trip pane. By default the three selectable panes display:

  | Trip Pane #1 |Power Statistics| |
  |-------|-------|-------|
  | Instantaneous Wh/mi (50ms default interval) | Average Wh/mi (1min default interval) | Amp-hours used |
  | Watt-hours remaining | Estimated range (With Avg Wh/mi's interval) | Amp-hours remaining |
  | Watt-hours regenerated | Miles traveled | Amp-hours regenerated | 
  
  | Trip Pane #2 |Trip Statistics| |
  |-------|-------|-------|  
  | Estimated range average (1min) | Trip Time | Max battery amps |
  | Estimated range instantaneous (50ms) | Moving Trip Time | Minimum battery voltage |
  | Temperature max (motor) | Average moving speed | Max speed |
  Max battery amps * Min battery voltage = Peak battery power.
  
  | Trip Pane #3 |BMS Statistics| |
  |-------|-------|-------|
  | BMS Temp #1 | BMS Temp #2 | BMS Temp 1-4 Max |
  | BMS Temp #2 | BMS Temp #3 | BMS Current (Accessory discharge is positive, charging is negative) | 
  | Cell Imbalance (max mV difference between groups) | Cell Voltage Avg | Cell Voltage Minimum | 
  
6. Speed gauge (mph default, analog gauge + text)
7. Power gauge (kW, analog gauge + text)
8. Minimum range slider -- Enable and drag to minimum miles of range needed, to enable a PID control loop that will limit maximum battery current when instantaneous Wh/mi exceeds what would be required for minimum range. This limit is recalculated and updated in <20 milliseconds intervals; initial PID parameters are tuned for my own build, an extra display UI is provided with Kp/Ki/Kd sliders for initial tuning on other setups.
9. Profile selector-- Retune any number of controller variables, between three or more profiles. For example, to enable/disable field weakening or adjust phase current from a reasonable thermal limit for max power, down to the stator saturation limit for better efficiency, or yet lower for street-legal power levels. The parameter dictionary to setup profiles is derived from the ASIParameterDictionary.xml 
10. Digital assist level selector -- If using torque sensor or PAS, allows you to control the digital assist level from the display. Power limits can be set for each of 9 levels, regardless of the system/throttle power set in each profile; the smallest of the two determines the torque/PAS limit while the profile limit determines the throttle limit.
11. Antitheft lock -- Tap lock button to enable antitheft and display PIN input dialog to unlock. This requires an additional hardware connection to the 'Pedal-First-Sensor' and either a 3.3v to 5V level shifter or a transistor to supply PFS with 5V when enabled, unless you have the very latest 6.015+ firmware which enables setting pullup resistors for this and Cruise input via MODBUS serial I/O.
12. ACID-compliant SQL logging of all stats. A rolling database of trip statistics used for averages is stored, of the length/duration specified by `self.iter_attribute_slicer_threshold` in main.py MainWindow class. Setting this parameter to a negative value will allow the database to grow indefinitely, logging numerous variables including battery voltage and current, motor current, motor temperature, speed, etc in 16ms intervals. Another 'lifetime statistics' database stores all incremental counters e.g. Wh, Ah, distance that are updated in a row for the current discharge cycle;  when a charge is detected a new row is created. Thus depth of discharge, regen stats, distance, dates, and loads of other information can be reviewed for every discharge cycle while keeping the database <20mb even for tens of thousands of cycles. 
IN DEVELOPMENT:
13. Extended options and diagnostics pane is not fully implemented with extra controller tuning options, and diagnostics for all sensor voltages and input state flags. Currently, only Makerplane backlight and dark/light themes are implemented.
14. JBD BMS support is beta and this addition is not yet married to the SQL database, but a feature to save/restore any number of EEPROM profiles will be added. 
15. Support for hardware profile and assist-level switching using digital switches & GPIO will be added.

## Installation
Vehicle-specific parameters are passed by command-line arguments (e.g. onboot startup script) including; number of cell series groups, parallel cells per group, total Amp-hours capacity, wheel circumference in millimeters, controller serial port address,  optionally BMS serial port address, and optionally a PIN code for the antitheft lock which is '0000' by default; these can be specified as command-line arguments e.g. `main.py -battseries 21 -battparallel 14 -battah 42.0 -wheel 420.69 -bacport /dev/ttyUSB0 -bmsport /dev/ttyAMA1` An additional argument -speedparse/-sp disables certain assumptions to enable legacy support for older V5.xxx version firmware controllers.

On Raspbian you should be able to get all dependencies via apt-get/pip. Then add a script to open main.py on startup e.g. add file containing the line `sudo -H python3 /path/to/project/main.py -bs <cell-series-number> -bp <cell-parallel-groups> -ba <pack amp-hours> -whl <wheel circumference in millimeters> -pin <integer> -bacport <controller-serial-port> -bmsport <BMS-serial-port>` in .X.d directory to run after starting Xorg. The flag args are described in the terminal if you try to run main.py without them. 

However, I reccomend piCore OS for its supreme stability and spent a lot of time compiling a full piCore 12.x ARMv7L extension set to run this app on it, and included a stripped-down bespoke extension set with only the files required by this application. A complete list of dependencies for /mnt/mmcblk0p2/onboot.lst is included in this directory. Any questions about piCore can be answered by searching the forum (http://forum.tinycorelinux.net/index.php/). If you're interested in using piCore and using identical hardware, but the setup is too complex for you, contact me and I can temporarily share a (gigantic) fully configured image. Just flash to sd, edit your vehicle parameters in `.X.d/ampy` startup script, connect to your home wifi then run `filetool.sh -b` to save WPA keys locally for easy future updates via SSH, and you're set.

If you are not running FW 6.016+ on your controller you must replace the ASIParameterDictionary.xml with your own. 6.013 is included. You may also optionally include your own state of charge:voltage map if you are running a chemistry besides Lithium-NCA (https://lygte-info.dk/ and https://automeris.io/WebPlotDigitizer/ can be used to generate profiles for specific cells, but cells within a chemistry should have essentially identical profiles). This map is used because it is far more accurate than the linear approximation used by the controller itself to monitor state-of-charge. 

### Bill of Materials:
All you need is a Raspberry Pi, at least one UART/usb serial output for the controller or two for BMS integration, and a display. If not using an 800x480 display you'll have to tweak the GUI widget proportions to fit your display with the easy-to-use standalone Qt Designer application. And if you use a different pi/display you'll likely need to edit or fabricate your own case. The official Raspberry Pi power supply is sufficient to run a Pi 4B and power the Makerplane display from GPIO pins.
1. Raspberry Pi 4B 8gb (overkill)
2. microSD card (I'm using a Kingston Canvas Go ~170mb/s-- fast cards are desirable for fast boot time. You probably don't need more than 1gb unless you'd like to use dashcam later.)
3. FTDI TTL-232r-5v-WE USB-Serial Adapter for ASI Controller (could use Pi's UART with a level shifter/optoisolators if desired)
4. FTDI TTL-232r-3v3 for BMS (or use Pi's UART's) 
5. UH401-2KV USB Isolator (not strictly necessary)
6. Makerplane 5" 1100-nit IPS 800x480 HDMI, single-point capacitive touch GPIO display
    http://store.makerplane.org/5-sunlight-readable-touchscreen-hdmi-display-for-raspberry-pi/
    To fit in my case model, I used HDMI ribbon cables and plug/jacks from Adafruit:
    https://www.adafruit.com/product/3549
    https://www.adafruit.com/product/3553
    https://www.adafruit.com/product/3560
6. Case: https://www.thingiverse.com/thing:4752509


### Development Notes and Customization Tips
* The GUI refresh is tied directly to the controller serial updates which are a 16ms interval, since it does not make sense to update the GUI without any new information. A few parameters including Watt-hour calculation require at least 3 updates for precise Simpsons-method integration so this results in approximately 21fps by default. This update rate, the SQL update rate, the number of updates used for averages, etc can be changed with the MainWindow class iterator thresholds attributes in main.py (`self.iter_xxx` and `self.mean_length`). For example, if you have a fast Pi4B doing nothing else and don't mind tripling the modest CPU usage to update the speedo and power gauges at ~60fps set MainWindow `self.iter_threshold=1` instead of `=3`.
* Any JBD/JBLTools/xiaoxiang compatible 'smart bms' of which there are many on Alibaba will work with the BMS protocol. Specifically, those using TI BQ76940 controller(s) connected to an Atmel 8 bit microcontroller. Calculations are setup assuming that the BMS is bypassed for main power, since this is more efficient and all BMS cell-level fault limits are replicated by this  accessory power discharging, and connecting to both the controller and BMS, it is possible to discriminate between main discharge/regen, accessory discharge, and recharging simultaneously. This integration is still in progress.
* Couloumb counting is overall an excellent method to estimate SOC although it can be imperfect and suffer long-term drift if it's not occassionaly reset with another reference, e.g. voltage. Great care was taken to use the most accurate methods for these functions, but to avoid drift, the class init of the display in main.py calls 'self.socreset()' on start since presumably the bike has been at rest, may have self-discharged, and this is the best time to get an accurate voltage reading. However, if you're already discharging before the boot completes this will result in a low initial reading. This can be disabled by removing self.socreset() from the recieve_floop function, then requiring occassional resetting of SoC with the battery icon. 
* It is necessary to use 6.013 or later ASI firmware to take advantage of certain features e.g. enabling antitheft, and toggling forward/reverse via display use serial commands to switch the pullups on PFS and Cruise built into the controller. If you have an older HW5.xx controller and can't update the firmware to 6.xx, these functions could be controlled by connecting GPIO pins to the controller through a logic-level shifter or preferably, controlling a transistor to gate the controllers 5V signal to these lines. 
* Users can easily construct or theme the existing .ui file using Qt Designer standalone gui application, and pyuic5 command-line converter (e.g. `pyuic5 ampy.ui -o ampy.py`) to draw from these existing widgets as desired for any type of display. If you add extra icons update the ampy.qrc file via `pyrcc5 ampy.qrc -o ampy_rc.py` If you just want to theme the display read up on Qt stylesheets.
