# 3.2a Counter
# by C Lyman
# March 2019
# Activity from Module 3 of Coding & Innovation using Microbits - Python
# This project uses a counter to add 1 to a variable to increase its value.
# At Costco store the person greeting everyone is also using a counter
# in their hand to keep track of how many people enter so they can 
# have enough checkers to get people through their lines.

from microbit import *

display.scroll("COUNT")
# set up a variable count and assign it a value of 0
count = 0

# forever loop for Events
while True:
    # Event - button A pressed?
    if button_a.is_pressed():
        count = count + 1
        display.scroll(count)
