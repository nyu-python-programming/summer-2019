"""
Repeat a print statement 5 times, in various styles

@author Foo Barstein
@date 20 June 2019
"""

### the old-fashioned way
print('Mudslide!!!')
print('Mudslide!!!')
print('Mudslide!!!')
print('Mudslide!!!')
print('Mudslide!!!')


### for loop style
for m in range(0, 5, 1):
    print('Mudslide!!!')


### while loop style
i = 0
while i < 5:
    print('Mudslide!!!')
    i = i + 1
    
    
print('done')

