"""
A somewhat more difficult somewhat practical example of using dictionaries
This is an extension of teh code in 4.slightly_practical_example.py

@author Foo Barstein
@date 27 June 2019
"""

# a dictionary containing net IDs and their associated assignment grades as a list
students_grades = {
                'aa1234': [93, 22, 100, 22, 100],
                "ab1234": [93, 22, 100, 56, 100],
                'ff1234': [93, 22, 100, 56, 100],
                'gg4432': [93, 22, 100, 56, 100]        
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
        
        # check whether key exists in dictionary
        if net_id in students_grades.keys() :  
            
            # if this key exists in the dictionary, get the corresponding value
            grades_list = students_grades[net_id]
        
            # one solution to the problem of converting the list to a nice looking string...
            grades = str(grades_list) # convert list to string
            grades = grades[1: len(grades) - 1] # remove the square brackets from the beginning and end
            
            # another solution to the problem of converting the list to a nice string...
            #grades_list_as_strings = []
            #for grade in grades_list:
            #    grades_list_as_strings.append( str(grade) )
            
            # get a comma-separated string from the list
            #grades = ", ".join(grades_list_as_strings)
            
            # yet another solution to the problem of converting the list to a nice string...
            #grades = ""
            #counter = 0
            #for grade in grades_list:
            #    if counter == len(grades_list) - 1:
            #        grades = grades + str(grade)
            #    else:                  
            #        grades = grades + str(grade) + ", "
            #    
            #    counter = counter + 1
    
            # print out the grades
            print("{}'s assignment grades are {}.".format(net_id, grades) )
            
        else:
            # we did not find the key in the dictionary
            print("Sorry, didn't find a student with that Net ID.")