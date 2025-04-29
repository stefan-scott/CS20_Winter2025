# Rainbow Text and Functions Review
# April 28, 2025
# Mr. Scott

from colorama import Fore, Back, Style

def rainbow_text(input_text):
    # style the input_text with rainbow coloring
    # and return that styled string
    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.BLUE, Fore.MAGENTA]#OOB
    #            0            1           2          3           4         5
    output_text = Style.BRIGHT+Back.BLACK
    color_index = 0
    
    for letter in input_text:
        output_text = output_text + colors[color_index]
        output_text = output_text + letter
        
        color_index += 1 #now, advance the color
        if color_index >= len(colors):
            color_index = 0
            
    output_text += Back.RESET
    return output_text
    




# Function taking input, no return value
# non-fruitful function
def func_a(a, b, c):
    # function that joins/prints 3 things together
    # a, b, c → string type data
    print(f"{a}{b}{c}")

# fruitful variant
def func_b(a, b, c):
    # a, b, c → string type data
    # join a,b,c and RETURN the data
    return f"{a}{b}{c}"

#result = func_b("hi", "there", "cs20")