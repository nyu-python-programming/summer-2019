"""
File: use_booleans_to_compare_strings.py
Author: Foo Barstein
Date: 4 June 2019
Description: Example of using boolean logic to compare strings
"""

name = input("Please enter your name: ")

if name.lower() == "amos" or name.lower() == "jessica":
    print("Welcome to the program, {}!".format(name.title()))

else:
    print("Who are you really, {}?!".format(name.title()))

if name.islower():
    print("Hey, {} - didn't you ever learn to write your name in uppercase?".format(name))


if name.isalpha():
    print("It's great that you only have alphabetic characters in your name!")
elif name.isalnum():
    print("Nice combination of alphabetic and numeric characters!")

if name.isnumeric():
    print("What kind of name is that?!")
