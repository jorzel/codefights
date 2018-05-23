"""
Consider a (2k+1) × (2k+1) square subarray of an integer integers matrix. Let's call the union of the square's two longest diagonals, middle column and middle row a star. Given the coordinates of the star's center in the matrix and its width, rotate it 45 · t degrees clockwise preserving position of all matrix elements that do not belong to the star.

Example

For

matrix = [[1, 0, 0, 2, 0, 0, 3],
          [0, 1, 0, 2, 0, 3, 0],
          [0, 0, 1, 2, 3, 0, 0],
          [8, 8, 8, 9, 4, 4, 4],
          [0, 0, 7, 6, 5, 0, 0],
          [0, 7, 0, 6, 0, 5, 0],
          [7, 0, 0, 6, 0, 0, 5]]
width = 7, center = [3, 3] and t = 1, the output should be

starRotation(matrix, width, center, t) = [[8, 0, 0, 1, 0, 0, 2],
                                          [0, 8, 0, 1, 0, 2, 0],
                                          [0, 0, 8, 1, 2, 0, 0],
                                          [7, 7, 7, 9, 3, 3, 3],
                                          [0, 0, 6, 5, 4, 0, 0],
                                          [0, 6, 0, 5, 0, 4, 0],
                                          [6, 0, 0, 5, 0, 0, 4]]
For

matrix = [[1, 0, 0, 2, 0, 0, 3],
          [0, 1, 0, 2, 0, 3, 0],
          [0, 0, 1, 2, 3, 0, 0],
          [8, 8, 8, 9, 4, 4, 4],
          [0, 0, 7, 6, 5, 0, 0]]
width = 3, center = [1, 5] and t = 81, the output should be

starRotation(matrix, width, center, t) = [[1, 0, 0, 2, 0, 0, 0],
                                          [0, 1, 0, 2, 3, 3, 3],
                                          [0, 0, 1, 2, 0, 0, 0],
                                          [8, 8, 8, 9, 4, 4, 4],
                                          [0, 0, 7, 6, 5, 0, 0]]
"""

import copy

def get_positions(center, width, i):
    return [
        (center[1] - width / 2 + i, center[0] - width / 2 + i),
        (center[1], center[0] - width / 2 + i),
        (center[1] + width / 2 - i, center[0] - width / 2 + i),
        (center[1] + width / 2 - i, center[0]),
        (center[1] + width / 2 - i, center[0] + width / 2 - i),
        (center[1], center[0] + width / 2 - i),
        (center[1] - width / 2 + i, center[0] + width / 2 - i),
        (center[1] - width / 2 + i, center[0])
    ]


def starRotation(matrix, width, center, t):
    freq = 8
    t = t % freq
    start_y, start_x = center[0] - width / 2, center[1] - width / 2
    output = copy.deepcopy(matrix)
    for iy in range(center[0] + 1 - start_y):   
        for ix in range(center[1] + 1 - start_x):
            if ix == iy:
                positions = get_positions(center, width, ix)
                for position in positions:
                    index = positions.index(position)
                    new_index = (index + t) % freq
                    new_position = positions[new_index]
                    output[new_position[1]][new_position[0]] = matrix[position[1]][position[0]]
            ix += 1
        iy += 1
    return output
