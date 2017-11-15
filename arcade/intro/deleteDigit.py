"""
Given some integer, find the maximal number you can obtain by deleting exactly one digit of the given number.

Example

For n = 152, the output should be
deleteDigit(n) = 52;
For n = 1001, the output should be
deleteDigit(n) = 101.
"""


def deleteDigit(n):
    nlist = list(str(n))
    maximal = 0
    for i, d in enumerate(nlist):
        el = nlist.pop(i)
        current = int(''.join(nlist))
        nlist.insert(i, el)
        if current > maximal:
            maximal = current
    return maximal
