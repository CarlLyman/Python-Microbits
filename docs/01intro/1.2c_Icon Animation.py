# 1.2c Icon Animation
# by C Lyman
# March 2019
# Activity from Module 1 of Coding & Innovation using Microbits - Python
# Displays Icons from the library with animation

from microbit import *

# forever loop
while True:
    display.show(Image.HEART_SMALL)
    sleep(1000)
    display.show(Image.HEART)
    sleep(1000)
