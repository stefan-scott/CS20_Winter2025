# Microbit Image Functions
# Mr. Scott
# June 5, 2025

import microbit, time, random

grid = [ [0, 0, 0, 0, 0],
         [2, 2, 2, 2, 2],
         [4, 4, 4, 4, 4],
         [6, 6, 6, 6, 6],
         [8, 8, 8, 8, 8] ]

# LED HELPER FUNCTIONS
def print_grid():
    # prints out the grid in easy-to-read format
    for row in grid:
        print(row)

def show_grid():
    # convert our 2D list to a string, and display
    result = ""  #accumulator
    for row in grid:
        for pixel in row:
            result += str(pixel)
        result += ":"
    result = result[:-1]  #remove final ":"
    print(result)
    microbit.display.show(microbit.Image(result))

def set_pixel(x, y, intensity):
    # set pixel at (x,y) to a brightness (0-9)
    grid[y][x] = intensity
    show_grid()

def plot(x,y):
    # turn pixel on at (x,y) to full brightness
    set_pixel(x,y,9)

def unplot(x,y):
    # turn off a pixel at (x,y)
    set_pixel(x,y,0)

def queue_pixel(x,y,intensity):
    #modify a pixel, but don't display yet...
    grid[y][x] = intensity

def set_all(intensity): #x:0-4  y:0-4
    #turn all pixels in the grid to INTENSITY
    for x in range(5): #0, 1, 2, 3, 4
        for y in range(5): #0, 1, 2, 3, 4
            queue_pixel(x,y,intensity)
    show_grid()

# Create an Animation
# Fading Screen
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1
# for i in range(5):
#     for brightness in range(10): #FADE IN
#         set_all(brightness)
#         time.sleep(0.005)
# 
#     for brightness in range(8, 0, -1): #FADE OUT
#         set_all(brightness)
#         time.sleep(0.005)
# set_all(0)




# Working with stopwatch / timer
print(time.time()) #tells us the current time
# time (in s) from a reference point
# ref:  GMT -00 Jan 1, 1970 at midnight

# Working with real time (stopwatch)
# 1. Before the loop, record the time
start = time.time()

# 2. Set up the main/game loop
while True:
    #3. store current time in var
    #   calculate elapsed time (difference)
    curr = time.time()
    elapsed = curr - start
    #print(elapsed)
    time.sleep(0.1) #optional step for performance
    
    #4. To reset the timer, update
    # (catch up) start variable
    if microbit.button_a.was_pressed():
        start = time.time()
    
    # Time-based events. Don't use ==, use >= <=
    if elapsed > 1:
        brightness = random.randint(0,9)
        set_all(brightness)
        start = time.time() #reset the timer

    # to exit after a certain amount of time
    if elapsed > 3:
        break #exit the loop we are in

