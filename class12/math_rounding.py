import math

# let's say we have a float
original_val = 10.6
print(original_val)

# increase up to next int using the ceil function
round_up_val = math.ceil(original_val) #11
print(round_up_val)

# cut off decimal place using the floor function
round_down_val = math.floor(original_val) #10
print(round_down_val)

# do round up or down
rounded = round(original_val)
print(rounded)

# cut off the decimal place another way
clipped = int(original_val)
print(clipped)


