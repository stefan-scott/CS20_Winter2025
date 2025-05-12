# L-System Demo
# Mr. Scott
# May 12, 2025

# Turtle Code Setup Here...
import turtle
t = turtle.Turtle()
wn = turtle.Screen()
wn.setup(700,700)

t.speed(0)
#set initial position
t.up()
t.goto(-200,0)
t.down()

# L-System Code Here...
def apply_rules(ch):
    # Apply our L-System rules to a single character
    # We'll modify this for different L-systems...
    if ch == "L":
        return "+R-F-R+"
    elif ch == "R":
        return "-L+F+L-"
    else:  #If there is no rule to match ch
        return ch

def process_string(original_str):  #ABBA
    # Use accumulator pattern to computer next generation
    # one character at a time
    new_str = ""
    for c in original_str:
        new_str = new_str + apply_rules(c)
    
    return new_str

def create_L_system(num_generations, axiom):
    #Run the L-system for a set # of generations
    current_generation = axiom
    next_generation = ""
    for i in range(num_generations):
        next_generation = process_string(current_generation)
        current_generation = next_generation
        
    return next_generation
    
# Time to drive the turtle...
def draw_L_system(instructions, angle, distance):
    # interpret our L-system with the Turtle
    for cmd in instructions:
        if cmd == "F":
            t.fd(distance)
        elif cmd == "B":
            t.bk(distance)
        elif cmd == "+":
            t.right(angle)
        elif cmd == "-":
            t.left(angle)
        turtle.update() #animate quickly!
    
# MAIN CODE HERE
turtle.tracer(False)
commands = create_L_system(14, "L--F--L--F")
print(commands)
draw_L_system(commands, 37.5, 1)


wn.exitonclick()
    
