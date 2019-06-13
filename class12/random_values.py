import random

#use the random function
print("Get a random float between 0-1, not including 1")
x = random.random()
print(x)

#use randrange function
print("Get a random number between 0-9")
x = random.randrange(10)
print(x)

print("\nGet a random number between 50-100")
x = random.randrange(50, 101)
print(x)

print("\nGet a even random number between 50-100")
x = random.randrange(50, 101, 2)
print(x)

#use the randint function
print("\nGet a random integer between 1-10")
x = random.randint(1, 10)
print(x)

#use the uniform function
print("\nGet a random float betweeen 1-10")
x = random.uniform(1, 11)
print(x)

print("\nGet a random float with two decimal places betweeen 1-10 starting from a float with more decimal places")
x = random.uniform(1, 11)
x = x * 100 #shift the decimal point over two places to the right
x = int(x) #slice off the remaining decimal point values
x = x / 100 #shift the decimal point back two places to the left
print(x)