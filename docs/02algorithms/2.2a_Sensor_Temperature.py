# 2.2a Sensor Temperature
# by C Lyman
# March 2019
# Activity from Module 2 of Coding & Innovation using Microbits - Python
# Displays current temperature in Celsius

from microbit import *

display.scroll("SENSORS")

# forever loop for Events
while True:
    # button A pressed?
    if button_a.is_pressed():
        display.scroll(temperature())
        sleep(2000)
        display.clear
        