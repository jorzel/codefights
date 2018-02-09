"""
Given a string consisting of lowercase English letters, find the largest square number which can be obtained by reordering the string's characters and replacing them with any digits you need (leading zeros are not allowed) where same characters always map to the same digits and different characters always map to different digits.

If there is no solution, return -1.

Example

For s = "ab", the output should be
constructSquare(s) = 81.
The largest 2-digit square number with different digits is 81.
For s = "zzz", the output should be
constructSquare(s) = -1.
There are no 3-digit square numbers with identical digits.
For s = "aba", the output should be
constructSquare(s) = 900.
It can be obtained after reordering the initial string into "baa" and replacing "a" with 0 and "b" with 9.
"""


def counter(string):
    letters = dict()
    for s in string:
        if s in letters:
            letters[s] += 1
        else:
            letters[s] = 1
    letters = letters.values()
    letters.sort()
    return letters


def constructSquare(string):
    bounds = [
        (1, 3),
        (4, 9),
        (10, 31),
        (32, 99),
        (100, 316),
        (317, 999),
        (1000, 3162),
        (3163, 9999),
        (10000, 31622),
        (31623, 99999)
    ]

    letters = counter(string)

    length = len(string)
    _range = bounds[length - 1]

    for i in reversed(range(_range[0], _range[1] + 1)):
        number = i * i
        numbers = counter(str(number))
        if numbers == letters:
            return number
    return -1
