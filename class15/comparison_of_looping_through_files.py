"""
Loop through a list in two different styles

@author Foo Barstein
@date 20 June 2019
"""

#f = open('data.txt', 'r')

# loop through lines in the file with a for loop
#for line in f:
#    line = line.strip()
#    print(line)

#f.close()


# loop through lines in the file with a while loop
f = open('data.txt', 'r')

num_lines = 0
for line in f:
    num_lines = num_lines + 1

f.close()

f = open('data.txt', 'r')

i = 0
while i < num_lines:
    line = f.readline()
    line = line.strip()
    
    print(line)

    i = i + 1


# a better example of using a while loop to iterate through lines of the file
f = open('data.txt', 'r')
lines = f.readlines()
f.close() # we're done with the file here!

i = 0
while i < len(lines):
    line = lines[i]
    line = line.strip()
    
    print(line)

    i = i + 1
    
    
    
    