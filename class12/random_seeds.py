import random

print("Pseudo-random set of numbers based on seed 4")
random.seed(4)
print(random.random())
print(random.random())
print(random.random())
print(random.random())


print("\nSame pseudo-random set of numbers based on seed 4")
random.seed(4)
print(random.random())
print(random.random())
print(random.random())
print(random.random())


print("\nDifferent pseudo-random set of numbers based on seed 111")
random.seed(111)
print(random.random())
print(random.random())
print(random.random())
print(random.random())