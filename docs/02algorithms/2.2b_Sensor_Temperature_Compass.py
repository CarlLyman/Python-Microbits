# 2.2b Sensor Temperature & Compuss
# by C Lyman
# March 2019
# Activity from Module 2 of Coding & Innovation using Microbits - Python
# When button A pressed - display current temperature in 
# When button B pressed - display compass heading in degrees

from microbit import *

display.scroll("SENSORS")
# The compass needs to be calibrated to work.
# It will ask you to "Tilt until the screen is filled."
# Then it will show a "smiley face" show it worked.
compass.calibrate()

# forever loop for Events
while True:
    # Event - button A pressed?
    if button_a.is_pressed():
        display.scroll(temperature())
        sleep(2000)
        display.clear
    # Event - button B pressed?
    if button_b.is_pressed():
        display.scroll(compass.heading())
        sleep(2000)
        display.clear
