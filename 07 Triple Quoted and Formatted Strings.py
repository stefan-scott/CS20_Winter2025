# Triple Quoted and Formatted Strings
# Mr. Scott
# April 11, 2025
# More about text formatting + data in variables

# ----- First, Triple Quoted -----
# Four ways to encapsule a string:
# ""   ''   """ """   '''  '''

my_string = '''He'd said my hair was "cool".
That was rather nice of him.
I had thought it looked a bit weird.'''
# print(my_string)

# ----- Escape Sequences ------
# using \+another character in a string to insert something special
# \t →TAB   \n → NEWLINE   \" → "    \' → '  \\→ \

my_string2 = "ab\tc\'\n\"de\\f\g"
# print(my_string2)

# Formatted Strings - Joining strings with variables
food = "apple"
sport = "soccer"
time_remaining = 20

import random

short_story = f"""My short story:
It's time for an {food} break.
The {sport} game is nearly done.
There are {random.randint(5,20)} minutes left. """

# print(short_story)


# ----- Lists and Strings Recap + For Loops ---- #

pet_names = ["silver", "waggy", "gryffindor", "ted", "donny"]
#                0        1         2           3       4
# For Loops:
# Repeat ONCE per item in the collection (list)
# current item is stored in the LOOP VARIABLE
# for current_pet in pet_names:
#     print(f"I love my pet {current_pet}!!!!!")


# If I just want a certain number of repetitions
# use range(n) → automatically generate a list with n items

# for i in range(15):  #0 - 14
#     print(i)

# for i in range(5,10):   #start list at 5
#     print(i)            #go up to (but not include) 10

for i in range(0,100,5):  #start, end, step amount
    print(i)





