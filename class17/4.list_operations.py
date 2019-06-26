"""
A few list operations and mutator functions to be aware of.

@author Foo Barstein
@date 25 June 2019
"""

a = [3, 1, 2]
b = ['c', 'a', 'b']

# create a new list made frmo the concatenation of list a and list b
c = a + b
print(c)


## MUTATOR FUNCTIONS... 
# the following function calls modify the list
# note how none of these mutator functions return anything

# sort the list of ints in ascending order
a.sort()
print("\nThe sorted a list: ")
print(a)

# sort the list of strings in ascending order
b.sort()
print("\nThe sorted b list: ")
print(b)

# include the values in b at the end of a
a.extend(b)
print("\nThe extended a list: ")
print(a)

# reverse the values in the list
a.reverse()
print("\nThe reversed a list: ")
print(a)

# remove the last value in the list
a.pop()
print("\nThe a list with its last value popped off: ")
print(a)

# remove any value from the list by its index number
print("\nThe a list with its third value popped off: ")
a.pop(2)
print(a)

# remove any value from the list by its value
a.remove('b')
print("\nThe a list with the 'b' value removed: ")
print(a)

# insert the string 'hello world' at index position 2
a.insert(2, 'hello world!')
print("\nThe a list with 'hello world!' inserted into third place: ")
print(a)

# add the value True at the end of the list
a.append(True)
print("\nThe a list with True appended at the end: ")
print(a)

