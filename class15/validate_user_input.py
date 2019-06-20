"""
Validate user input with a while loop.

@author Foo Barstein
@date 20 June 2019
"""

correct_response = "please"

users_response = ""

while users_response != correct_response:
    users_response = input("What's the magic word? ")
