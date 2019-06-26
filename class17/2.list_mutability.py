"""
Modifying lists ... since they're mutable, why not?

@author Foo Barstein
@date 25 June 2019
"""

# a list of groceries we intend to buy
groceries = [
                "broccoli",
                "2% milk",
                "whole wheat bread",
                "spaghetti",
                "no pulp orange juice"
            ]


# modify the second value in the list
my_least_favorite_drink = groceries[1]
my_new_favorite_drink = "almond milk"
groceries[1] = my_new_favorite_drink


