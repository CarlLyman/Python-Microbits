# 3.2b Score Keeper
# by C Lyman
# March 2019
# Activity from Module 3 -Everything Counts (Variables)
# of Coding & Innovation using Microbits - Python
# This project uses counters to add 1 to a variable to increase its value.
# A scorekeeper keeps score for 2 teams by adding to each score as needed.

from microbit import *

display.scroll("SCORES")
# set up score variables and assign values of 0
score1 = 0
score2 = 0

# forever loop for Events
while True:
    # Add 1 to score2
    # Event - button A pressed?
    if button_a.is_pressed():
        score1 = score1 + 1
        # or score1 += 1
        display.scroll(score1)

    # Add 1 to score2
    # Event - button B pressed?
    if button_b.is_pressed():
        score2 = score2 + 1
        # or score2 += 1
        display.scroll(score2)

    # Display scores for each team
    # Event - pin0 touched? (pin0 & GND)
    if  pin0.is_touched():
        display.scroll("SCORE1")
        display.scroll(score1)
        display.scroll("SCORE2")
        display.scroll(score2)

    # Set scores back to 0 when shaking the Microbit
    # Event - shake?
    if accelerometer.is_gesture("shake"):
        score1 = 0
        score2 = 0
        display.scroll("SCORES")
        display.scroll(score1)

 
