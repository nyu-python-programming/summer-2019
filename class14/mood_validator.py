"""
Ask the user to enter their mood, and check whether it is one of our accepted moods.

@author Foo Barstein
@date 19 June 2019
"""

# a list of acceptable moods
list_of_good_moods = ['happy', 'sad', 'apathetic', 'angry']

# flag that keeps track of whether the mood the user entered is acceptable or not yet
got_a_good_response = False

# keep looping as long as the user has not entered an acceptable mood yet
while not got_a_good_response:
    
    # ask the user for their mood
    mood = input("What's your mood today?")
    
    # check whether what the user entered is one of our acceptable moods
    if mood in list_of_good_moods:
        # it's good!
        print("That's an acceptable mood!")
        
        # set flag to true, since we now have a good response
        got_a_good_response = True
        
    else:
        # the user did not enter one of our accepted moods
        print("That's not an acceptable mood!")
        
# the loop has completed by this point of the code
print("done!")