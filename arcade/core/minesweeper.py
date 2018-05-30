"""
In the popular Minesweeper game you have a board with some mines and those cells that don't contain a mine have a number in it that indicates the total number of mines in the neighboring cells. Starting off with some arrangement of mines we want to create a Minesweeper game setup.

Example

For

matrix = [[true, false, false],
          [false, true, false],
          [false, false, false]]
the output should be

minesweeper(matrix) = [[1, 2, 1],
                       [2, 1, 1],
                       [1, 1, 1]]   
"""


def get_direction_table(i, depth):
    if i == 0:
        dir_table = [0, 1]
    elif i == depth:
        dir_table = [-1, 0]
    else:
        dir_table = [-1, 0, 1]
    return dir_table
   

def minesweeper(matrix):
    M = matrix
    rows = len(M)
    cols = len(M[0])
    box = list()

    for i in range(rows):
        box_row = list()
        x_direction_table = get_direction_table(i, rows - 1)
        for j in range(cols):
            y_direction_table = get_direction_table(j, cols - 1)
            bombs_number = 0
            for x in x_direction_table:
                for y in y_direction_table:
                    if y == 0 and x == 0:
                        continue
                    if M[i + x][j + y]:
                        bombs_number += 1
            box_row.append(bombs_number)
        box.append(box_row)
    return box
