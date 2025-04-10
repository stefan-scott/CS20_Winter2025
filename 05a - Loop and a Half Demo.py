# Loop-and-a-half Demo
# Mr. Scott
# April 9, 2025
# "Forever" Loop, break, continue

# create an infinite loop
while True:
    "choice is set to input()"
    choice = input("Stop the loop? [yes/no]") #yes YES Yes yES
    if choice.upper() == "YES":
        break  #exits the current loop
    else:
        continue #"restarts" the loop
                 #it goes immediately to the next iteration
    print("let's ask it again...")
