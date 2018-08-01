"""
Medium

Codewriting

300

You have a rectangular white board with some black cells. The black cells create a connected black figure, i.e. it is possible to get from any black cell to any other one through connected adjacent (sharing a common side) black cells.

Find the perimeter of the black figure assuming that a single cell has unit length.

It's guaranteed that there is at least one black cell on the table.

Example

For

matrix = [[false, true,  true ],
          [true,  true,  false],
          [true,  false, false]]
the output should be
polygonPerimeter(matrix) = 12.



For

matrix = [[true, true,  true],
          [true, false, true],
          [true, true,  true]]
the output should be
polygonPerimeter(matrix) = 16.
"""


def open_sides(x, y, matrix, width, height):
    result = 0
    if x - 1 < 0 or x + 1 == width:
        result += 1
    if y - 1 < 0 or y + 1 == height:
        result += 1
    if x - 1 >= 0 and matrix[y][x-1] == False:
        result += 1
    if x + 1 < width and matrix[y][x+1] == False:
        result += 1
    if y - 1 >= 0 and matrix[y-1][x] == False:
        result += 1
    if y + 1 < height and matrix[y+1][x] == False:
        result += 1
    return result

def polygonPerimeter(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    perimeter = 0
    for y in range(rows):
        for x in range(cols):
            if matrix[y][x] == True:
                perimeter += open_sides(x, y, matrix, cols, rows)
    return perimeter
    