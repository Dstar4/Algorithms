#!/usr/bin/python

import math

"""
Understand
-------------
- function receives a recipe {dictionary}
- function also receives all the ingredients available to us {dictionary}
- Keys are ingredient names - values are corresponding amounts
- In ingredients dictionary value represent amount available to us

- Output the maximum number of whole batches that can be made with the
- supplied recipe using the ingredients available.

Plan
-------------

- loop through recipes
- nested loop through ingredients
- check for name in ingredients list
- compare the value
- if there is enough continue, if there is not, break
- if the whole loop runs, count 1 then run it again
- when it runs out of ingredients break and return the count
- need to account for a way to subtract recipe values from ingredients

------------------------------------------------------------------------
Did not account for a way to subtract recipe values from ingredients
========================================================================


-  New Approach

- Try a while loop - while ingredients > 0 run
- take ingredients key and subtract recipe key
- if that is 0 or greater + 1 to count
-repeat loop until we get 0 or less when subtracting the key.
- Break loop with a flag if we get <= 0

Carry Out Plan
--------------


"""


def recipe_batches(recipe, ingredients):
    count = 0
    done = False
    try:
        while not done:
            shortage = False

            for key in recipe.keys():
                ingredients[key] -= recipe[key]

                if ingredients[key] == 0:
                    done = True

                elif ingredients[key] < 0:
                    done = True
                    shortage = True

            if shortage is False:
                count += 1

    except KeyError:
        pass

    return count


# recipe_batches(
#     {'milk': 100, 'butter': 50, 'flour': 5},
#     {'milk': 138, 'butter': 48, 'flour': 51}
# )

# recipe_batches({'milk': 100, 'butter': 50, 'cheese': 10},
    #    {'milk': 198, 'butter': 52, 'cheese': 10})


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'cheese': 10}
    ingredients = {'milk': 198, 'butter': 52, 'cheese': 10}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
