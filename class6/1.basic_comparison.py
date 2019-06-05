"""
An example of using an if/elif/else conditional statement

Created on Wed Jun  5 10:51:54 2019

@author: Foo Barstein
"""

#ask the user what their favorite fruit is and store the answer in a variable
x = input("What is your favorite fruit?")

#check the value of the variable against four different conditions
if x == "orange":    
    print("Yes, oranges are very nice")
elif x == "apple":    
    print("boring")
elif x == "strawberry":    
    print("not in season")
else:    
    print("never heard of it")

#output a generic message
print("thanks!")

#end of program
