# Microbit Sprite Control
# Mr. Scott
# June 9, 2025


import microbit, time, random


#  --- "Library" STARTS HERE ------

grid = [ [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0] ]

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


# ---- "Library" ENDS HERE. Main program begins ---

def generate_item_x():
    x = random.randrange(0,5)  
    while x == player_x:
        x = random.randrange(0,5)
    return x

show_grid() #Clear the screen (grid is all 0s)

player_x = 2
player_y = 2

item_x = generate_item_x()
item_y = 2
queue_pixel(item_x, item_y, 5)

plot(player_x, player_y)

start_time = time.time() #snapshot of cur time

while True: #main/game loop
    queue_pixel(player_x,player_y,0)
    #update time variables
    cur_time = time.time()
    elapsed_time = cur_time - start_time
    print(elapsed_time)
    
    # check for user event:
    if microbit.button_a.was_pressed():
        player_x -= 1
        if player_x < 0:
            player_x = 0
        
    if microbit.button_b.was_pressed():
        player_x = min(player_x + 1, 4)
    
    # check for an item collection...
    if player_x == item_x:
        # increase the score variable...
        item_x = generate_item_x()
        queue_pixel(item_x, item_y, 5)
        start_time = time.time() #resets the timer
    
    # check for running out of time
    if elapsed_time > 4:
        # took too much time - quit the game!
        print("Ran out of time!")
        break
    
    # update the screen (often should be last step)
    plot(player_x, player_y) #5,2
    time.sleep(0.1)

# more code AFTER the main loop? Ending / reporting section