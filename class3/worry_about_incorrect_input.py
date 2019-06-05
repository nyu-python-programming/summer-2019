"""
File: worry_about_incorrect_input.py
Author: Foo Barstein
Description: How to deal with incorrect data input
"""

# asking user for a string that is the month
month = input("Please enter the month of the year: ")

# check whether it is a number between 1 and 12
if month.isnumeric():
    # we know the string has only numeric characters in it
    month = int(month)
else:
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    
    # make sure the first letter of what the user typed is capitalized
    month = month.capitalize()
    
    if month in months:
        print("hi,", month)
        