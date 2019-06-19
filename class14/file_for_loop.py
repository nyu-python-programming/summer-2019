"""
Open up a text file, and loop through every line.  
Count lines and print out the fourth line and all subsequent lines.

@author Foo Barstein
@date 19 June 2019
"""

#open a text file in read mode
f = open("data.txt", "r")

# set up a counter
line_number = 0

# iterate through each line of the file
for line in f:
    
    # remove line break from string
    line = line.strip()
    
    # count the line we're currently on
    line_number = line_number + 1
    
    # check if we are at the fourth line or greater
    if line_number >= 4:

        # if so, print out the line
        print(line)
    
# it's polite to python to close the file
f.close()
