"""
Ask the user for a number between 1 and 10, inclusive.
This program is an extensino of the code in 2.modules_recap.py, which does not inclue loops.
This version uses a while loop to validate the number.
The file, 4.for_loops_recap.py takes this code one step further and asks the user for 10 numbers instead of one.

@author Foo Barstein
@date 24 June 2019
"""

#import recap_boolean_decisions_module
from recap_boolean_decisions_module import *

# assume we don't have a good number yet
is_good = False

# loop as long as we don't have a good number
while not is_good:
    
    # ask the user for a number
    num = ask_for_int_in_range("Enter a number between {} and {}: ", 1, 10)

    # validate that number
    is_good = validate_int_in_range(num, 1, 10)
    
    # if it's not good, tell the user!
    if not is_good:
        print("Sorry, that wasn't a good number!")
   
# if the number is good, the loop will quit, and we print out a success message
print('Happy day!')


