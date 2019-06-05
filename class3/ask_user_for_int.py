"""
File: ask_user_for_int.py
Author: Foo Barstein
Description: Showing how to ask the user for an int and make sure it's really an int
"""

# get the user's response (as a string)
real_years = input("How old is your dog (in years)?")

# this is a mistake.. it does string concatenation, since real_years refers to a string
#fake_years = real_years * 7

# this is the correct way... convert real_years to an int if you want it to be an int
fake_years = int(real_years) * 7

# one way to output this int concatenated to some strings
print('Your dog is ' + str(fake_years) + ' years old in equivalent human years.')

#another way to write the same thing
print('Your dog is', fake_years, 'years old in equivalent human years.')
