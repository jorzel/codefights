"""
Let's call two integers A and B friends if each integer from the array divisors is either a divisor of both A and B or neither A nor B. If two integers are friends, they are said to be in the same clan. How many clans are the integers from 1 to k, inclusive, broken into?

Example

For divisors = [2, 3] and k = 6, the output should be
numberOfClans(divisors, k) = 4.

The numbers 1 and 5 are friends and form a clan, 2 and 4 are friends and form a clan, and 3 and 6 do not have friends and each is a clan by itself. So the numbers 1 through 6 are broken into 4 clans.
"""


def make_key(l):
    return '_'.join([str(p) for p in l])


def numberOfClans(divisors, k):
    clans = set()
    numbers = [i for i in range(1, k + 1)]
    for n in numbers:
        current = []
        for d in divisors:
            if n % d == 0:
                current.append(d)
        key = make_key(current)
        clans.add(key)
    return len(clans)
