"""
File: boolean_logic_starter_kit.py
Author: Foo Barstein
Date: 4 June 2019
Description: A brief overview of boolean logic
"""


## EXAMPLES OF HOW TO REFER TO AN INT 5
5 #literal
3+2 #expression that results in a value
int("5") #a function that returns a value
x = 5
x #a variable that refers to a value

## EXAMPLES OF HOW TO REFER TO A BOOLEAN TRUE
True #literal
True and True #an expression that results in True
bool("True") #a function that returns True
x = True
x #a variable that refers to True

### BOOLEAN AND
x = True #water is wet
y = True #the sky is blue
z = False #men carry babies in the womb
a = False #3 = 2 - 2

x and y # True
y and x # True
x and z # False
z and x # false
z and a # False
a and z # False

### OR ####
x or y # True
y or x # True
x or z # True
z or x # True
z or a # False

### NOT ###
not x # False
not z # True

### == comparison ###
name = "Bob"
netID = "bc12345"

name == "Bob" # True
name == "Francis" # False
name == "Bob" and netID == "bc12345" #True
name == "Bob" and netId == "ff54321" #False

### != comparison ###
x = 5
y = 7

x == y #False
x == x #True
x != y #True
x != x #False
not (x == y) # True
not (x == x) # False


### < and > and <= and >= ###
x = 100
y = 200

x < y #True
x <= y #True
y > x #True
y >= x #True

y < x #False
y <= x #False


