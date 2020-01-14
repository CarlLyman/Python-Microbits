# 5.2f Counter
# by C Lyman
# January 2020
# Activity from Module 5 - Music, Designs, LEDs, etc. (Loops)
# of Coding & Innovation using Microbits - Python
# This project displays the current value of 'i' counted on the screen

from microbit import *

#Count by 1s
display.scroll("COUNT1s")
for i in range (10):
    display.show(i)
    sleep (500)
    
# Count by 2s
display.scroll("COUNT2s")
for i in range (0, 10, 2):
    display.show(i)
    sleep (500)
    
# Count Down by 1s
display.scroll("CNTDWN")
for i in range (10, 0, -1):
    display.show(i)
    sleep (500)
display.scroll("FIRE")

    