"""
A simple example of a function definition and how to call it.

@author Foo Barstein
@date 6 June 2019
"""

# a function definition is always preceded by the word def
# you give functions whatever name you want, following the same rules as variable names
def foobar():
    print("hello")
    print("hi")
    print("bye")

def foo_bar():
    foobar()
    foobar()
    foobar()

# use the same name as an existing "built-in" function
# DON'T DO THIS AT HOME
def input():
    print("Sorry, we overrode the input function")

# you cannot name functions after keywords in the language    
#def and():
#    print("hello")
#    print("hi")
#    print("bye")

# run the code in our other function
foo_bar()

# run the code in our version of input
# DON'T DO THIS AT HOME
input()


