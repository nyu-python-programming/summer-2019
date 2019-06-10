"""

Solution to the in-class mini-workshop about functions.
We ask the user to enter an email and password, and validate that they are good.

@author Foo Barstein
@date 10 June 2019

"""

# a dedicated function that asks the user for an email address
def get_email():
    email = input("Please enter an email address: ")
    return email

# a dedicated function that asks the user for a password
def get_password():
    password = input("Please enter a password: ")
    return password

# a dedicated function to validate the email
def validate_email(email):
    # create a bunch of flags that represent our starting assumptions
    contains_at_sign = False
    contains_letters = False
    contains_numbers = False
    contains_nyu_dot_edu = False
    
    # determine whether it contains an @ sign in the middle somewhere
    position_of_at_sign = email.find("@") #the position of the @
    if position_of_at_sign >= 1 and position_of_at_sign < (len(email) -1) :
        # it has the at sign in the middle somewhere!
        contains_at_sign = True
    
    # determine whether it contains two letters at the beggining
    first_two_chars = email[:2] # the first two characters
    first_three_chars = email[:3] # the first three characters
    if first_three_chars.isalpha() or first_two_chars.isalpha():
        # it has letters as the first two or three characters!
        contains_letters = True
        
    # determine whether it contains four numbers after the letters
    if first_three_chars.isalpha() and email[3:7].isnumeric():
        # if the first three characters are alphabetic and the subsequent four characters are numeric, it's good!
        contains_numbers = True
    elif first_two_chars.isalpha() and email[2:6].isnumeric():
        # if the first two characters are alphabetic and the subsequent four characters are numeric, it's good!
        contains_numbers = True
        
    # determine whether the email address ends in '@nyu.edu'
    search_term = "@nyu.edu"
    position_of_search_term = email.find(search_term)
    if position_of_search_term == len(email) - len(search_term):
        # the email address ends in '@nyu.edu'
        contains_nyu_dot_edu = True
        
    # debugging... remove this once you're sure it all works
    debug(contains_at_sign, contains_letters, contains_numbers, contains_nyu_dot_edu)

    # return True if all requirements are met, False otherwise
    if contains_at_sign and contains_letters and contains_numbers and contains_nyu_dot_edu:
        # good!
        return True
    else:
        # no good!
        return False
    
# a dedicated function to output a success message
def output_success_message():
    print("Your NYU email address is valid!")

# a dedicated function to output a failure message
def output_failure_message():
    print("You have entered an invalid email address!")
    
# a dedicated function for outputting debugging messages
def debug(contains_at_sign, contains_letters, contains_numbers, contains_nyu_dot_edu):
    # debugging... show what we know about the email
    if contains_at_sign:
        print("The email address contains an @ sign.")
    else:
        print("The email address does not contain an @ sign.")
        
    if contains_letters:
        print("The email address contains 2 or 3 alphabetic letters at the beginning.")
    else:
        print("The email address does not contain 2 or 3 alphabetic letters at the beginning.")

    if contains_numbers:
        print("The email address contains 4 numbers after the letters.")
    else:
        print("The email address does not contain 4 numbers after the letters.")
        
    if contains_nyu_dot_edu:
        print("The email address contains '@nyu.edu' at the end.")
    else:
        print("The email address does not contain '@nyu.edu' at the end.")

# a dedicated function with the main logic of our program
def main():
    # ask the user for their email and password, using dedicated functions
    email = get_email()
    
    # validate the email address
    email_is_valid = validate_email(email)
    
    # output a meaningful response
    if email_is_valid:
        output_success_message()
    else:
        output_failure_message()
    
    
# call the main function
main()
