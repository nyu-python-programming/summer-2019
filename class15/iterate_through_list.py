"""
Iterate through every item in a list with a while loop.

@author Foo Barstein
@date 20 June 2019
"""

list_of_values = [ 'they', 'sailed', 'away', 'in', 'a', 'sieve', 'they', 'did' ]
i = 0
while i < len(list_of_values):
    val = list_of_values[i]
    print(val)
    i += 1
