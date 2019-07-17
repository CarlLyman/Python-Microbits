# 2.2c Accelorator Tilt
# by C Lyman
# July 2019
# Activity from Module 2 of Coding & Innovation using Microbits - Python
# This project uses the tilting of Microbit and the accelerometer
# to display an arrow symbol in the direction of the tilt.

from microbit import *

display.scroll("TILT")

# forever loop for Events
while True:
    # Event - face up?
    faceUp = accelerometer.was_gesture("face up")
    if faceUp:
        display.show(Image.HAPPY)
        
    # Event - face down?
    faceDown = accelerometer.was_gesture("face down")
    if faceDown:
        display.show(Image.SAD)

    # Event - up?
    up = accelerometer.was_gesture("up")
    if up:
        display.show(Image.ARROW_S)
        
    # Event - down?
    down = accelerometer.was_gesture("down")
    if down:
        display.show(Image.ARROW_N)

    # Event - tilt right?
    right = accelerometer.was_gesture("right")
    if right:
        display.show(Image.ARROW_E)
 
    # Event - tilt left?
    left = accelerometer.was_gesture("left")
    if left:
        display.show(Image.ARROW_W)
 
    # Event gesture shake
    shake = accelerometer.was_gesture("shake")
    if shake:
        display.scroll("SHK")
        
