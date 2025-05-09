# Custom Turtle Shapes
# Mr. Scott
# May 6, 2024
# Turtle shape by coordinates or GIF

# Turtle SETUP
import turtle

window = turtle.Screen()
mr_t = turtle.Turtle()

# Custom Shapes must be Registered
new_shape = ((-30,0), (0,-30), (30,0), (0,30)) #coordinates for a new shape- tuple
turtle.register_shape("diamond", new_shape)

mr_t.shape("diamond")
mr_t.speed(0)
mr_t.up()

y_start = 300   #each diamond is 60x60   grid of 10x10 diamonds
x_start = -300
mr_t.goto(x_start, y_start)

#draw our Argyle Pattern

for j in range(10):
    #single row:
    for i in range(10):
        mr_t.stamp()
        mr_t.forward(60)
    y_start = y_start - 60  #y_start -= 60
    mr_t.goto(x_start, y_start)
mr_t.shape("turtle")

# REGISTER A GIF for turtle shape
# a few things:
# .gif only, probably not animated
# not all gif images have transparent backgrounds
#     may need to use a tool to do this...
# image rotation is fixed; doesn't actually reflect heading
turtle.register_shape("turtle_image.gif")
mr_t.shape("turtle_image.gif")
mr_t.speed(1)
mr_t.left(65)
mr_t.fd(500)

window.exitonclick()