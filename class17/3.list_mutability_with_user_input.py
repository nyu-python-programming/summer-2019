"""
This program outputs a list of groceries and allows the user to change any of them.

@author Foo Barstein
@date 25 June 2019
"""

def print_groceries(groceries):
    """
    This function outputs a nicely formatted list of groceries
    
    @param groceries The list of groceries to iterate through
    """
    
    # print out the list contents
    print("\nThe groceries list contains the following items:")
    
    # set a counter, which keeps track of how many times we have looped
    counter = 1 

    # loop through all the values in the list
    for product in groceries:
        
        # print out the value in the list, prefixed with the counter
        print( '\t{} - {}'.format(counter, product) )
        
        # increment the counter
        counter = counter + 1
    
    
def handle_floats(product_identifier):
    """
    This function checks whether the product identifier a user typed has a decimal point in it, and removes everything after the decimal point if so.
    
    @param product_identifier The string the user entered when identifying a product
    @return The product identifier as a string with just an integer in it.
    """

    # check whether the product_identifier has a dot in it
    if "." in product_identifier:

        # if so, make a list of the values before and after the dot
        values = product_identifier.split(".")
        
        # if the value before the dot is an integer...
        if values[0].isnumeric():
            
            # set the identifier to be just this value before the dot
            product_identifier = values[0]
            
    # return the product identifier, which may or may not have been modified 
    return product_identifier
            


# a list of groceries we intend to buy
groceries = [
                "broccoli",
                "2% milk",
                "whole wheat bread",
                "spaghetti",
                "no pulp orange juice"
            ]

# print out the items in the list
print_groceries(groceries)

# ask the user whether they want to replace any of the items in the list
response = input("Would you like to replace any products in this groceries list? ")

# a list of acceptable responses to the question
acceptable_responses = ['yes', 'y', 'yeah', 'sure', 'ok', 'fine']

# if what the user entered is indeed one of the acceptable responses...
if response.lower() in acceptable_responses:
    
    # ask the user which product they want to replace
    product_identifier = input("Which product would you like to replace? ")
    
    # replace floating point numbers with ints if necessary
    product_identifier = handle_floats(product_identifier)
    
    # if what the user typed is a valid int...
    if product_identifier.isnumeric() and int(product_identifier) <= len(groceries) and int(product_identifier) > 0:
        
        # the user did type an integer.. subtract one and use that as the index
        index = int(product_identifier) - 1
        
        # ask the user what they want to swap it for
        new_product = input("What you would like to replace {} with?".format(groceries[index]) )
        
        # update that value in the list with the new product
        groceries[index] = new_product
        
    # otherwise if what the user typed is one of the values in the list...
    elif product_identifier in groceries:
        
        # the user typed a product name... find its index
        index = groceries.index(product_identifier)

        # ask the user what they want to swap it for
        new_product = input("What you would like to replace {} with?".format(groceries[index]) )
        
        # update that value in the list with the new product
        groceries[index] = new_product
        
    # otherwise, if the user didn't type an integer, and didn't type the name of one of the products in the list...
    else:
        # print an error message
        print("Sorry, {} is not in the groceries list.".format(product_identifier) )
        
        
# print out the items in the list
print_groceries(groceries)


