# Multiple Turtles and For Loops
# Mr. Scott
# May 1st, 2025

# Turtle Setup Code (Boilerplate)
import turtle, random #loads turtle.py

# Create Screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(700,700)

# Create multiple turtles
turtle_list = []
color_list = ["red", "green", "blue", "orange", "yellow", "grey", "white"]

NUM_TURTLES = 150 #all caps → Constant
angle = 360/NUM_TURTLES

#Turtle Creation
turtle.tracer(False) #don't update screen
for i in range(NUM_TURTLES): # [0,1,2...
    temp = turtle.Turtle()
    temp.color(random.choice(color_list))
    temp.left(i*angle)
    temp.speed(0)
    temp.up()
    temp.shape("turtle")
    turtle_list.append(temp)


#Loop through all turtles, and give instructions
for i in range(2000):  #[0,1,2,3..10.,1998,1999]
    for t in turtle_list:
        t.fd(5)
        t.left(random.randint(1,3))
        if i % 10 == 0: #True once for each multiple of 10
            t.stamp() #leaves an impression of the turtle
    turtle.update() #refresh the screen


# At the very end
wn.exitonclick()
