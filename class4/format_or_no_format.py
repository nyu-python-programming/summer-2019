"""
File: format_or_no_format.py
Author: Foo Barstein
Date: 3 June 2019
"""

word1 = "happy"
word2 = "sad"
word3 = "fuzzy"

# the "old-fashioned" way to plug variables into a string
sentence = "The " + word1  + " clown and the " + word2 + " turtle " + " emerged from the " + word3 + " paradigm"
print(sentence)

# the "fancy" way to do the same thing
sentence = "The {} clown and the {} turtle emerged from the {} paradigm".format(word1, word2, word3)
print(sentence)

# the "somewhat fancy" way to do the same thing
sentence = "The {2} clown and the {1} turtle emerged from the {0} paradigm".format(word3, word2, word1)
print(sentence)

# the "even fancier" way to do the same thing
sentence = "The {adj1} clown and the {adj2} turtle emerged from the {adj3} paradigm".format(adj2=word2, adj1=word1, adj3=word3)
print(sentence)