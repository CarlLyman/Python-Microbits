# 5.2d European Siren While Loop
# by C Lyman
# January 2020
# Activity from Module 5 - Music, Designs, LEDs, etc. (Loops)
# of Coding & Innovation using Microbits - Python
# This project plays 2 notes based on light level

from microbit import *
import music

display.scroll("SIREN")

light =  display.read_light_level ()
while True:
    if light > 75:
        music.play("C4:4")
        display.show(Image("00000:09990:09990:09990:00000"))
        music.play("F4:4")
        display.show(Image("00000:03330:03330:03330:00000"))        
    light =  display.read_light_level ()
    