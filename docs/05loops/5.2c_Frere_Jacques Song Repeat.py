# 5.2c Frere Jacques Song - Repeat Loop
# by C Lyman
# July 2019
# Activity from Module 5 - Music, Designs, LEDs, etc. (Loops)
# of Coding & Innovation using Microbits - Python
# This project uses an A button pressed to play music.
# Each line of the song repeats 2 times so each line 
# can be put in a loop and repeated.

from microbit import *
import music

display.scroll("SONG")
# Adjust tempo
music.set_tempo(bpm=180)

# forever loop for Events
while True:
    # Event - button A pressed?
    if  button_a.is_pressed():
        # action when button A is pressed
        #repeat for 2 times
        for i in range (2):
            music.play("C4:4")
            music.play("D4:4")
            music.play("E4:4")
            music.play("C4:4")
        #repeat for 2 times
        for i in range (2):
            music.play("E4:4")
            music.play("F4:4")
            music.play("G4:8")
        #repeat for 2 times
        for i in range (2):
            music.play("G4:2")
            music.play("A4:2")
            music.play("G4:2")
            music.play("F4:2")
            music.play("E4:4")
            music.play("C4:4")
        #repeat for 2 times
        for i in range (2):
            music.play("C4:4")
            music.play("G3:4")
            music.play("C4:8")
             