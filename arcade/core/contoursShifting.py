"""
Medium

Codewriting

300

Mark got a rectangular array matrix for his birthday, and now he's thinking about all the fun things he can do with it. He likes shifting a lot, so he decides to shift all of its i-contours in a clockwise direction if i is even, and counterclockwise if i is odd.

Here is how Mark defines i-contours:

the 0-contour of a rectangular array as the union of left and right columns as well as top and bottom rows;
consider the initial matrix without the 0-contour: its 0-contour is the 1-contour of the initial matrix;
define 2-contour, 3-contour, etc. in the same manner by removing 0-contours from the obtained arrays.
Implement a function that does exactly what Mark wants to do to his matrix.

Example

For

matrix = [[ 1,  2,  3,  4],
           [ 5,  6,  7,  8],
           [ 9, 10, 11, 12],
           [13, 14, 15, 16],
           [17, 18, 19, 20]]
the output should be

contoursShifting(matrix) = [[ 5,  1,  2,  3],
                             [ 9,  7, 11,  4],
                             [13,  6, 15,  8],
                             [17, 10, 14, 12],
                             [18, 19, 20, 16]]
For matrix = [[238, 239, 240, 241, 242, 243, 244, 245]],
the output should be
contoursShifting(matrix) = [[245, 238, 239, 240, 241, 242, 243, 244]].

Note, that if a contour is represented by a 1 × n array, its center is considered to be below it.

For

matrix = [[238],
           [239],
           [240],
           [241],
           [242],
           [243],
           [244],
           [245]]
the output should be

contoursShifting(matrix) = [[245],
                             [238],
                             [239],
                             [240],
                             [241],
                             [242],
                             [243],
                             [244]]
If a contour is represented by an n × 1 array, its center is considered to be to the left of it.

"""



def get_previous_point(point, left, right, top, bottom, clockwise=1):
    dir_table = [0,0]
    x, y = point

    if y == top and x == left:
        dir_table = [0, 1] if clockwise == 1 else [1, 0]
    elif y == top and x == right:
        dir_table = [-1, 0] if clockwise == 1 else [0, 1]
    elif y == bottom and x == right:
        dir_table = [0, -1] if clockwise == 1 else [-1, 0]
    elif y == bottom and x == left:
        dir_table = [1, 0] if clockwise == 1 else [0, -1]
    else:
        if y == top:
            dir_table = [clockwise*(-1), 0]
        elif y == bottom:
            dir_table = [clockwise*1, 0]
        if x == right:
            dir_table = [0, clockwise*(-1)]
        elif x == left:
            dir_table = [0, clockwise*1]

    if top == bottom:
        dir_table = [-1, 0] if clockwise == 1 else [1, 0]
        if x == right and clockwise == -1:
            dir_table[0] = - (right - left)
    elif left == right:
        dir_table = [0, -1] if clockwise == 1 else [0, 1]
        if y == bottom and clockwise == -1:
            dir_table[1] = - (bottom - top)
    return dir_table

    
    
def contoursShifting(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    contours = (min(rows, cols) + 1) / 2

    output = [[0 for j in range(cols)] for i in range(rows)]
    for contour in range(contours):
        clockwise = -1 if contour % 2 else 1 
        for y in range(contour, rows - contour):
            for x in range(contour, cols - contour):
                if y in (contour, rows - contour - 1) or x in (contour, cols - contour - 1): 
                    dx, dy = get_previous_point((x, y),
                                              contour,
                                              cols - contour - 1,
                                              contour,
                                              rows - contour - 1,
                                              clockwise)

                    output[y][x] = matrix[y+dy][x+dx]
                    
    return output