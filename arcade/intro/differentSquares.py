"""
Given a rectangular matrix containing only digits, calculate the number of different 2 × 2 squares in it.

Example

For

matrix = [[1, 2, 1],
          [2, 2, 2],
          [2, 2, 2],
          [1, 2, 3],
          [2, 2, 1]]
the output should be
differentSquares(matrix) = 6.

Here are all 6 different 2 × 2 squares:

1 2
2 2
2 1
2 2
2 2
2 2
2 2
1 2
2 2
2 3
2 3
2 1
"""


def differentSquares(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    container = set()
    for i in range(rows - 1):
        for j in range(cols - 1):
            container.add((matrix[i][j], matrix[i][j + 1], matrix[i + 1][j], matrix[i + 1][j + 1])) 
    return len(container)
