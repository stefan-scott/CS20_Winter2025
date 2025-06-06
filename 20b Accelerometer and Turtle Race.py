# Accelerometer and Turtle Race
# Mr. Scott
# June 3, 2025
# Includes a recap on FUNCTIONS

import microbit, time, random, turtle

#accelerometer - measures orientation (by inertial forces)
#when flat:  			reading ~ 0
#when 90 degrees left:  reading ~ -1048
#when 90 degrees right: reading ~ 1048

# -1048     |       0      |       1048
#         -300           +300
#  LEFT            FLAT           RIGHT

def horizontal_tilt(sensitivity):
    # report the horizontal position of microbit(left, right, flat)
    # sensitivity → positive number to determine how much tilt causes
    #               non-flat reading.  (threshold)
    x = microbit.accelerometer.get_x()
    if x < sensitivity*-1:
        return "left"
    elif x > sensitivity:
        return "right"
    else:
        return "flat"
  
# Quick Turtle
t = turtle.Turtle()
s = turtle.Screen()
t.speed(0)
movement = 5  
  
while True:
    current = horizontal_tilt(300)
    #ACCELEROMTER
    if current == "left":
        t.left(10)
    elif current == "right":
        t.right(10)
    t.fd(movement)
    
    #BUTTONS
    if microbit.button_a.is_pressed():
        movement += 1
    if microbit.button_b.is_pressed():
        movement -= 1
    time.sleep(0.02)
    