import random

#roll imaginary dice to get two values between 1 and 6
die1 = int((random.random() * 6) + 1)
die2 = int((random.random() * 6) + 1)

#calculate the total of the dice values
total = die1 + die2

# check for snake eyes
if die1 == 1 and die2 == 1:
    print("Snake eyes!")

# output the total value
print("Your total is: " + str(total))
                  