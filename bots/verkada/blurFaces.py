"""
You are given an image, represented as a matrix of integers, where each integer corresponds to a color. The number in the ith (0-based) row and jth (0-based) column represents the color of the pixel in the ith row and jth column of the image.

Your task is to blur the image. In order to do that, you need to replace each number of the matrix with the average of the numbers in the neighboring cells. We assume that two cells are neighbors if they share at least one corner. The cell itself is not considered part of the average; only the 8 surrounding neighbors (or fewer if the cell is against an edge).

Example

For img = [[1, 4], [7, 10]], the output should be blurFaces(img) = [[7, 6], [5, 4]].

newImg[0][0] = (4 + 7 + 10) / 3 = 21 / 3 = 7
newImg[0][1] = (1 + 7 + 10) / 3 = 18 / 3 = 6
newImg[1][0] = (1 + 4 + 10) / 3 = 15 / 3 = 5
newImg[1][1] = (1 + 4 + 7) / 3 = 12 / 3 = 4
For img = [[3, 0, 2, 5], [1, 2, 3, 4], [2, 3, 2, 3]], the output should be blurFaces(img) = [[1, 2.2, 2.8, 3], [2, 2, 2.625, 3], [2, 2, 3, 3]].

newImg[0][0] = (0 + 1 + 2) / 3 = 3 / 3 = 1
newImg[0][1] = (1 + 2 + 2 + 3 + 3) / 5 = 11 / 5 = 2.2
newImg[0][2] = (0 + 2 + 3 + 4 + 5) / 5 = 14 / 5 = 2.8
newImg[0][3] = (2 + 3 + 4) / 3 = 9 / 3 = 3
newImg[1][0] = (0 + 2 + 2 + 3 + 3) / 5 = 10 / 5 = 2
newImg[1][1] = (0 + 1 + 2 + 2 + 2 + 3 + 3 + 3) / 8 = 16 / 8 = 2
newImg[1][2] = (0 + 2 + 2 + 2 + 3 + 3 + 4 + 5) / 8 = 21 / 8 = 2.625
newImg[1][3] = (2 + 2 + 3 + 3 + 5) / 5 = 15 / 5 = 3
newImg[2][0] = (1 + 2 + 3) / 3 = 6 / 3 = 2
newImg[2][1] = (1 + 2 + 2 + 2 + 3) / 5 = 10 / 5 = 2
newImg[2][2] = (2 + 3 + 3 + 3 + 4) / 5 = 15 / 5 = 3
newImg[2][3] = (2 + 3 + 4) / 3 = 9 / 3 = 3
"""

def blurFaces(img):
    rows = len(img)
    cols = len(img[0])
    new_img = res = [ [ 0 for i in range(cols) ] for j in range(rows) ]
    for i in range(rows):
        for j in range(cols):
            neigbours = []
            for dx, dy in [(-1, -1), (0, -1),  (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]:
                if 0 <=  i + dx < rows and 0 <= j + dy < cols:
                    neigbours.append(img[i + dx][j + dy])
            new_img[i][j] = float(sum(neigbours)) / len(neigbours)
    return new_img