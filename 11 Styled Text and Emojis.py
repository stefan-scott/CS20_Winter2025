# Styling Text in Python
# Mr. Scott
# April 17, 2025

# Two NEW libraries:  colorama    emoji
# To install emoji library:
# Tools -> Open System Shell,  then type:  pip install emoji
from colorama import Fore, Back, Style
import emoji

# Testing out the emoji library:
print(emoji.emojize("Testing an emoji - :thumbs_up:"))
print(emoji.emojize(":anguished_face:   :carrot:   :woman_vampire:    :wrench:"))

# Testing text colors / style
# Fore→ Text color   Back→ Highlight color   Style→change weight of the text
print(Fore.RED + "Red " + Fore.BLUE + "Blue " + Fore.RESET)
print(Back.YELLOW + "Yellow" + Back.MAGENTA + "Magenta" + Back.RESET)
print(Fore.GREEN + Style.DIM + "Dim " + Style.BRIGHT + "Bright" + Style.NORMAL + "Normal")
