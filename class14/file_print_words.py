#open a text file in read mode
f = open("data.txt", "r")

#get the full text from the file
the_text = f.read()

#split the text into a List of words by space delimiters
words = the_text.split()

#loop through each word and analyze it
for word in words:
    
    # remove punctuation
    word = word.replace('.', '')
    word = word.replace(',', '')

    #print for debugging
    print(word)