"""
Easy

Codewriting

1000

You are supposed to label a bunch of boxes with numbers from 0 to n, and all the labels are stored in the array arr. Unfortunately one of the labels is missing. Your task is to find it.

Example

For arr = [3, 1, 0], the output should be
missingNumber(arr) = 2.
"""


def missingNumber(arr):
    for i in range(len(arr)+1):
        if i not in arr:
            return i
