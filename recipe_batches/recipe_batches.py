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
---------------------------------------------------------------------------
Did not account for a way to subtract recipe values from ingredients
========================================================================


-  New Approach

- Try a while loop - while ingredients > 0 run
- take ingredients key and subtract recipe key

Carry Out Plan
--------------


"""


def recipe_batches(recipe, ingredients):
    count = 0
    done = False
    while not done:
        shortage = False
        for key in recipe.keys():
            print("ingredients key", ingredients[key])
            print("recipe key", recipe[key])

    return count


recipe_batches(
    {'milk': 100, 'butter': 50, 'flour': 5},
    {'milk': 138, 'butter': 48, 'flour': 51}
)


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
