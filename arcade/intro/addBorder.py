"""
Given a rectangular matrix of characters, add a border of asterisks(*) to it.

Example

For

picture = ["abc",
           "ded"]
the output should be

addBorder(picture) = ["*****",
                      "*abc*",
                      "*ded*",
                      "*****"]
"""


def addBorder(picture):
    bordered_picture = []
    length = len(picture[0])
    top_bottom = (length + 2) * '*'
    bordered_picture.append(top_bottom)
    for p in picture:
        element = '*' + p + '*'
        bordered_picture.append(element)
    bordered_picture.append(top_bottom)
    return bordered_picture
