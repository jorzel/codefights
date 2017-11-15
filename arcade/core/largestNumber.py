"""
Given an integer n, return the largest number that contains exactly n digits.

Example

For n = 2, the output should be
largestNumber(n) = 99.
"""


def largestNumber(n):
    ln = ''
    for i in range(n):
        ln += '9'
    return int(ln)
