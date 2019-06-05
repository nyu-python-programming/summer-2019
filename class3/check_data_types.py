"""
File: check_data_types.py
Author: Foo Barstein
Description: Double-check the data type that a user has entered.
"""

day = input("What day of the week is it? (1 for Monday, 2 for Tuesday, 3, for Wednesday, etc)")

# convert the string the user entered to an int
day = int(day)

if day == 1:
    print("Monday?! But, I wasn’t even finished with Saturday yet.") 
elif day == 2:
    print("I am not a woman on Monday, an immigrant on Tuesday, a worker on Wednesday, and a mom on Thursday, I am all of those things all of the time, and I am going to fight for all of those things all of the time.")
elif day == 3:
    print("I do doubles on Monday and Thursday, take Wednesday off or do easy cardio, do doubles on Thursday and Friday, and the weekend I just get outside and get active - jog or bike ride, or play tennis with my mom.")
elif day == 4:
    print("It's almost Friday!")
elif day == 5:
    print("It's Friday!")
elif day == 6:
    print("Good luck!  It's the weekend!")
elif day == 7:
    print("Good luck!  It's the weekend!")
  
    