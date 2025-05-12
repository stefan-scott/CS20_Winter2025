# L-System Demo
# Mr. Scott
# May 12, 2025

# Turtle Code Setup Here...


# L-System Code Here...
def apply_rules(ch):
    # Apply our L-System rules to a single character
    # We'll modify this for different L-systems...
    if ch == "A":
        return "B"
    elif ch == "B":
        return "AB"
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
    

