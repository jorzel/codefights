"""
Given an array of strings, return another array containing all of its longest strings.

Example

For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
allLongestStrings(inputArray) = ["aba", "vcd", "aba"].
"""


def allLongestStrings(inputArray):
    max_length = 0
    for s in inputArray:
        length = len(s)
        if length > max_length:
            max_length = length
    return [s for s in inputArray if len(s) == max_length]
