"""
File: slice_string.py
Author: Foo Barstein
Date: 3 June 2019
"""

birthdate = input("Please enter your birthdate in the format mm/dd/yy: ")

#slice the month
month = birthdate[:2]

#convert month string to an int
if month.isnumeric():
    
    month = int(month)

    #validate the month
    if month >= 1 and month <= 12:
        print("Your birth month is", month)
        print("Thanks for the good month value!")
    else:
        print("No thanks for that bad month value!")


#slice the day
day = birthdate[3:5]

#convert day string to an int
if day.isnumeric():
    day = int(day)

    #validate the month
    if day >= 1 and day <= 31:
        print("Your birth day is", day)
        print("Thanks for the good day value!")
    else:
        print("No thanks for that bad day value!")



#slice the year
year = birthdate[6:]

#convert year string to an int
if year.isnumeric():

    #validate the month
    if len(year) <= 2:
        print("Your birth year is", year)
        print("Thanks for the good year value!")
    else:
        print("No thanks for that bad year value!")

