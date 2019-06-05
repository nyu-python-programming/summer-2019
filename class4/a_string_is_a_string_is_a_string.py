"""
File: a_string_is_a_string_is_a_string.py
Author: Foo Barstein
Date: 3 June 2019
"""


# a variable that refers to a string
x = "hello world"
print("The location of the first occurrence of letter 'o' is", x.find('o'))

# a string literal
print("The location of the first occurrence of letter 'o' is", "hello world".find('o'))

# a function that returns a string
print("The location of the first occurrence of letter 'o' is", input("Please enter the words 'hello world': ").find('o'))

# an expression that evaluates to a string
print("The location of the first occurrence of letter 'o' is", ("hello" + " " + " world").find('o'))

