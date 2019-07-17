# 2.2a Sensor Temperature
# by C Lyman
# July 2019
# Activity from Module 2 of Coding & Innovation using Microbits - Python
# Displays current temperature in Celsius

from microbit import *

display.scroll("SENSORS")

# forever loop for Events
while True:
    # button A pressed?
    Apressed = button_a.was_pressed()
    if Apressed:
        display.scroll(temperature())
        sleep(2000)
        display.clear
        