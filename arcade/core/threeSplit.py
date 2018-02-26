"""
You have a long strip of paper with integers written on it in a single line from left to right. You wish to cut the paper into exactly three pieces such that each piece contains at least one integer and the sum of the integers in each piece is the same. You cannot cut through a number, i.e. each initial number will unambiguously belong to one of the pieces after cutting. How many ways can you do it?

It is guaranteed that the sum of all elements in the array is divisible by 3.

Example

For a = [0, -1, 0, -1, 0, -1], the output should be
threeSplit(a) = 4.

Here are all possible ways:

[0, -1] [0, -1] [0, -1]
[0, -1] [0, -1, 0] [-1]
[0, -1, 0] [-1, 0] [-1]
[0, -1, 0] [-1] [0, -1]
"""


def prefix_sums(A):
    n = len(A)
    P = [0] * (n + 1)
    for k in xrange(1, n + 1):
        P[k] = P[k - 1] + A[k - 1]
    return P

def count_total(P, x, y):
    return P[y + 1] - P[x]

def threeSplit(a):
    P = prefix_sums(a)
    part_sum = sum(a) / 3
    added = set()

    length = len(a)
    for left in range(1, length - 1):
        l = count_total(P, 0, left - 1)
        right = left + 1
        while l == part_sum and right <= length - 1:
            m, r = count_total(P, left, right - 1), count_total(P, right, length - 1)
            if l == m == r:
                added.add((left, right))
            right += 1
    return len(added)
