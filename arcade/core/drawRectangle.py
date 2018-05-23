"""
You are implementing a command-line version of the Paint app. Since the command line doesn't support colors, you are using different characters to represent pixels. Your current goal is to support rectangle x1 y1 x2 y2 operation, which draws a rectangle that has an upper left corner at (x1, y1) and a lower right corner at (x2, y2). Here the x-axis points from left to right, and the y-axis points from top to bottom.

Given the initial canvas state and the array that represents the coordinates of the two corners, return the canvas state after the operation is applied. For the details about how rectangles are painted, see the example.

Example

For

canvas = [['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
          ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
          ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
          ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
          ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']]
and rectangle = [1, 1, 4, 3], the output should be


drawRectangle(canvas, rectangle) = [['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
                                    ['a', '*', '-', '-', '*', 'a', 'a', 'a'],
                                    ['a', '|', 'a', 'a', '|', 'a', 'a', 'a'],
                                    ['b', '*', '-', '-', '*', 'b', 'b', 'b'],
                                    ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']]
Note that rectangle sides are depicted as -s and |s, asterisks (*) stand for its corners and all of the other "pixels" remain the same. Color in the example is used only for illustration.
"""

def drawRectangle(canvas, rectangle):
    lt = rectangle[0], rectangle[1]
    rt = rectangle[2], rectangle[1]
    lb = rectangle[0], rectangle[3]
    rb = rectangle[2], rectangle[3]
    for row in range(lt[1], lb[1] + 1):
        for col in range(lt[0], rt[0] + 1):
            if (col, row) in [lt, rt, lb, rb]:
                canvas[row][col] = '*'
            elif row in (lt[1], lb[1]):
                canvas[row][col] = '-'
            elif col in (lt[0], rt[0]):
                canvas[row][col] = '|'
    return canvas