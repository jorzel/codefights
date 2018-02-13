"""
Given a rectangular matrix of characters, add a border of asterisks(*) to it.

Example

For

picture = [abc,
           ded]
the output should be

addBorder(picture) = [******,
                      *abc*
                      *ded*,
                      *****]
"""


def addBorder(picture):
    size = len(picture[0])
    result = [(size + 2) * '*']
    for line in picture:
        result.append('*{}*'.format(line))
    result.append((size + 2) * '*')
    return result
