"""
Determine if the given number is a power of some non-negative integer.

Example

For n = 125, the output should be
isPower(n) = true;
For n = 72, the output should be
isPower(n) = false.
"""

from math import sqrt


def isPower(n):
    if n == 1:
        return True
    n_sqrt = int(sqrt(n))
    for i in xrange(1, n_sqrt + 1):
        for j in xrange(2, n_sqrt + 1):
            if i ** j == n:
                return True
    return False
