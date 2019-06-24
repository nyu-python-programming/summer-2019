"""
Ask the user for ten numbers between 1 and 10, inclusive.
This program is an extension of the code in 3.loops_recap.py, where we only ask for one number, not ten.
This version simply validates each number one at a time, but does not store the full set of numbers.
The program named 5.loops_and_lists.py takes the code in this file one step further and stores the numbers in a list.

@author Foo Barstein
@date 24 June 2019
"""

#import recap_boolean_decisions_module
from recap_boolean_decisions_module import *

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

