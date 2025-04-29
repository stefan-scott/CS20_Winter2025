# First Turtle Program
# Mr. Scott
# April 29, 2025
# A look at window, turtle, movement, color
#
# Reminder: NEVER save your file as turtle.py

import turtle, random

# Boilerplate code → "startup code for using turtle"
window = turtle.Screen() # creates a screen object
window.bgcolor("lightblue")  #sets background color
window.setup(600,300) #resize screen dimensions

my_turtle = turtle.Turtle() #creates a turtle object
my_turtle.color("yellow")  #change pen color
my_turtle.pensize(4)  #thickness of line (in px)
my_turtle.speed(0) #0 - max speed

turtle.tracer(False)

# PROGRAM 3 - Loops and color strings
colors = ["LightSeaGreen","MediumSlateBlue", "PowderBlue", "Teal", "SpringGreen"]
num_moves = 40

for j in range(360):
    my_turtle.down()  #puts the pen down
    for i in range(num_moves): #[0,1,2,3...,num_moves-1]
        my_turtle.color(random.choice(colors))
        my_turtle.fd(5)
    my_turtle.up()
    my_turtle.goto(0,0)
    my_turtle.left(1)
    turtle.update()  #when the tracer is off
                    #update() allows to manually refresh

# PROGRAM 2 - A few more instructions
# my_turtle.bk(75)  #.backward()  .back()  .bk()
# my_turtle.rt(62)  #.rt()   .right()
# my_turtle.fd(110) #.fd()   .forward()
# my_turtle.goto(0,0) #absolute movement to (x,y)

# PROGRAM 1 - Basic Movement
# my_turtle.forward(100)  # move forward 100 pixels
# my_turtle.left(45)      # turn left (CCW) 45 degrees
# my_turtle.backward(150) # move backward 150 pixels

# AT THE VERY END OF YOUR PROGRAM....
window.exitonclick() #waits for a click, then closes
