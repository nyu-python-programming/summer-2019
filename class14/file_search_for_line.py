#open a text file in read mode
f = open("data.txt", "r")

search_term = "fourth"

# flag that keeps track of whether we found the line we're looking
found_it = False

# iterate through each line of the file
for line in f:
    
    # remove line break from string
    line = line.strip()
    
    # check if we are at the fourth line or greater
    if line.lower() == search_term:
        
        # flip the flag
        found_it = True
    
    # if we have previously found the line we're looking for...
    if found_it:
        
        # print it out
        print(line)
        
        
    
