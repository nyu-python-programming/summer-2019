"""
A little puzzle of a program that uses flags, boolean conditional, and functions to determine job suitability.

Created on Wed Jun  5 10:51:54 2019

@author: Foo Barstein
"""

def doCashierStuff():
    #this is where you would put cashier questions
    print("Welcome to the cashier application center")

def doBusBoyStuff():
    #this is where you would put bus boy questions
    print("Welcome to the bus boy application center")

def doManagementStuff():
    #this is where you would put management questions
    print("Welcome to the management application center")

        
def doFryCookStuff():
    yearsExperience = input("How many years food-related experience do you have? ")
    age = input("How old are you? ")
    hasFoodCert = input("Do you have a food-handling certificate? ")
    agreesToGiveAwayRights = input("Do you agree to sign away your right to litigate against us? ")

    isValidCandidate = True
    isExcellentCandidate = False
    
    if isValidCandidate and hasFoodCert.lower() != "yes":
        print("Your chances are not so great because of the high level of competition for fry cooks these days.  Please consider a job as a cashier instead.")
        agreesToGetCert = input("Do you promise to obtain legal food handling certification within 2 weeks?")
        if agreesToGetCert.lower() != "yes":
            print("Your application has been withdrawn.  Good luck!")
            isValidCandidate = False
        else:
            print("Great, thanks for being cooperative.")

    if isValidCandidate and int(age) < 16:
        print("Sorry, you're too young... You may want to consider working as a bus boy.")
        isValidCandidate = False
        print("Sending you to the bus boy application process...")
        doBusBoyStuff()

    if isValidCandidate and int(yearsExperience) <= 1:
        #warn them about their chances
        print("Your chances, frankly speaking, are not great.")
        #follow-up questions
        hasOtherRelevantExperience = input("Do you have other relevant experience?")
        otherExperience = input("Oh, what other experience do you have?")
        if hasOtherRelevantExperience.lower() != "yes":
            print("Sorry, we're looking for people with more experience than you can offer.")
            isValidCandidate = False

    elif isValidCandidate and int(yearsExperience) <= 5:
        #they are a good candidate
        #encourage them
        print("You sound like a great candidate for fry cook.")        
        #ask follow-up questions
        willingToWorkOvertime = input("Are you willing to work overtime, if necessary?")
        if willingToWorkOvertime.lower() == "yes":
            print("Great, that will help you a lot!")
            isExcellentCandidate = True

    elif isValidCandidate:        
        #these people are over qualified
        #be suspicious about their motivation taking such a job
        print("Why would you want to take such a job, given your vast experience?")
        print("Sorry, we have many more appropriate candidates... consider moving into management.")

        interestedInManagement = input("Would you like me to refer you to the management recruiting process?")
        if interestedInManagement.lower() == "yes":
            doManagementStuff()

    if isValidCandidate:
        print("Great, thanks for speaking with us... we'll get back to you shortly about this job.")
        


#start
#output welcome message
print("Welcome to the job self-evaluation tool")

#ask user for job title
jobTitle = input("Please enter the job you're interested in: ")

#if job is fry cook, then do this first branch
if jobTitle == "fry cook":
    #do the fry-cook stuff
    doFryCookStuff()
    
elif jobTitle == "cashier":
    #do the cashier-relted stuff
    doCashierStuff()
else:
    #do default stuff
	#don't worry about this for now
    print("coming soon...")