"""
Medium

Codewriting

300

You are given a vertical box divided into equal columns. Someone dropped several stones from its top through the columns. Stones are falling straight down at a constant speed (equal for all stones) while possible (i.e. while they haven't reached the ground or they are not blocked by another motionless stone). Given the state of the box at some moment in time, find out which columns become motionless first.

Example

For

rows = ["#..##",
        ".##.#",
        ".#.##",
        "....."]
the output should be gravitation(rows) = [1, 4].

Check out the image below for better understanding:
"""


def gravitation(rows):
    memo = {}
    for i, line in enumerate(zip(*rows)):
        for element in line:
            if i not in memo and element == '#':
                memo[i] = 0
            if i in memo and element != '#':
                memo[i] += 1
        if i not in memo:
            memo[i] = 0
    _sorted = sorted(memo.items(), key=lambda x: x[1])
    return [x[0] for x in _sorted if x[1] == _sorted[0][1]]