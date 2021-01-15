# ASI_AmpyDisplay
This project aims to improve the functionality of the incredibly high-performance field-oriented controllers created by Accelerated Systems. Most EV hotrodders using these controllers have plenty of tinkering abilities but the programming skills required for amateurs to fully utilize the abilities of this controller, which is designed as a base system for commercial development, are nontrivial. Generic displays like Kingmeter don't display or control all relevant information, while more versatile universal displays like Justin Le's phenomenal CycleAnalyst require an external shunt instead of reading this controllers internal shunt values. This initial version in open Python is intended for use with the piCore branch of Tinycore Linux and will be tested on a Raspberry Pi4. RPi was chosen since it has enough headroom for not only these display functions, but many other potential functions in future revisions. Future features under consideration include a dashcam logger with automatic home backup via WiFi, GPS + IoT/WiFi hotspotting for navigation and highly intelligent destination-based trip simulations to predict energy required throughout a trip and allocate power limits according to elevation/wind/numerous vehicle efficiency parameters, a lowjack that can enable controller antitheft functions and alarms/horn remotely, RFID/NFC based antitheft and alarm switching, and bluetooth BMS interface with any JBDTools compatible BMS for cell-level fault thresholds and warnings as well as displaying individual cell-voltages and adjusting the charge thresholds. 

Discussion and suggestions here: https://endless-sphere.com/forums/viewtopic.php?f=2&t=108580

Display example: https://i.imgur.com/vq930iW.png

Users can easily construct or theme the existing .ui file using Qt Designer standalone gui application, and pyuic5 command-line converter (e.g. >pyuic5 ampy.ui -o ampy.py) to draw from these existing widgets as desired for any type of display.

State-of-charge map if not using Li-NCA or similar Lithium chemistry should be replaced. This map is used because it is far more accurate than the linear approximation performed by the controller itself. https://lygte-info.dk/ and https://automeris.io/WebPlotDigitizer/ can be used to generate profiles for specific cells, but cells within a chemistry should be suitable enough. 

Vehicle-specific parameters needed for calculations include battery series groups, parallel cells per group, total Amp-hours, and wheel circumference in millimeters; these can be specified as command-line arguments e.g. python main.py -battseries 21 -battparallel 14 -battah 42.0 -wheel 1972.0
An additional argument -speedparse/-sp reduces CPU use meaningfully (~9% total) by assuming V6.xxx parameter addresses. If you use a older V5.xxx or newer version you must include the AsiParameterDictionary.xml provided with your copy of ASI's BacDoor application and firmware to get the right addresses.

Key display elements:
1. Time of day
2. Battery SOC -- derived from Simpsons-integrated Ah, and reset with the battery charge button after charging from a cubic fit of a high-resolution voltage:state-of-charge array that can be swapped out for different chemistries. 
4. Controller fault codes -- Check controller button appears when fault is detected, that creates popup to check and optionally clear fault codes. 
5. Trip statistics -- Optionally a trip selector button can be enabled to switch labels between various combinations of the following parameters:
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
