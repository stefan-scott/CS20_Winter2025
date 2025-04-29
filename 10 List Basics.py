favourite_places = []  #create an empty list
favourite_places.append("Saskatoon")
favourite_places.append("The forest")
favourite_places.append("Iceland")
favourite_places.append("Soccer Pitch")
print(favourite_places[1])
print(favourite_places[3])

# Exercise.  Ask the user for a number (0-3)
#            Remove that item from the list
#            Print out the list.    .pop(index)

# num = input("Enter a number (0-3): ")
# num = int(num)
# favourite_places.pop(num)
# print(favourite_places)

# 1. using the slicing operator, print out the middle two
# items in our list  0, 1, 2, 3
#
# 2. using slicing operator on favourite_places[1], select
# everything except the first 3 characters
print( favourite_places[1:3] )
# The forest
# 0123456789
print( favourite_places[1][3:] )

