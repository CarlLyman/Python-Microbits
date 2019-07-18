# 5.2b Music Tunes- Repeat Loop
# by C Lyman
# July 2019
# Activity from Module 5 - Music, Designs, LEDs, etc. (Loops)
# of Coding & Innovation using Microbits - Python
# This project plays 2 predefined tunes when A buttom is pressed.

from microbit import *
import music

display.scroll("TUNES")
while True:
    # Event - button A pressed?
    if button_a.is_pressed():
        # repeat for 2 times
        for i in range (2):
            music.play(music.PRELUDE)
            music.play(music.ODE)