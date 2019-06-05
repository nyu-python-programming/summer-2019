"""
File: slicing_and_dicing.py
Author: Foo Barstein
Date: 4 June 2019
Description: Example of using boolean logic to compare strings
"""

import random

# generate two pseudo-random numbers
die1 = random.randint(1,6)
die2 = random.randint(1,6)

# ask the user for the numbers
guess = input("Guess the two numbers, separated by a comma: ")

# flags... start with a set of baseline values
first_num_is_good = True
second_num_is_good = True
comma_is_good = True
length_is_good = True

# validate the user's response
position_of_comma = guess.find(",")
if position_of_comma != 1:
    comma_is_good = False

if not (guess[0].isnumeric() and int(guess[0]) >= 1 and int(guess[0]) <= 6):
    first_num_is_good = False

if not (guess[2].isnumeric() and int(guess[2]) >= 1 and int(guess[2]) <= 6):
    second_num_is_good = False

if len(guess) != 3:
    length_is_good = False


# determine whether everything is going well
going_well = first_num_is_good and second_num_is_good and comma_is_good and length_is_good

if going_well:
    
    # print out the numbers
    print(die1, die2)
    
    # determine whether the user guessed correctly
    
    # place a comma between the two original numbers
    #correct_answer = str(die1) + "," + str(die2) # unecessarily verbose
    correct_answer = "{},{}".format(die1, die2) # nice short and lazy
    
    
    # inform the user whether they guessed correctly or not
    if correct_answer == guess:
        print("You guessed correctly!")
    else:
        print("Wrong!  Try again.")
        
else:
    print("Your input was invalid,,, try again!")





