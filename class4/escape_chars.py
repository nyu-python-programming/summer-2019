"""
File: escape_chars.py
Author: Foo Barstein
Date: 3 June 2019
"""

# eaxmple of line break escape character
x = "This\nis\na\nstring"
length_of_x = len(x)
print("The length of the string x is", length_of_x)

# example of an escape character, in this case \" renders the quote inert
y = "My favorite quote from Alan Turing is, \"The masters [programmers] are liable to get replaced because as soon as any technique becomes at all stereotyped it becomes possible to devise a system of instruction tables which will enable the electronic computer to do it for itself. It may happen however that the masters will refuse to do this. They may be unwilling to let their jobs be stolen from them in this way. In that case they would surround the whole of their work with mystery and make excuses, couched in well chosen gibberish, whenever any dangerous suggestions were made.\""

# example of a tab escape character
z = "This\tThat\tThe other"
length_of_z = len(z)
print("The length of the string z is", length_of_z)

# example of an escaped backslash
a = "My favorite character is the backslash \ character"
print(a)
b = "I love the \\n character!"
print(b)

