# Microbit Day Two
#
# TO INSTALL LIBRARY:
# Tools → Open System Shell
# pip install cs20-microbitio

# if "could not get a prompt error"
# THEN  press reset button,   re-run program

# Micro:bit programs are typically "Interactive Programs"
# Programs that live inside a MAIN LOOP
import microbit, time

# MICRO:BIT INPUTS
# Microbit Buttons:
# is_pressed() → is the button currently pressed
# was_pressed() → true once per single press

count_a = 0
count_b = 0

time.sleep(3) #see the bug: press buttons now!
microbit.button_a.was_pressed()
microbit.button_b.was_pressed()
  #this statement resets the button variables

while True: #Forever Loop
    if microbit.button_a.is_pressed():
        count_a += 1
    if microbit.button_b.was_pressed():
        count_b += 1
    print(f"a: {count_a} \t b: {count_b}")





