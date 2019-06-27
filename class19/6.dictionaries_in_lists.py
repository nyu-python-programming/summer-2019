"""
Dictionaries stored in a list...

@author Foo Barstein
@date 27 June 2019
"""

# a list full of dictionaries... note that each dictionary has the same keys
students = [
        {
           "name": "Bob Bobson",
           "net id": "bb1234",
           "email": "bb1234@nyu.edu",
           "N number": "N123456789",
           "assignment grades": [22, 56, 99, 100],
           "exam grades": [99, 55]
        },
        {
           "name": "Alice Alicesson",
           "net id": "aa1234",
           "email": "aa1234@nyu.edu",
           "N number": "N987654321",
           "assignment grades": [100, 99, 22, 56],
           "exam grades": [55, 99]
        },
        {
           "name": "Georgina R. Stoops",
           "net id": "gs9988",
           "email": "gs9988@nyu.edu",
           "N number": "N55443322",
           "assignment grades": [100, 99, 22, 56],
           "exam grades": [55, 99]
        },
        {
           "name": "Teresa J. Criswell",
           "net id": "tc774433",
           "email": "tc774433@nyu.edu",
           "N number": "N88552299",
           "assignment grades": [99, 43, 26, 78],
           "exam grades": [59, 51]
        }
]
        

# print out the names of each student
# loop through the students list... remember each value in the list is a dictionary!
for student in students:
    
    # look up the value corresponding to the 'name' key in the dictionary
    print("{} ({})".format(student['name'], student['net id']) )
        

# ask the user to enter a student's net ID
net_id = input("Please enter a student's Net ID to see their final exam grade")

# start off assuming we have not found the student we're looking for yet
found_student = False

# loop through each student dictionary in the students list
for student in students:
    
    # check whether the Net ID the user typed matches the Net ID in this dictionary
    if student['net id'] == net_id:
        
        # we found the student, so flip the flag
        found_student = True
        
        # grab the student's name
        name = student['name']
        
        # grab the student's final exam grade
        final_exam_grade = student['exam grades'][1]
        
        # print them out
        print("{} ({})'s final exam grade is {}".format(name, net_id, final_exam_grade))


# print out a special message if we never found the student
if not found_student:
    # consolation message
    print("Sorry, couldn't find the student with net id {}".format(net_id) )







        