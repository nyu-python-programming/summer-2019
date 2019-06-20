"""
Iterate through every item in a range with a while loop.

@author Foo Barstein
@date 20 June 2019
"""

range_of_nums = range(10, 20, 3)
i = 0
while i < len(range_of_nums):
    val = range_of_nums[i]
    print(val)
    i += 1
