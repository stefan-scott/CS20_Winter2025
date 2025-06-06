# Micro:bit First Day
# June 2, 2025
# Mr. Scott
#
# TO INSTALL LIBRARY:
# Tools → Open System Shell
# pip install cs20-microbitio
#
# If there is a "could not get a prompt" error:
#    press RESET on the microbit
#    re-run your program

import microbit, time

# Show Static Text:
for letter in "SASKATCHEWAN":
    microbit.display.show(letter)
    time.sleep(0.3) #delay in seconds

# Show Animated Text:
microbit.display.scroll("CENTENNIAL")


