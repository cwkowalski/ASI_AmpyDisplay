# ASI_AmpyDisplay
This project aims to improve the functionality of the incredibly high-performance field-oriented controllers created by Accelerated Systems. Most EV hotrodders using these controllers have plenty of tinkering abilities but the programming skills required for amateurs to fully utilize the abilities of this controller, which is designed as a base system for commercial development, are nontrivial. Generic displays like Kingmeter don't display or control all relevant information, while more versatile universal displays like Justin Le's CycleAnalyst require an external shunt instead of reading the controllers internal shunt values. This initial version in open Python is intended for use with the piCore branch of Tinycore Linux and will be tested on a Raspberry Pi4, with a large e-ink display and touchscreen overlay. RPi was chosen since it has enough headroom for not only these display functions, but many other potential functions in future revisions e.g. dashcam logger, a lowjack that can enable controller antitheft functions or alarms/horn, possibly a bluetooth BMS interface, etc.

The GUI uses PyQT5, so users will be able to easily edit their own GUI's by arranging the base widget elements of this display using QT Designer to edit the ampy.ui file to fit the desired display, for a custom implementation.

Key display elements:
1. Time of day
2. Battery SOC
3. Peak voltage drop over x seconds
4. Controller fault codes
5. Instantaneous wh/mi
6. Trip average wh/mi
7. Trip total wh or ah
8. Trip distance
9. Estimated range
10. Speed (mph default, analog gauge + text)
11. Power (kW, analog gauge + text)
12. Trip range slider (limit peak power to ensure a minimum range)
13. Profile selector (retune any number of controller variables, between three profiles. For example, to enable/disable field weakening or adjust phase current from a reasonable thermal limit, down to saturation limit, to optimize either efficiency or max power) 
14. Digital assist level selector (If using torque sensor or PAS, allows you to control the digital assist level from the display)
