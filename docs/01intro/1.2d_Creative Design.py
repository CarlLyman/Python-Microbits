# 1.2d Creative Design
# by C Lyman
# March 2019
# Activity from Module 1 of Coding & Innovation using Microbits - Python
# Displays Creative Design using LEDs & number code for brightness
# LED brightness are in the range 0-9 with 0 off and 9 bright

from microbit import *

# Boat design
display.show(Image("00900:"
                   "05550:"
                   "00600:"
                   "79997:"
                   "09990"))
sleep(3000)
# X with bright center
display.show(Image("50005:07070:00900:07070:50005"))