"""
Sudoku is a number-placement puzzle.
The objective is to fill a 9 × 9 grid with digits so that each column, each row, and each of the nine 3 × 3 sub-grids that compose the grid contains all of the digits from 1 to 9.

This algorithm should check if the given grid of numbers represents a correct solution to Sudoku.

Example

For the first example below, the output should be true. For the other grid, the output should be false: each of the nine 3 × 3 sub-grids should contain all of the digits from 1 to 9.
"""


def valid_line(line):
    a = []
    for el in line:
        if el not in a:
            a.append(int(el))
        else:
            return False
    return True


def sudoku(grid):
    n = len(grid)
    box_size = 3
    for i in xrange(0, n / box_size):
        for j in xrange(0, n / box_size):
            center = i * (n / box_size), j * (n / box_size)
            box = []
            for k in range(box_size):
                for l in range(box_size):
                    value = grid[center[0] + k][center[1] + l]
                    if value not in box:
                        box.append(value)
                    else:
                        return False
    for r in grid:
        if not valid_line(r):
            return False
    
    zipped = zip(*grid)
    for c in zipped:
        if not valid_line(c):
            return False
    return True