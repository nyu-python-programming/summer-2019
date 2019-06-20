"""
Iterate through every line in a file with a while loop.

@author Foo Barstein
@date 20 June 2019
"""

filename = 'data.txt'

f = open(filename, "r")
lines = 0

while f.readline():
    lines += 1


print( "There are {} lines in the file named '{}'".format(lines, filename) )