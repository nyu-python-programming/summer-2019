"""
Write a random number to a file

@author Foo Barstein
@date 19 June 2019
"""

import random

# open the file in write mode
f = open('data2.txt', 'w')

# generate a pseudo-random integer
num = random.randint(0,100)

# put together a pretty string
message = "The number is {}\n".format(num)

# write that string to the file
f.write(message)

# close the file!
f.close()
