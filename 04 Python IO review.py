# Python IO Review
# Mr. Scott
# April 7, 2025
# Input and printing multiple things...

# OUTPUT (lvl 1) - printing one piece of data
print(99)        # print a number
print("hello")   # print a string literal
text = "CS20"
print(text)      # printing a variable (str)

# OUTPUT (lvl 2) - printing multiple strings at once
print("hello" + text) #STR+STR -> join/concat
print("hello",text)   #print with ,  prints 2 or more items with a space

# OUTPUT (lvl 3) - printing mixed types
num = 45
       #  STR        +  INT
print("best number: " + str(num))
print("best number:" , num)

# OUTPUT (lvl MAX) - formatted strings
new_text = f"best number: {num} \n text: {text}"
print(new_text)