# ASI_AmpyDisplay
This project aims to improve the functionality of the incredibly high-performance field-oriented controllers created by Accelerated Systems. Most EV hotrodders using these controllers have plenty of tinkering abilities but the programming skills required for amateurs to fully utilize the abilities of this controller, which is designed as a base system for commercial development, are nontrivial. Generic displays like Kingmeter don't display or control all relevant information, while more versatile universal displays like Justin Le's CycleAnalyst require an external shunt instead of reading the controllers internal shunt values. This initial version in open Python is intended for use with the piCore branch of Tinycore Linux and will be tested on a Raspberry Pi4, with a large e-ink display and touchscreen overlay. RPi was chosen since it has enough headroom for not only these display functions, but many other potential functions in future revisions e.g. dashcam logger, a lowjack that can enable controller antitheft functions or alarms/horn, possibly a bluetooth BMS interface, etc. 

Discussion and suggestions here: https://endless-sphere.com/forums/viewtopic.php?f=2&t=108580

Some features are not fully debugged or implemented, commented in the beginning of Main. Final coming soon.

Key display elements:
1. Time of day
2. Battery SOC -- derived from Simpsons-integrated Ah, and reset with the battery charge button after charging from a cubic fit of a high-resolution voltage:state-of-charge array that can be swapped out for different chemistries. 
4. Controller fault codes -- Check controller button appears when fault is detected, that creates popup to check and optionally clear fault codes. 
5. Trip statistics:
  Instantaneous Wh/mi
  Average Wh/mi
  Wh used
  Wh remaining
  Amp-hours used
  Amp-hours remaining
  Regenerative braking Wh gained
  Regenerative braking Ah gained
  Distance
  Range remaining
  Total trip time
  Moving time
  Average moving speed
  Max current
  Minimum voltage
  Max motor temperature
  Battery internal resistance
  Lifetime battery cycles
  Lifetime Ah discharged
  Lifetime Wh discharged
  Lifetime distance
6. Speed gauge (mph default, analog gauge + text)
7. Power gauge (kW, analog gauge + text)
8. Minimum range slider -- Enable and drag to minimum miles of range needed, to enable a PID control loop that will limit maximum battery current when instantaneous Wh/mi exceeds what would be required for minimum range. This limit is recalculated and updated in <20 milliseconds intervals.
9. Profile selector-- Retune any number of controller variables, between three or more profiles. For example, to enable/disable field weakening or adjust phase current from a reasonable thermal limit for max power, down to the stator saturation limit for better efficiency, or yet lower for street-legal power levels. 
10. Digital assist level selector -- If using torque sensor or PAS, allows you to control the digital assist level from the display. Power limits can be set for each of 9 levels, regardless of the system/throttle power set in each profile; the smallest of the two determines the torque/PAS limit while the profile limit determines the throttle limit.
11. Antitheft lock -- Tap lock button to enable antitheft and display PIN input dialog to unlock. This requires an additional hardware connection to the 'Pedal-First-Sensor' and either a 3.3v to 5V level shifter OR transistor gate to supply PFS with 5V when enabled. 

Users can easily construct or theme the existing .ui file using Qt Designer standalone gui application, and pyuic5 command-line converter (e.g. >pyuic5 ampy.ui -o ampy.py) to draw from these existing widgets as desired for any type of display.

Currently Battery Ah, Wh, number of series groups, state-of-charge map if not using Li-NCA or similar Lithium chemistry, and wheel circumference attributes need to be specified in the beginning __init__ of AppWindow in Main to function properly for various configurations.
