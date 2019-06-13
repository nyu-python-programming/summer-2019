#example that crawls all NYU i6 accounts and counts how many times  a given word is mentioned

import urllib.request

#get a list of all the letters
letters = "a b c d e f g h i j k l m n o p q r s t u v w x y z" .split(" ")

#get a list of all the numbers
numbers = "0 1 2 3 4 5 6 7 8 9".split(" ")

#generate all possible net ids, assuming net id is 2 letters  followed by 4 numbers
net_ids = [] #a blank list that will hold all possible net ids

#nested for loops!
for l1 in letters:
    for l2 in letters:
        for n1 in numbers:
            for n2 in numbers:
                for n3 in numbers:
                    for n4 in numbers:
                        net_id = l1 + l2 + n1 + n2 + n3 + n4
                        net_ids.append(net_id)

#debugging            
print(net_ids)

#count how many times the word "awesome" is used on i6 user  home pages
page_counter = 0
awesome_counter = 0

#loop through all net ids and scrape their i6 pages
for net_id in net_ids:

    #make an http request for the web page of this person
    f = urllib.request.urlopen("http://i6.cims.nyu.edu/~" +  net_id)

    #get the html code for this page
    html_code = f.read()

    #increment our page counter
    page_counter = page_counter + 1

    #you can now do any kind of analysis on these pages here
    if "awesome" in html_code:
        #increment the awesome counter
        awesome_counter = awesome_counter + 1

        #debugging
        print("Found an awesome on " + net_id + "'s page.")