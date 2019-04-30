# 2.0 Sensors 
# by C Lyman
# April 2019
# Module 2 of Coding & Innovation using Microbits - Python
# Code for different sensors using Microbits

from microbit import *

while True:
# Sensor code lines and examples with value stored in a variable

# Temperature in Celsius 
# Code: temperature()
# Example: 
    temp = temperature()
       
# Light level from the display 0-255
# Code: display.read_light_level()
# Example: 
    light = display.read_light_level()
        
# Acceleration x - tilting left - right + 
# 0 when flat facing up
# Code: accelerometer.get_x()
# Example: 
    accelX = accelerometer.get_x()

# Acceleration y - tilting forward + back - 
# 0 when flat facing up
# Code: accelerometer.get_y()
# Example: 
    accelY = accelerometer.get_y()

# Acceleration z - moving up + down - 
# -1024 when flat face up (Gravity acting downwards)
# 1024 when face down 
# vigorous movement will get values +-2048
# Code: accelerometer.get_z()
# Example: 
    accelZ = accelerometer.get_z()

# Acceleration all axes 
# Code: accelerometer.get_values()
# Example: 
    accelXYZ = accelerometer.get_values()

# Compass Calibrate 
# The compass must be calibrated before it can be used.
# The microbit asks you to "tilt until the screen is filled".
# When that is completed a smiley face shows on the screen.
# Then the compass will work.
# Code: compass.calibrate()
# Example: 
    compass.calibrate()

# Compass Heading 
# Gives a compass degrees for the direction top of the microbit 
# (away from the pins) is pointed. 0 or 360 North, 90 East, 
# 180 South, and 270 West.
# Code: compass.heading()
# Example: 
    compassHeading = compass.heading()

# Compass x gives a magnetic field strength reading in nano tesla
# Code: compass.get_x()
# Example: 
    magnetismX = compass.get_x()

# Compass Strength gives an indication of the magnitude 
# of the magnetic field strength around the device in nano tesla
# Code: compass.get_field_strength()
# Example: 
    magnetismStrength = compass.get_field_strength()
	

