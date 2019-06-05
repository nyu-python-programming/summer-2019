"""
File: a_string_is_a_string_is_a_string.py
Author: Foo Barstein
Date: 3 June 2019
"""


# left aligned within 20 characters
x = format('Prince Harry', '<20s')
print(x)


# right aligned within 20 characters
x = format('Prince Harry', '>20s')
print(x)

# center aligned within 20 characters
x = format('Prince Harry', '^20s')
print(x)

# center aligned within 20 characters, filled with carets ^
x = format('Prince Harry', '?^20s')
print(x)

# limit decimal places (WILL round up or down)
x = format(0.33999, '.2f')
print(x)



# imagine a timesheet for a job in a format like the following
#Monday      4.0     Regular time
#Tuesday     3.5     Regular time
#Wednesday   2       Over time

print(format("Monday", '<15s'), format(4.0, '<5.1f'), "Regular time")
print(format("Tuesday", '<15s'), format(3.5, '<5.1f'), "Regular time")
print(format("Wednesday", '<15s'), format(2, '<5d'), "Over time")




