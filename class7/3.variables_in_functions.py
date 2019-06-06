"""
The various variables and their variability and functionlity in functions

@author Foo Barstein
@date 6 June 2019
"""

def foo():
    x = 5 # a local variable that exists only within the foobar function scope

def bar():
    global x # a global variable that exists throughout the memory space of the entire program
    x = 10


# the following line will cause an error, since x is undefined at this point
#print(x)

# a global variable named x
x = 20
print(x)

# call the function named foobar, in other words, run the code therein    
foo()

# print out the value of the variable x
# the following line will crash, since x was a local variable that only existed within the scope of the function, and now no longer exists
#print(x) #crashes, since x was local to the function foo

# call the bar function
bar()
print(x) #works wonderfully, since x is a global variable