"""
How to get values out of functions without using global variables for everything

@author Foo Barstein
@date 6 June 2019
"""

# a function that returns a value
def foo():
    x = 5
    return x

# a function that does not return a value.... automatically returns None
def bar():
    x = 10
    #return None #python does this automatically if you don't say to return anything within the function

print(foo()) # will print out '5'
print(bar()) # will print out 'None'


