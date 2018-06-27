"""
As part of an Instacart beta testing group, Sara is trying out a brand new feature that automatically estimates the combined cost of the items in her handwritten shopping list. Her list contains both items and their prices. All Sara has to do is snap a photo of her list with the Instacart app, and she gets a quick estimate of what everything will cost.

Sara asked for your help, so it is up to you to devise an algorithm that calculates the cost after the image is converted into plain text. All you need to do is extract all numbers from the given string items and sum them up.

Example

For items = "Doughnuts, 4; doughnuts holes, 0.08; glue, 3.4", the output should be
shoppingList(items) = 7.48;
For items = "blue suit for 24$, cape for 12.99$ & glasses for 15.70", the output should be
shoppingList(items) = 52.69.
"""


from datetime import timedelta


import re

def shoppingList(items):
    return sum([float(n) for n in re.findall("\d+\.\d+|\d+", items)])

