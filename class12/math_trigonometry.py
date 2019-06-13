#import the math module
import math

#print out the value of pi, which is a variable in the math module
print( "The value of pi is {}".format(math.pi) )

#print out the value of pi, which is a variable in the math module
print( "\nThe math module's trigonometric functions expect angles to be measured in radians.")
print( "\nTo convert an angle in degrees to radians, multiply that angle by Π / 180.")

# let's say we had a 90 degree angle
degrees = 90

# convert this angle from degrees to radians
radians = degrees * math.pi / 180 

# calculate the sin
print( "\nThe sine of {}° is {}".format(degrees, math.sin(radians) ) )

# calculate the cosine
print( "\nThe cosine of {}° is {}".format(degrees, math.cos(radians) ) )

# calculate the tangent
print( "\nThe tangent of {}° is {}".format(degrees, math.tan(radians) ) )

