# Accumulator Exercises
# Mr. Scott
# May 14, 2025
# (String Processing)

# 1. Teen Talk
# input:  a sentence (as a string)
# output: a new sentence with the word "like" between
#         each of the original words...
# ex:  "that's so fire" → "that's like so like fire"    

def teen_talk(str):
    result = ""
    for char in str:
        if char == " ":
            result = result + " like "
        else:
            result += char
    return result
