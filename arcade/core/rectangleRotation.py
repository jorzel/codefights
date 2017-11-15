"""
A rectangle with sides equal to even integers a and b is drawn on the Cartesian plane. Its center (the intersection point of its diagonals) coincides with the point (0, 0), but the sides of the rectangle are not parallel to the axes; instead, they are forming 45 degree angles with the axes.

How many points with integer coordinates are located inside the given rectangle (including on its sides)?

Example

For a = 6 and b = 4, the output should be
rectangleRotation(a, b) = 23.

The following picture illustrates the example, and the 23 points are marked green.
"""

import math


def rectangleRotation(a, b):
    result = 0
    max_ = 50
    for x in range(-(a + max_), a + max_):
        for y in range(-(b + max_), b + max_):
            x1 = (x + y) / math.sqrt(2)
            y1 = (y - x) / math.sqrt(2)
            if x1 < a / 2.0 and x1 > -a / 2.0 and y1 < b / 2.0 and y1 > -b / 2.0:
                result += 1
    return result
