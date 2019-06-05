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

temp = int(temp)

if (precipitation == "rain" or precipitation == "drizzle") and (temp >=5 and temp  <= 60) :
    print("Wear a rain jacket, please!")

elif (precipitation == "sleet" or precipitation == "hail") and (temp >= 32):
    print("Wear a rain jacket, please!")

elif (precipitation == "snow" or precipitation == "sleet" or precipitation ==  "hail") and (temp >=0 and temp <=32):
    print("Wear a Canada Goose winter jacket, please!")

elif (precipitation == "clear" or precipitation == "none") and (temp <=32):
    print("Wear a North Face jacket.")
          
elif (precipitation == "clear" or precipitation == "none") and (temp >=60):
    print("Don't wear a jacket")

else:
    #catch-all... be sure that you have accounted for all other conditions
    print("Please dress at your best judgment.")