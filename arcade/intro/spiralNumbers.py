"""
Construct a square matrix with a size N × N containing integers from 1 to N * N in a spiral order, starting from top-left and in clockwise direction.

Example

For n = 3, the output should be

spiralNumbers(n) = [[1, 2, 3],
                    [8, 9, 4],
                    [7, 6, 5]]
"""


def spiralNumbers(n):
    N, S, W, E = (0, -1), (0, 1), (-1, 0), (1, 0)
    turn_right = {E: S, S: W, W: N, N: E}

    matrix = [[None for i in range(n)] for j in range(n)]
    x, y = 0, 0
    i = 1
    current = E

    while i <= n * n:
        if matrix[y][x] is None:
            matrix[y][x] = i
        new_x = x + current[0]
        new_y = y + current[1]
        if new_x < 0 or new_x >= n or new_y < 0 or new_y >= n or matrix[new_y][new_x] is not None:
            current = turn_right[current]
            x = x + current[0]
            y = y + current[1]
        else:
            x, y = new_x, new_y
        i += 1
    return matrix
