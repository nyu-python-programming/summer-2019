"""
Functions with return values and parameters/arguments

@author Foo Barstein
@date 6 June 2019
"""

import random

def a_function_with_no_params_and_no_return_value():
    rand = random.randint(1,10)
    print(rand)    

def a_function_with_two_params_and_no_return_value(x, y):
    product = x * y
    print(product)    

def a_function_with_no_params_but_a_return_value():
    rand = random.randint(1,10)
    return rand   

def a_function_with_two_params_and_a_return_value(x, y):
    product = x * y
    return product
    

# call the first function with no parameters that returns no value
a_function_with_no_params_and_no_return_value()

# call the second function with no parameters that returns no value
a_function_with_two_params_and_no_return_value(5, 7)

# call the third function with no parameters that does return a value
print(a_function_with_no_params_but_a_return_value())

result = a_function_with_two_params_and_a_return_value(10, 2) + a_function_with_two_params_and_a_return_value(20, 3) + a_function_with_two_params_and_a_return_value(30, 4)
print(result)
