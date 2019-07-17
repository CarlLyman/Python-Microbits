# 2.0 Event Structures
# by C Lyman
# March 2019
# Module 2 of Coding & Innovation using Microbits - Python
# Structures for different events using Microbits

from microbit import *

# Gesture Events - Not the best version because it
#   keep 4-5 gestures in the buffer before moving
#   to the next gesture.

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
        
    # Event - face up?
    if accelerometer.is_gesture("face up"):
        # action when microbit is face up
        display.scroll("UP")
        
    # Event - face down?
    if accelerometer.is_gesture("face down"):
        # action when microbit is face down
        display.scroll("DOWN")
        
    # Event - shake?
    if accelerometer.is_gesture("shake"):
        # action when microbit is shaken
        display.scroll("SHK")

    # Event - up?
    if accelerometer.is_gesture("up"):
        # action when microbit is up (tilt forward)
        display.scroll("FWD")
        
    # Event - down?
    if accelerometer.is_gesture("down"):
        # action when microbit is down (tilt back)
        display.scroll("BACK")
        
    # Event - tilt right?
    if accelerometer.is_gesture("right"):
        # action when microbit is tilted right
        display.scroll("=>")
 
    # Event - tilt left?
    if accelerometer.is_gesture("left"):
        # action when microbit is tilted left
        display.scroll("<=")
        
    # Event - freefall?
    if accelerometer.is_gesture("freefall"):
        # action when microbit is in freefall
        display.scroll("FF")
        
    # Event - 3g?
    if accelerometer.is_gesture("3g"): #6g & 8g are options
        # action when microbit is accelerated at 3G
        display.scroll("3G")
        
          
        
        

        
