"""
Asks the user for a filename.  Opens the file.  Copies the data into a list.  Outputs the data nicely.  

@author Foo Barstein
@date 26 June 2019
"""

import os

# output a welcome message
print("\nWelcome to the Summer Reading Book Recommender!\n")

# show the user the files in the current working directory
cwd = os.getcwd() # get the current working directory from the operating system
file_list = os.listdir(cwd) # get all the files here as a list

# loop through the list of available files and print them out nicely to the user
print("Here are the files in the current working directory: ")
for filename in file_list:
    print( "\t- {}".format(filename) )

# ask the user for the filename
filename = input("What is the filename of your summer reading list? ")

# open the file
f = open(filename, 'r')

# get the lines of the file as a list
books = f.readlines()
#print(books)

# reset the pointer internal to the file back to the beginning
f.seek(0)

# alternative method
file_contents = f.read()
books = file_contents.split("\n")
#print(books)

# loop through and print out the books
print("Here is your summer reading:")
for book in books:
    if len(book) > 0:
        print( "\t- {}".format(book) )
        

