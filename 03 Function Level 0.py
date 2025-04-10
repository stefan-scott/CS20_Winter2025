# Fortune Teller Machine
# Mr. Scott, April 7th

# Functions "level 0" (no inputs, no outputs)
# Useful for reuse of code, and organization

def fortune_one():
    #print out a fortune for the user
    print("Today is your lucky day!!")

def fortune_two():
    #print another fortune
    print("Don't step on the cracks...")

def fortune_three():
    #a final fortune
    print("Your lucky number is 1139834")

# MAIN CODE STARTS HERE...
# Use random numbers to select which
# Fortune to display
import random as r
roll = r.randint(0,2) #0,1,2

if roll == 0:
    fortune_one() #function invokation
elif roll == 1:
    fortune_two()
else:
    fortune_three()

#Another comment here to introduce the next section (if there is one...)
