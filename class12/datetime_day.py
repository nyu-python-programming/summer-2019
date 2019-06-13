"""
Determine the day of the week today.

@author Foo Barstein
@date 13 June 2019
"""

from datetime import *

"""
Return the name of the day, based on its number, where 0 is Monday, 1 is Tuesday, etc.
@arg num The number of the day, as an int
@return The name of the day
"""
def getDayName(num):
    #receive the numeric day as input in the variable dayNum
    #figure out what weekday is based on the dayNum
    
    if num == 0:
        weekday = "Monday"
    elif num == 1:
        weekday = "Tuesday"
    elif num == 2:
        weekday = "Wednesday"
    elif num == 3:
        weekday = "Thursday"
    elif num == 4:
        weekday = "Friday"
    elif num == 5:
        weekday = "Satuday"
    elif num == 6:
        weekday = "Sunday"
    else:
        weekday = "" #another way to assign a default value to day
        
    #send the human-friendly day as output from the function
    return weekday


# this function does the same thing as the function above, but with far less code
"""
Return the name of the day, based on its number, where 0 is Monday, 1 is Tuesday, etc.
@arg num The number of the day
@return The name of the day
"""
def getDayNameBetter(dayNum):
    # make a list of days... these are automatically indexed starting from 0
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Satuday", "Sunday"]
    
    # return the day in the list at the given index position
    return days[dayNum]


# a function containing the main logic of the program
"""
The main logic of the program.
"""
def main():

    #get today's date as a specialied "date object"
    today = date.today() 

    #convert the "date object" to a number between 0-6 representing the day
    day_num = date.weekday(today) 
    
    #convert that number to a human-friendly day using both functions
    friendlyDay1 = getDayName(day_num) 
    friendlyDay2 = getDayNameBetter(day_num) 

    print("Today is {}!".format(friendlyDay1) ) #print that day out
    print("Yes, today is {}!".format(friendlyDay2) ) #print that day out

#start up
main()
