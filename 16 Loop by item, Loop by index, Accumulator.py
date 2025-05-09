# Loop by Item VS Loop by Index
# Mr. Scott
# May 9, 2025

# Also...the accumulator pattern

transport = ["airplane","bus","car","dogsled","elevator"]
#                0        1     2       3         4
#               -5       -4     -3      -2       -1
# len(transport) → 5  range(len(transport)) → [0,1,2,3,4]

# LOOP BY ITEM. Easy to code, but we don't have information
# about "where" the current item resides in the list.
# for vehicle in transport:
#     print(f"you can travel by {vehicle}")

# LOOP BY INDEX. A little longer to code, but we can still
# access each of the items and know their positions in the list.
# for index in range(len(transport)): #[0,1,2,3,4]
#     vehicle = transport[index]
#     print(f"item at pos {index}: {vehicle}")

# using the ACCUMULATOR PATTERN.
#   tries to solve a problem in small steps
#
#   start with an "empty" answer
#        - in a loop we add to it / refine it...over and over
#        - each time through the loop it should get closer to
#          our desired result
#        - when the loop ends, we have the answer

# Simple Example:  "String Copy" function
# Takes and input string, loops by index, copying all
# characters into a new string.
def copy_string(input_str):
    #1. Accumulator, make a variable to hold the answer:
    result = ""
    for i in range(len(input_str)): #[0,1,2,...]
        current_letter = input_str[i]
        if current_letter == "e":
            current_letter = "3"
        result = result + current_letter
    # when the loop is done, we've accumulated the result
    return result

# in keyword    not in keyword
def is_vowel(ch):
    # ch → a single character (as a string)
    # output Boolean, tells us if ch is a vowel or not
    vowels = "aeiou"
    if ch == "":
        return False  #edge case
    if ch in vowels:
        return True
    else:
        return False
    