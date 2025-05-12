# Accumulator Recap
# Mr. Scott
# May 12, 2025

# String Processing: Character Doubler
# write a function that for a given string
# returns a string with every character
# doubled.  "test"  →  "tteesstt"

def str_doubler(str):
    result = ""
    for char in str:
        result = result + char*2
    
    return result
    
    
    