#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  if len(recipe) > len(ingredients):
    return 0
  else:
    quant = []
    for i in ingredients:
      print(i, ingredients[i], recipe[i], ingredients[i]//recipe[i])
      quant.append(ingredients[i]//recipe[i])
    print(quant)
    return min(quant)

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))