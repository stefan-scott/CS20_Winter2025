# Quick Number Guesser
# Mr. Scott 
# April 7, 2025
# A review of python basics...

import random

#pick a random number
hidden_num = random.randint(1,100)  #1-100

#conditional loop is best here:
user_guess = -1  #placeholder
while user_guess != hidden_num:
    user_guess = input("Enter a num: ") #STR
    user_guess = int(user_guess) #convert str→int
    
    #report if guess is too low or too high
    if user_guess < hidden_num:
        print("TOO LOW")
    elif user_guess > hidden_num:
        print("TOO HIGH")
    else:
        print("CORRECT!") #after this the loop ends

