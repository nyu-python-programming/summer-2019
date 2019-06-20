"""
Validate user input with a while loop.  There are multiple acceptable responses.

@author Foo Barstein
@date 20 June 2019
"""

correct_responses = ["please", "I give up", "uncle"]

users_response = ''
first_try = True

while users_response not in correct_responses:
    if not first_try:
        print('Please enter valid response!')

    users_response = input("What's the magic word? ")

    first_try = False
    

print('Thanks!')


