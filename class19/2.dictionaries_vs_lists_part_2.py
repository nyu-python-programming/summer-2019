"""
Dictionaries compared to lists some more

@author Foo Barstein
@date 27 June 2019
"""

### LISTS ###

# lists can store a bunch of related data bundled together 
bob = [
       "Bob Bobson",
       "bb1234",
       "bb1234@nyu.edu",
       "N123456789",
       [22, 56, 99, 100],
       [99, 55]
       ]

# ge the assignment scores from the list... note the use of an index number
assignment_scores = bob[4]

# get the second value from the assignment scores list
second_assignment_grade = assignment_scores[1]

# print it
print(second_assignment_grade)



### DICTIONARIES ###

# dictionaries can also store a bunch of related data bundled together
# dictionaries are more intuitive for some uses, since they can include labels on the data
bob = {
           "name": "Bob Bobson",
           "net id": "bb1234",
           "email": "bb1234@nyu.edu",
           "N number": "N123456789",
           "assignment grades": [22, 56, 99, 100],
           "exam grades": [99, 55]
        }

# ge the assignment scores from the dictionary... note the use of the key
assignment_scores = bob["assignment grades"]

# get the second value from the assignment scores list
second_assignment_grade = assignment_scores[1]

# print it
print(second_assignment_grade)





