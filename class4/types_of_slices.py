"""
File: types_of_slices.py
Author: Foo Barstein
Date: 3 June 2019
"""

response = input("What's the lucky number? ")

# how to get the last thing in a string?

# this is a bad solution, but works when the number only has two characters
num_chars = len(response)
print("The number of characters in the string is", num_chars)
last_thing = response[num_chars - 2:]
print("The last thing in the line is", last_thing)


# this is perhaps a slightly better solution
position = response.rfind(" ")
print("The last space occurs at position", position)
last_thing = response[position+1:]
print("The last thing in the line is", last_thing)

