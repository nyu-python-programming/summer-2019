#open a text file in read mode
f = open("mydata.txt", "r")

#get the full text from the file
the_text = f.read()

#split the text into a List of words by space delimiters
words = the_text.split()

#what word are we looking for?
term = "persimon"

#keep a counter of how many times we found the word that we're looking for
counter = 0

#loop through each word and analyze it
for word in words:

    #check whether the word matches our searchTerm (case-insensitive)
    if word.lower() == term.lower():

        #if so, increment the counter
        counter = counter + 1

#print out the result
print("We found the word", term, counter, "times.")