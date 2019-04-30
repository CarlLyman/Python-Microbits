# 2.2c Accelorator Tilt
# by C Lyman
# March 2019
# Activity from Module 2 of Coding & Innovation using Microbits - Python
# This project uses the tilting of Microbit and the accelerometer
# to display an arrow symbol in the direction of the tilt.

from microbit import *

display.scroll("TILT")

# forever loop for Events
while True:
    # Event - face up?
    if accelerometer.is_gesture("face up"):
        display.show(Image.HAPPY)
        
    # Event - face down?
    if accelerometer.is_gesture("face down"):
        display.show(Image.SAD)

    # Event - up?
    if accelerometer.is_gesture("up"):
        display.show(Image.ARROW_S)
        
    # Event - down?
    if accelerometer.is_gesture("down"):
        display.show(Image.ARROW_N)

    # Event - tilt right?
    if accelerometer.is_gesture("right"):
        display.show(Image.ARROW_E)
 
    # Event - tilt left?
    if accelerometer.is_gesture("left"):
        display.show(Image.ARROW_W)
        
