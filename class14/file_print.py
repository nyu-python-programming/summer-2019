"""
Read the data from a text file and print it out.

@author Foo Barstein
@date 19 June 2019
"""

#open a text file in read mode
f = open("data.txt", "r")

#pull all the data out of the file into a variable
the_text = f.read()

#print out the contents of the file
print(the_text)


