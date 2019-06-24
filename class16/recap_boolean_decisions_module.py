"""
Functions that can be used to ask the user to input an integer within a given range and validate it.

@author Foo Barstein
@date 24 June 2019
"""

def ask_for_int_in_range(message, lower_bound, upper_bound):
    """
    Ask the user for an input within a given range.
    
    @param message The message to print to the user
    @param lower_bound The lower boundary of the acceptable range
    @param upper_bound The upper boundary of the acceptable range
    """
    
    num = input(message.format(lower_bound, upper_bound) ) 
    return num


def validate_int_in_range(num, lower_bound, upper_bound):
    """
    Validate a number to see whether it within a given range.
    This version uses positive logic.
    
    @param num The number to validate
    @param lower_bound The lower boundary of the acceptable range
    @param upper_bound The upper boundary of the acceptable range
    """
    
    # Validate the input using positive logic
    if num.isnumeric() and int(num) >= lower_bound and int(num) <= upper_bound :
        
        return True
    
    else:
        return False
    
def validate_int_in_range_alternate(num, lower_bound, upper_bound):
    """
    Validate a number to see whether it within a given range.
    This version uses negative logic.
    
    @param num The number to validate
    @param lower_bound The lower boundary of the acceptable range
    @param upper_bound The upper boundary of the acceptable range
    """
    
    if not num.isnumeric() or not int(num) >= lower_bound or not int(num) <= upper_bound :
    
        return False
    
    else:
        return True

    
 
