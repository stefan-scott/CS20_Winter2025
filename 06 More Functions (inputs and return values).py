# More about Functions (inputs and returns)
# Mr. Scott
# April 10, 2025
# Arguments, Parameters, Returns....
# Variable Scope: WHERE in the program a variable is accessible

def add_three(num1, num2, num3): 
    # adds three numbers together
    # num1, num2, num3 → INT numbers to add 

    result = num1 + num2 + num3
    return result  #send data back to the function call

# NO INDENTATION → Global Scope, Accessible Everywhere
# a = 5
# b = 6
# c = 7

# To ways to use returned data:
# 1. Store in a variable    2. Print it out directly
r = add_three(5,6,7)

print(add_three(1,1,1))
print(add_three(5,6,7))
print(add_three(99,98,97))
