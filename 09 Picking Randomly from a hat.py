# Picking a name from a hat

import random

names = ["Stefan", "Aubree", "Megan", "Jeremiah"] #len==4
        #   0         1         2        3  (len-1)        
        #   -4        -3        -2      -1

#Approach 1: random by index
index = random.randint(0, len(names)-1)
#print(names[index])

#Approach 2: random by choice
sibling = random.choice(names)
print(sibling)