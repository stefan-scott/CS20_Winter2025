# Regular Polygons and Turtle
# Mr. Scott
# May 2, 2025

import turtle, random

# Turtle setup code (minimalist version)
wn = turtle.Screen()
roscoe = turtle.Turtle()

def triangle_simple():
    # using our turtle, draw a regular triangle
    # limitations:
    # - controls a specific global turtle
    # - size of the triangle is fixed (100)
    for i in range(3):
        roscoe.fd(100)
        roscoe.left(120)
        
def triangle_improved(active_turtle, length):
    # improved version of our function
    # any turtle can draw a regular triangle
    # side length can vary
    for i in range(3):
        active_turtle.fd(length)
        active_turtle.left(120)
        
roscoe.speed(0)
turtle.tracer(False)
sylvie = turtle.Turtle()
sylvie.color("orange")
sylvie.up() #pick up the pen
sylvie.speed(0)
sylvie.goto(random.randint(-300,300),random.randint(-300,300))
sylvie.left(random.randint(0,180))
sylvie.down()


for i in range(100):
    roscoe.up()
    sylvie.up()
    roscoe.goto(random.randint(-300,300),random.randint(-300,300))
    sylvie.goto(random.randint(-300,300),random.randint(-300,300))
    roscoe.left(random.randint(0,180))
    sylvie.left(random.randint(0,180))
    roscoe.down()
    sylvie.down()
    for side_length in range(5,300,5): #[5,10,15,...,290, 295]
        #                  start, end, skip_amount
        triangle_improved(roscoe, side_length)
        triangle_improved(sylvie, side_length)
        turtle.update()




wn.exitonclick()