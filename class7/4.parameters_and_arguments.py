"""
How to get values into a function

@author Foo Barstein
@date 6 June 2019
"""
# define a function a parameter... a local variable whose value is TBD
def foo(x):
    y = x + 10
    print(y)
    
# define a function with two parameters... both local variables of course
def bar(num1, num2):
    product = num1 * num2
    print(product)

    
# call the function with an argument
foo(5)

# call the function with two arguments
bar(10, 20)

# call the function with two arguments that are variable values
num1 = 20
num2 = 10
bar(num2, num1)

# call the function with named arguments
bar(num2=10, num1=5)


# call one of two functions based on a random number
import random
rand = random.randint(0,1)

# PERHAPS THIS IS TOO MUCH INFORMATION... DON'T WORRY ABOUT THIS FOR THIS CLASS
if rand == 0:
    # if rand is a zero, this is the defintion of the function x
    def x(num):
        print("Hello... the random number is {}".format(num))
else:
    # if rand is a one, this is the defintion of the function x
    def x(num):
        print("Goodbye... the random number is {}".format(num))
        
# call whichever x defintion has been executed
x(rand)





