# 2.0 Event Structures
# by C Lyman
# July 2019
# Module 2 of Coding & Innovation using Microbits - Python
# Structures for different events using Microbits

from microbit import *

# forever loop for Events
while True:
    # Event - button A pressed?
    if button_a.is_pressed():
        # action when A is pressed
        display.show("A")
        
    # Event - button B pressed?
    if  button_b.is_pressed():
        # action when B is pressed
        display.show("B")
        
    # Event - buttons AB pressed?
    if  button_a.was_pressed() and button_b.was_pressed():
        # action when A&B are pressed
        display.scroll("AB")
        
    # Event - pin0 touched?
    if  pin0.is_touched():
        # action when pin0 & ground are touched
        display.show("0")
        
    # Event - pin1 touched?
    if  pin1.is_touched():
        # action when pin1 & ground are touched
        display.show("1")

    # Event - pin2 touched?
    if  pin2.is_touched():
        # action when pin2 & ground are touched
        display.show("2")
        
    # Event gesture face up
    faceUp = accelerometer.was_gesture("face up")
    if faceUp:
        display.scroll("UP")
    
    # Event gesture face down
    faceDown = accelerometer.was_gesture("face down")
    if faceDown:
        display.scroll("DWN")
        
    # Event gesture shake
    shake = accelerometer.was_gesture("shake")
    if shake:
        display.scroll("SHK")
        
    # Event gesture up
    up = accelerometer.was_gesture("up")
    if up:
        display.scroll("^")
        
    # Event gesture down
    down = accelerometer.was_gesture("down")
    if down:
        display.show("v")
        
    # Event gesture right
    right = accelerometer.was_gesture("right")
    if right:
        display.show(">")
        
    # Event gesture left
    left = accelerometer.was_gesture("left")
    if left:
        display.show("<")
        
    # Event - freefall?
    freefall = accelerometer.was_gesture("freefall")
    if freefall:
        # action when microbit is in freefall
        display.scroll("FF")
        
    # Event - 3g?
    threeG = accelerometer.was_gesture("3g")
    if threeG:
    #6g & 8g are also options
        # action when microbit is accelerated at 3G
        display.scroll("3G")
        
