"""
Given a position of a knight on the standard chessboard, find the number of different moves the knight can perform.

The knight can move to a square that is two squares horizontally and one square vertically, or two squares vertically and one square horizontally away from it. The complete move therefore looks like the letter L. Check out the image below to see all valid moves for a knight piece that is placed on one of the central squares.

Example

For cell = "a1", the output should be
chessKnight(cell) = 2.


For cell = "c2", the output should be
chessKnight(cell) = 6.
"""

from itertools import product


def moves():
    """ The available (relative) moves"""
    a = list(product((1, -1), (2, -2)))
    return a + [tuple(reversed(m)) for m in a]


def chessKnight(cell):
    fields = 0
    for c in moves():
        x, y = ord(cell[0]) + c[0], int(cell[1]) + c[1]
        if (x > 96 and x < 105) and (y > 0 and y < 9):
            fields += 1
    return fields
