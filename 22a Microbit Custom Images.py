# Microbit Custom Images
# Mr. Scott
# June 6, 2024

import microbit, time, random
#LED Values 0→off   -   9→full brightness

# Create an image of a die with a one on it
dice1 = "33333:30003:30903:30003:33333" #STR
dice1 = microbit.Image(dice1) #M:bit image object
microbit.display.show(dice1)

dice4 = "33333:" \
        "39093:" \
        "30003:" \
        "39093:" \
        "33333"  
dice4 = microbit.Image(dice4)  #image object

while True:
    if microbit.button_a.was_pressed():
        roll = random.choice([1,4])
        #could insert some animation for rolling...
        if roll == 1:
            microbit.display.show(dice1)
        elif roll == 4:
            microbit.display.show(dice4)
    
    
    
    
        