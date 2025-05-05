# Rest of Regular Polygons
# Mr. Scott
# May 5, 2025

import turtle, random

# minimalist turtle boilerplate
wn = turtle.Screen()
rory = turtle.Turtle()
rory.speed(20)

def square(a_turtle, side_length):
    # use a given turtle to draw a square
    for i in range(4):
        a_turtle.fd(side_length)
        a_turtle.left(90)


def pentagon(a_turtle, side_length):
    # draw a pentagon
   for i in range(5):
       a_turtle.fd(side_length)
       a_turtle.left(72)

def regular_poly(a_turtle, n, side_length):
    # draw a regular polygon with n sides
    for i in range(n):
        a_turtle.fd(side_length)
        a_turtle.left(360/n)

def hollow_c(a_turtle):
    long = 100
    short = 15
    
    for i in range(3):
        a_turtle.fd(long)
        a_turtle.left(90)
    a_turtle.fd(short)
    a_turtle.left(90)
    
    a_turtle.fd(long-short)
    a_turtle.right(90)
    
    a_turtle.fd(long-(2*short))
    a_turtle.right(90)
    
    a_turtle.fd(long-short)
    a_turtle.left(90)
    
    a_turtle.fd(short)
    a_turtle.left(90) #end facing same direction

for i in range(0, 360, 4):
    hollow_c(rory)
    rory.left(4)


# for num_sides in range(3, 30):
#     regular_poly(rory, num_sides, 20)
    
#what is different:
# 1. number of repetition  EASY  n
# 2. left turn amount   360/n





# # Warm-up:  Clock Drawing
# rory.shape("turtle")
# # .forward()   .back()
# # .up()  .down()  - change pen state
# # .stamp()   - leave in impression
# 
# for i in range(12):   #solve the easy one first
#     rory.up()
#     rory.fd(50)
#     rory.down()
#     rory.forward(5)
#     rory.up()
#     rory.forward(20)
#     rory.stamp()
#     rory.back(75)
#     
#     rory.left(360/12)










wn.exitonclick()