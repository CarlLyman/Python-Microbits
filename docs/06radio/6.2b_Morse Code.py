# 6.2b Morse Code
# by C Lyman
# July 2019
# Activity from Module 6 - Radio Communications
# of Coding & Innovation using Microbits - Python
# This project uses radios built in to the microbits
# to communicate by sending Morse Code using 
# button A to send "dots" and
# button B to send "dashes"

from microbit import *
import radio
radio.on()
# set the channel to 5 It can be any number (1-255)
radio.config(channel = 5)
radio.config(power=7)

display.scroll("MORSE CODE")

# forever loop for Events
while True:
    # Event button A pressed
    if button_a.was_pressed():
        radio.send("0")

    # Event button B pressed
    if button_b.was_pressed():
        radio.send("1")
             
    # set up variable to store code received
    code = radio.receive()
    if code == "0":
        display.show(Image.DIAMOND_SMALL)
        sleep(1000)
        display.clear()
        
    if code == "1":
        display.show(Image.TORTOISE)
        sleep(1000)
        display.clear()
