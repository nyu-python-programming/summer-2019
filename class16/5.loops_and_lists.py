"""
Ask the user for ten numbers between 1 and 10, inclusive, and store the numbers in list.
This is an extension of the 4.for_loops_recap.py program, which does not include the list.
This version uses a lists to store and regurgitate the input.

@author Foo Barstein
@date 24 June 2019
"""

#import recap_boolean_decisions_module
from recap_boolean_decisions_module import *

# make a blank list... this will hold the numbers the user enters
numbers = []

# iterate a loop 10 times
for i in range(1, 11):
    
    # get a string with the number in i
    extra_prefix = "{} - ".format(i)
    
    # assume we don't have a good number yet
    is_good = False

    # loop as long as we don't have a good number
    while not is_good:
        
        # ask the user for a number
        num = ask_for_int_in_range(extra_prefix + "Enter a number between {} and {}: ", 1, 10)

        # validate that number
        is_good = validate_int_in_range(num, 1, 10)
        
        # if it's not good, tell the user!
        if not is_good:
            print("Sorry, that wasn't a good number!")
   
    # if the number is good, the loop will quit, and we print out a success message
    print('Happy day!')
    
    # add the number we got to the list of numbers
    numbers.append(num)



# print out the list of numbers in raw form
#print(numbers)


# loop through all the numbers in the list
print('\nYou entered the following numbers:')
for num in numbers:
    
    # print out each number
    print('\t-{}'.format(num) )


# loop through only the last 3 numbers in the list
print('\nHere are the last 3 numbers you entered:')
last_three = numbers[-3:]
for num in last_three:
    # print out each of the last 3 numbers
    print('\t-{}'.format(num) )

# figure out how many numbers are in the list
num_values = len(numbers)
print('\nThank you for those {} numbers!'.format(num_values ) )


