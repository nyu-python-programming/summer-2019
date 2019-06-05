# two variables that point to integers
num1 = 6
num2 = 99

# multiply the two variables together, and store the result
num3 = num1 * num2

# divide two variables and store the result
num4 = num3 / num1

# output the names of all variables and their values
print("The value of num1 is", num1, end=".\n")
print("The value of num2 is", num2, end=".\n")
print("The value of num3 is", num3, end=".\n")
print("The value of num4 is", num4, end=".\n")

# syntax errors
print('')
print("The following line of code contains a syntax error: ")
print("\t99 = num2")

print("")
print("The following line of code contains a syntax error: ")
print("\tprint('hello world\")")

# runtime errors
print('')
print("The following line of code contains a runtime error: ")
print("\tnum4 = 10 / 0")

print('')
print("The following line of code contains a runtime error: ")
print('\topen("foo.txt")')

# semantic errors
print('')
print("The following line of code contains a semantic error - we intended to multiply, but accidentally add instead: ")
print("\tnum3 = num1 + num2")

print('')
print("The following line of code contains a semantic error - we intended to get user input, but we print instead: ")
print('\tprint("foo bar")')




