"""
Validate numeric user input with a while loop.

@author Foo Barstein
@date 20 June 2019
"""


# a while loop that breaks when valid input is entered
while True:
    
    response = input('Please enter an integer between 1 and 10, inclusive: ')

    if response.isnumeric() and int(response) >= 1 and int(response) <= 10:
        break
    
    else:
        print('Please enter a valid integer between 1 and 10.')

print('Done')
 

# a while loop that sets a flag to False when valid input is entered
good_input = False

while not good_input:
    
    response = input('Please enter an integer between 1 and 10, inclusive: ')

    if response.isnumeric() and int(response) >= 1 and int(response) <= 10:
        good_input = True
    
    else:
        print('Please enter a valid integer between 1 and 10.')

print('Done')








   