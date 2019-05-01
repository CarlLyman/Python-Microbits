# 4.2b Dice Roll
# by C Lyman
# May 2019
# Activity from Module 4 - Making Decisions (Conditionals)
# of Coding & Innovation using Microbits - Python
# This project uses a condition (if..then..) and
# random numbers to simulate a dice roll when 
# the microbit is shaken.

from microbit import *
import random

display.scroll("DICE")
# set up variables and assign values of 0
roll = 0
roll1 = 1
roll2 = 2
roll3 = 3
roll4 = 4
roll5 = 5
roll6 = 6

# forever loop for Events
while True:
    # Get a random number when microbit is shaken
    # Event gesture shake?
    shake = accelerometer.was_gesture("shake")
    if shake:
        roll = random.randomint(6)
        if roll == 1:
            display.show(roll1)
        elif roll==2:
            display.show(roll2)
        elif roll==3:
            display.show(roll3)
        elif roll==4:
            display.show(roll4)
        elif roll==5:
            display.show(roll5)
        else:
            display.show(roll1)
        sleep(5000)
        display.clear()
        roll = 0
        