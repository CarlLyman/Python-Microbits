# 4.2a Coin Toss
# by C Lyman
# July 2019
# Activity from Module 4 - Making Decisions (Conditionals)
# of Coding & Innovation using Microbits - Python
# This project uses a condition (if..then..) and
# random numbers to simulate a coin toss when 
# the microbit is shaken.

from microbit import *
import random

display.scroll("TOSS")
# set up variables and assign values of 0
toss = 0

# forever loop for Events
while True:
    # Get a random number when microbit is shaken
    # Event gesture shake?
    shake = accelerometer.was_gesture("shake")
    if shake:
        toss = random.randint(0,1)
        if toss == 1:
            display.show(Image.SMILE)
        else:
            display.show(Image.DUCK)
        sleep(5000)
        display.clear()
        toss = 0
        