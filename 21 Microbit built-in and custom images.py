# Microbit built-in and custom images
# Mr. Scott
# June 4, 2025

import microbit, time, random

print(microbit.Image.STD_IMAGE_NAMES)

# Display Built-in Image on Microbit
microbit.display.show(microbit.Image.SKULL)
time.sleep(1)

# Display an Animation
clocks = microbit.Image.ALL_CLOCKS
# print(clocks)

# Loop by Item
# for hour in clocks:
#     microbit.display.show(hour)
#     time.sleep(0.3)

# Loop by Index, using a while loop
i = 0  #0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11   13→0
ani_delay = 0.2
while True:
    # Display Animation and update i
    hour = clocks[i]
    microbit.display.show(hour)
    i += 1
    if i > 11:
        i = 0
    time.sleep(ani_delay)
    
    # Check for button press Events
    if microbit.button_a.was_pressed():
        ani_delay = max(0, ani_delay-0.02)
#         ani_delay -= 0.02
#         if ani_delay < 0:
#             ani_delay = 0
    
    if microbit.button_b.was_pressed():
        ani_delay += 0.02
        #max delay should be 0.5s
        ani_delay = min(0.5, ani_delay+0.02)
    
    print(f"delay amount: {ani_delay}")



