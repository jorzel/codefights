"""
Given an array of strings, return another array containing all of its longest strings.

Example

For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
allLongestStrings(inputArray) = ["aba", "vcd", "aba"].
"""


def sort_on_second_attr(a, b):
    return cmp(a[1], b[1])

def allLongestStrings(inputArray):
    array = [(i, len(string)) for i, string in enumerate(inputArray)]
    array.sort(sort_on_second_attr, reverse=True)
    max_value = array[0][1]
    max_indexes = [el[0] for el in array if el[1] == max_value]
    return [string for i, string in enumerate(inputArray) if i in max_indexes]
