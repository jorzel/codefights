"""
Easy

Recovery

100

Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
There is a great technique that allows finding sums of consecutive elements in the given array extremely fast. It is based on the usage of prefix sums. Given array a, your task is to calculate all its prefix sums.

Example

For a = [1, 2, 3], the output should be
prefSum(a) = [1, 3, 6].

Here's how the prefix sums can be calculated: [1, 1 + 2, 1 + 2 + 3] = [1, 3, 6].
"""


def prefSum(a):
    return reduce(lambda l, v: (l.append(l[-1] + v) or l), a, [0])[1:]
