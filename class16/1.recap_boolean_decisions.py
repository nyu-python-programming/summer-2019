"""
Ask the user for a number between 1 and 10, inclusive.  Shows two ways to validate the input.
Simplest version without functions, modules, or loops.

@author Foo Barstein
@date 24 June 2019
"""

num = input("Enter a number between 1 and 10: ")


# FIRST VERSION OF VALIDATING THE INPUT
# Validate the input using positive logic
if num.isnumeric() and int(num) >= 1 and int(num) <=10 :
    
    print('Happy day!')

else:
    print("Sorry, that wasn't a good number!")


# SECOND VERSION OF VALIDATING THE INPUT
# Validate the input using negative logic
if not num.isnumeric() or not int(num) >= 1 or not int(num) <=10 :

    print("Sorry, that wasn't a good number!")

else:
    print('Happy day!')

