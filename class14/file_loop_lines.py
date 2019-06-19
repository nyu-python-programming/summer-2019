#open a text file in read mode
f = open("mydata.txt", "r")

#loop through each line in the file, one by one
for line in f:

    #remove the line break from the end of the string
    line = line.rstrip()

    #print out the line
    print(line)