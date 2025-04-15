# Reading Data from Files
# Mr. Scott, April 15, 2025

# Typically, the file we intend to open should
# be stored in the same folder as our .py file

# STEP ONE: open the file
my_file = open("poem.txt", "r") #'r' → open for READING

# STEP TWO: Read in CONTENTS
# Option One → Read the whole file into a string
# full_text = my_file.read()   #Typically at this point we would
                             #Split up the string somehow

# Option TWO: Read each line and store in a list
list_of_lines = my_file.readlines()

# Strip out the newline character for each line
for i in range(len(list_of_lines)): #[0,1,2...
    list_of_lines[i] = list_of_lines[i].rstrip("\n")

print(f"""A poem:
{list_of_lines[0]}
{list_of_lines[1]}
{list_of_lines[2]}
""")

# Last Step
my_file.close()
