# 6.2a Radio Initials
# by C Lyman
# July 2019
# Activity from Module 6 - Radio Communications
# of Coding & Innovation using Microbits - Python
# This project uses radios built in to the microbits
# to communicate and a person's initials 
# when the A button is pressed 

from microbit import *
import radio
radio.on()
# set the channel to 5 It can be any number (1-255)
radio.config(channel = 5)
radio.config(power=7)

display.scroll("INITIALS")

# forever loop for Events
while True:
    # Event gesture shake?
    if button_a.was_pressed():
        radio.send("ME")
        
    # set up variable to store receive initials
    initials = radio.receive()
    if initials is not None:
        display.scroll(initials)
        sleep (2000)
        initials = ""
    