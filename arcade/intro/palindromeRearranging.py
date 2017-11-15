"""
You are given an array of integers. On each move you are allowed to increase exactly one of its element by one. Find the minimal number of moves required to obtain a strictly increasing sequence from the input.

Example

For inputArray = [1, 1, 1], the output should be
arrayChange(inputArray) = 3.
"""


def arrayChange(inputArray):
    moves = 0
    for i, p in enumerate(inputArray):
        if i == 0 or inputArray[i] > inputArray[i-1]:
            pass
        else:
            diff = inputArray[i-1] - inputArray[i]
            move = diff + 1
            inputArray[i] += move
            moves += move
    return moves
