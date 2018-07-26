"""
Medium

Codewriting

1000

Given an integer size, return an array containing each integer from 1 to size in the following order:

1, size, 2, size - 1, 3, size - 2, 4, ...

Example

For size = 7, the output should be
constructArray(size) = [1, 7, 2, 6, 3, 5, 4].



"""


def constructArray(size):
    arr = [i for i in range(1, size + 1)]
    results = []
    for i in range(size):
        if i % 2:
            results.append(arr.pop())
        else:
            results.append(arr.pop(0))
    return results
