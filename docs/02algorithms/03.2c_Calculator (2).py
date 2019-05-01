# 3.2c Score Keeper
# by C Lyman
# May 2019
# Activity from Module 3 -Everything Counts (Variables)
# of Coding & Innovation using Microbits - Python
# This project uses variables, counters, 
# and math to add 2 numbers together.

from microbit import *

display.scroll("SUM")
# set up variables and assign values of 0
numberA = 0
numberB = 0
total = 0

# forever loop for Events
while True:
    # Add 1 to numberA
    # Event - button A pressed?
    if button_a.is_pressed():
        numberA = numberA + 1
        # or numberA += 1
        display.scroll(numberA)

    # Add 1 to numberB
    # Event - button B pressed?
    if button_b.is_pressed():
        numberB = numberB + 1
        # or numberB += 1
        display.scroll(numberB)
        
    # Display scores for each team
    # Event - pin0 touched? (pin0 & GND)
    if  button_a.was_pressed() and button_b.was_pressed():
        display.scroll("NUMBER A")
        display.scroll(numberA)
        display.scroll("NUMBER B")
        display.scroll(numberB)
        total = numberA + numberB
        display.scroll("SUM")
        display.scroll(total)

    # Set numbers back to 0 when shaking the Microbit
    # Event gesture shake?
    shake = accelerometer.was_gesture("shake")
    if shake:
        numberA = 0
        numberB = 0
        total = 0
        display.scroll("NUMBERS")
        display.scroll(numberA)