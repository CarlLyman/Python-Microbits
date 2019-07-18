# 5.2a Heart Beat - Repeat Loop
# by C Lyman
# July 2019
# Activity from Module 5 - Music, Designs, LEDs, etc. (Loops)
# of Coding & Innovation using Microbits - Python
# This project uses a loop to and pin0 to display a heart beat.

from microbit import *

display.scroll("HEART")
# set up variables and assign values of 0

# forever loop for Events
while True:
    # Event - pin0 touched?
    if  pin0.is_touched():
        # action when pin0 & ground are touched
        for i in range (10):
            display.show(Image.HEART)
            sleep(1000)
            display.show(Image.HEART_SMALL)
            sleep(1000)
        display.clear()