"""
Ask the user for a number between 1 and 10, inclusive.  Shows two ways to validate the input.
This version uses a module to ask for input and validate that input in two different styles.

@author Foo Barstein
@date 24 June 2019
"""


#import recap_boolean_decisions_module that contains useful functions
from recap_boolean_decisions_module import *

# ask the user for a number
num = ask_for_int_in_range("Enter a number between {} and {}: ", 1, 10)


# FIRST VERSION OF VALIDATING THE INPUT
# Validate the input using positive logic

# determine whether the number is valid or not
is_good = validate_int_in_range(num, 1, 10)

# print out an appropriate message
if is_good:
    print('Happy day!')
else:
    print("Sorry, that wasn't a good number!")


# SECOND VERSION OF VALIDATING THE INPUT
# Validate the input using negative logic

# using alternate function that performs negative logic
is_good = validate_int_in_range_alternate(num, 1, 10)
if is_good:
    print('Happy day!')
else:
    print("Sorry, that wasn't a good number!")

