"""
A program that determines the weather and recommends whether to wear a jacket.

Created on Wed Jun  5 10:51:54 2019

@author: Foo Barstein
"""

#this will be on the exam!!!!
#not exactly, but in spirit

temp = input("What's the temperature (e.g. 35)?")
precipitation = input("What sort of precipitation is there, if any?")

#rainjacket - precipitation: rain, drizzle temp: 5F - 60F
#rainjacket - precipitation: sleet, hail; temp: 32F - ?
#winter jacket - precipitation: snow, hail, sleet; temp: 0 - 32F
#winter jacket - precipitation: clear, none; temp <=32F
#no jacket - precipitation: clear, none; temp: 60F - ?

temp = int(temp) # convert to int

precipitation = precipitation.lower() # convert to lowercase

if (precipitation.find("rain") >= 0 or precipitation.find("drizz") >= 0 ) and (temp >=5 and temp  <= 60) :
    print("Wear a rain jacket, please!")
elif precipitation.find("rain") >= 0 :
    print("Wear a breathable rain jacket, please, but stay cool!")
elif (precipitation.find("sleet") >= 0 or precipitation.find("hail") >= 0) and (temp >= 32):
    print("Wear a rain jacket, please!")
elif (precipitation.find("snow") >= 0 or precipitation.find("sleet") >= 0 or precipitation.find("hail") >= 0) and (temp >=0 and temp <=32):
    print("Wear a Canada Goose winter jacket, please!")

elif (precipitation.find("clear") >= 0 or precipitation.find("none") >= 0) and (temp <=32):
    print("Wear a North Face jacket.")
          
elif (precipitation.find("clear") >= 0 or precipitation.find("none") >= 0) and (temp >=60):
    print("Don't wear a jacket")

else:
    #catch-all... be sure that you have accounted for all other conditions
    print("Please dress at your best judgment.")