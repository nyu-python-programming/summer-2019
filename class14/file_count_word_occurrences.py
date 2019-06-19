#open a text file in read mode
f = open("data.txt", "r")

# this is the search term we will be looking for in the file
search_term = "cowbells"

# start with the counter set to zero
counter = 0

#get the full text from the file
the_text = f.read()

#split the text into a List of words by space delimiters
words = the_text.split()

#loop through each word and analyze it
for word in words:
    
    # remove punctuation
    word = word.replace('.', '')
    word = word.replace(',', '')
    
    if word == search_term:
        counter = counter + 1

    #print for debugging
    #print(word)

# determine whether to print 'times' plural or not
times = "times"
if counter == 1:
    # if it's only occurring once, we use the singular
    times = "time"
    
print("Found the word, {} {} {}!".format(search_term, counter, times) ) 




