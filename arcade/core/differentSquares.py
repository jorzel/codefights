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
    if rows == 0:
        return 0
    cols = len(matrix[0])

    unique = []
    for r in range(rows - 1):
        for c in range(cols - 1):
            square = (matrix[r][c],
                      matrix[r + 1][c],
                      matrix[r][c + 1],
                      matrix[r + 1][c + 1])
            if square not in unique:
                unique.append(square)
    return len(unique)
