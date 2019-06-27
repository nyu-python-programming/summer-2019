"""
Shows the capabilities and limitations of dictionaries

@author Foo Barstein
@date 27 June 2019
"""

# a list of values
names = [
            #values
            "bob",
            "jane",
            "cynthia",
            "henry",
            "francois"
        ]

# a dictionary with key->value pairs
words = {
            # keys    # values
            "sneeze": "A reaction...",
            "hiccup": "A muscular reflexive contraction..." 
        }


# lists can store any data type
list_of_stuff = [
                    100,
                    3.14,
                    "hello world",
                    True,
                    None,
                    [1,2,3],
                    {1: True}
        ]


# dictionary keys can be of any immutable data type
dict_of_stuff = {
                    # keys      # values
                    100:        "hello world",
                    3.14:       "hello world",
                    "foo":      "hello world",
                    True:       "hello world",
                    None:       "hello world"
                    
                    # mutable data types cannot be used as keys
                    #[1,2,3] :   "hello world",
                    #{1:True} :  "hello world"
        }

# dictionary values can be of any data type at all
dict_of_stuff = {
                    # keys      # values
                    0:          1,
                    3.14:       'hello',
                    "foo":      3.14,
                    True:       False,
                    None:       [1,2,3],
                    2:          {2: True}
                }


