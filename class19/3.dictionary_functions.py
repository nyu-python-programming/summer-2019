"""
A brief introduction to various useful dictionary functions and what they return

@author Foo Barstein
@date 27 June 2019
"""

holidays = {
            "4 July 2019": "Independence Day",
            "25 December 2019": "Christmas",
            "1 January 2020": "New Year's Day",
            "21 June 2019": "Solstice",
            "17 March 2019": "St. Patrick's Day"
        }


# get a list of the keys in the dictionary
list_of_keys = holidays.keys() # the keys function returns a list of keys
print("\nThe keys are:")
for key in list_of_keys:
    print(key)

# get a list of the values in the dictionary
list_of_values = holidays.values() # the values function returns a list of values
print("\nThe values are:")
for value in list_of_values:
    print(value)

# get a list of the key/value pairs in the dictionary
list_of_items = holidays.items() # the keys function returns a list of items, which are themselves lists containing the key/value pair
print("\nThe items are:")
for item in list_of_items:
    print(item)

# get a list of the key/value pairs in the dictionary
list_of_items = holidays.items()
print("\nThe items are:")
for item in list_of_items:
    print(item[0], "-", item[1])

# get a list of the key/value pairs in the dictionary
list_of_items = holidays.items()
print("\nThe items are:")
for key, value in list_of_items:
    print(key, "-", value)








