"""
Determine whether today is early in the week, middle of the week, or late in the week.

@author Foo Barstein
@date 13 June 2019
"""

# import the datetime module
from datetime import *


"""
Determine whether a given day is early in the week.
@arg num The day to investigate, as an int
@return True if this day is early in the week, False otherwise
"""
def is_early_in_week(num):
    if num < 2:
        return True
    return False #you don't need an else since this line is only ever executed when the if statement evaluates to false

"""
Determine whether a given day is Wednesday, also known in corporate culture as "Hump Day".
@arg num The day to investigate, as an int
@return True if this day is Wednesday, False otherwise
"""
def is_humpday(num):
    if num == 2:
        return True
    return False

"""
Determine whether a given day is a weekday.
@arg num The day to investigate, as an int
@return True if this day is a weekday, False otherwise
"""
def is_weekday(num):
    if num < 5:
        return True
    return False

"""
Determine whether a given day is a weekend day.
@arg num The day to investigate, as an int
@return True if this day is a weekend day, False otherwise
"""
def is_weekend(num):
    if num >= 5:
        return True
    return False

"""
The main logic of the program.
"""
def main():
    # determine the date today
    d = date.today() # returns a specialiezd date object
    num = date.weekday(d) # returns a regular int, where 0 is Monday, 1 is Tuesday, etc.
    
    # Determine whether today is a weekday or weekend day
    if is_weekday(num):
        # it's a weekday!
        print("Today is a weekday!!!")
        
        # determine whether today is early in the week, a "hump day" or neither
        if is_early_in_week(num):
            # it's early in the week
            print("It's still early in the week... don't despair.")
        elif is_humpday(num):
            # it's Wednesday!
            print("Halfway there...")
        else:
            # it's late in the week
            print("The weekend is almost here!")
    elif is_weekend(num):
        # it's the weekend
        print("Today is a weekend!!!")
        

# run the program
main()
