# 3.2d Sensor Temperature C & F
# by C Lyman
# March 2019
# Activity from Module 3 of Coding & Innovation using Microbits - Python
# When button A pressed - display an adjusted current temperature in C°
# When button B pressed - display an adjusted current temperature in F°
# Checking the temperature on a Microbit and a thermometer the Microbit
# is about 2° warmer so the adjusted temperatue - 2° from the input.
from microbit import *

display.scroll("C & F")


# forever loop for Events
while True:
    celsius = temperature()
    # Event - button A pressed?
    if button_a.is_pressed():
        celsius = celsius - 2
        display.scroll(celsius)
        display.scroll("C")
        sleep(2000)
        display.clear
		
    # Event - button B pressed?
    if button_b.is_pressed():
        celsius = celsius - 2
        fahr = celsius * 9 / 5 + 32 
        display.scroll(fahr)
        display.scroll("F")
        sleep(2000)
        display.clear
