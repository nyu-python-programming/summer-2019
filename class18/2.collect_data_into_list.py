"""
Asks the user for names of books.  Stores them into a list.  Copies that list into a file.

@author Foo Barstein
@date 26 June 2019
"""

# set up a blank list of books
books = []

# output a welcome message
print("\nWelcome to the Summer Reading Book Collector!\n")

# ask the user what books they recommend
keep_going = True
while keep_going:
    response = input("Enter the name of a book (or 'exit' to quit): ")
    
    # handle the response
    if response.lower() == 'exit' or len(response) == 0:
        keep_going = False
    else:
        # store the response in the list
        books.append(response)

# print out the list of books
if len(books) == 1:
    print("This is the book you have recommended:")
elif len(books) != 0:
    print("These are the books you have recommended:")

# loop through and print out the books
for book in books:
    print( "\t- {}".format(book) )
        

# ask the user for a filename    
filename = input("What filename would you like to use to save this reading list? ")

# open up that file in write mode
f = open(filename, 'w')

# loop through the books
for book in books:
    f.write(book.title() + "\n")

# close the file
f.close()




    