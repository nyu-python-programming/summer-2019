"""
Loop through a list in two different styles

@author Foo Barstein
@date 20 June 2019
"""


vegetables = ['rutabega', 'arugula', 'carrot', 'lettuce', 'cabbage', 'beets']

# do it with a for loop
for c in vegetables:
    print(c)

# do it with a while loop
i = 0
while i < len(vegetables):
    c = vegetables[i]
    print(c)
    
    i = i + 1
    
    
