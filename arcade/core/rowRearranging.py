"""
Medium

Codewriting

300

Given a rectangular matrix of integers, check if it is possible to rearrange its rows in such a way that all its columns become strictly increasing sequences (read from top to bottom).

Example

For

matrix = [[2, 7, 1], 
          [0, 2, 0], 
          [1, 3, 1]]
the output should be
rowsRearranging(matrix) = false;

For

matrix = [[6, 4], 
          [2, 2], 
          [4, 3]]
the output should be
rowsRearranging(matrix) = true.
"""


def rowsRearranging(matrix):
    b = sorted(matrix)
    for i in range(1, len(b)):
        _length = len(b[i])
        for j in range(_length):
            if b[i-1][j] >= b[i][j]:
                return False
    return True
