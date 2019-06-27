"""
A somewhat practical example of using dictionaries
This is a simpler version than the code in 5.slightly_more_difficult_slightly_practical_example.py

@author Foo Barstein
@date 27 June 2019
"""

# a dictionary with student NYU Net IDs and their corresponding grades
students_grades = {
                'aa1234': 'A',
                "ab1234": "A-",
                'ff1234': 'B+',
                'gg4432': 'C'        
        }

# a flag to control the loop
keep_going = True

# keep looping as long as the flag is true
while keep_going:
    
    # ask the user for a net ID
    net_id = input('Enter the net ID of the student: ')

    # see whether the user wants to quit
    if net_id == "exit":
        # cause the loop to stop if so
        keep_going = False
        
    else:
        # look up the grade for the given Net ID
        grade = students_grades[net_id]

        # print it out
        print("{}'s grade is {}.".format(net_id, grade) )
        
        
        
        