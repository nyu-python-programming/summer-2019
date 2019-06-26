"""
A program that seems to be responsive to the user and artificially mildly intelligent.... and uses lists.

@author Foo Barstein
@date 26 June 2019
"""

from datetime import *
import random

# a list of days
days = [
            'monday', 
            'tuesday', 
            'wednesday', 
            'thursday', 
            'friday',
            'saturday', 
            'sunday'
        ]

# a list of prompts
prompts = [
            "what's your favorite day of the week? ",
            "please enter a day of the week you like: ",
            "which day of the week is it? ",
            "enter a day of the week! ",
            "give me a day of the week, puleez: ",
            "enough already! Give me a day: ",
            "stop messing around.  What's the day you like? ",
            "this is the last time!  Which day of the week is it going to be?! "            
        ]

# a list of expressions of confusion
confused_responses = [
            "huh?",
            "huh? '{}'?!",
            "sorry, i didn't get that!",
            'what?',
            "what's '{}'?!",
            'come again?',
            'say what?',
            'did you say something?',
            "what do you mean by '{}'?",
            "I don't understand...",
            "I really don't understand what you mean by '{}'..."
        ]

# a list of excited responses
excited_responses = [
            "{} is so awesome!",
            "That's so funny... I also love {}s!",
            "{} - that's the right answer!",
            "Wow... {}s are my favorite too!",
            "No way!  You love {}?! Hahahah!"
        ]

# get the day of the week today
today = date.today() # returns a 'date' object
weekday_num = date.weekday(today) # conver to regular int

# find the name of the day from the list
weekday_word = days[weekday_num]

# output the day of the week
print("Today is {}.".format(weekday_word.capitalize()) )


# a flag
keep_going = True

# a counter/accumulator
prompt_index = 0

# loop as long as we don't have a good response from the user and as long as we have not run out of prompts to use
while keep_going and prompt_index < len(prompts):
        
    # ask the user for their favorite day of the week
    message = prompts[prompt_index]
    fav = input(message.capitalize() )
    
    # use the 'in' operator to check for the presence of the value in the list
    if fav.lower() in days:
        # generate a pseudo-random int that representes the index number of one of the excited responses
        num = random.randint(0, len(excited_responses) - 1)

        # format the response nicely
        response = excited_responses[num].capitalize()
        response = response.format(fav.capitalize())

        # output the response
        print("\n" + response)
        
        # set the flag to False so the loop doesn't iterate another time
        keep_going = False
        
    else:
        # generate a pseudo-random int that represents the index number of one of the confused responses
        num = random.randint(0, len(confused_responses) - 1)
        
        # format the response nicely
        response = confused_responses[num].capitalize()
        response = response.format(fav)
        
        # output the response
        print("\n" + response)
    
    # increment the accumulator
    prompt_index = prompt_index + 1


print("\nI'm done with this!")

