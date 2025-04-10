# Area of a Square Calculator
# Mr. Scott
# April 4, 2025
# A first look at user input and data types

# Start by asking user for width and height info
width = input("enter a width:\t")  #\t → TAB
height = input("enter a height:\t")

    #input() ALWAYS YIELDS A STRING!!! 
# Since we want our variables to be numbers,
# We must convert them into numeric types
# int()   float()   str()   bool()
width = float(width)
height = float(height)

# Calculate and report the correct area:
area = width * height

print("The area is " + str(area) + " units squared")                                  