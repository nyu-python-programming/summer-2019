# a list of acceptable moods
list_of_good_moods = ['happy', 'sad', 'apathetic', 'angry']

# flag
got_a_good_response = False

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
        print("That's not an acceptable mood!")

print("done!")