import random

# open the file in write mode
f = open('data3.txt', 'a')

# generate a pseudo-random integer
num = random.randint(0,100)

# put together a pretty string
message = "The number is {}\n".format(num)

# write that string to the file
f.write(message)

# close the file!
f.close()
