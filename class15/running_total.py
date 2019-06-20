"""
Add to a running total with a while loop.

@author Foo Barstein
@date 20 June 2019
"""

total = 0
stop_response = "stop"
users_response = ""

while users_response != stop_response:
    users_response = input("Enter a number: ")
    
    try:
        val = int(users_response)
        total = total + val
        
    except:
        print("Sorry, that's not a valid number")

print("The total is " + str(total))