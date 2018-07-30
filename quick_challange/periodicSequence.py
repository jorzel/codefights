"""
Medium

Codewriting

2000

A periodic sequence s is defined as follows:

s[0], a, b and m are all given positive integers;
s[i] for i > 0 is equal to (a * s[i - 1] + b) mod m.
Find the period of s, i.e. the smallest integer T such that for each i > k (for some integer k): s[i] = s[i + T].

Example

For s0 = 11, a = 2, b = 6, and m = 12, the output should be
periodicSequence(s0, a, b, m) = 2.

The sequence would look like this: 11, 4, 2, 10, 2, 10, 2, 10, 2, 10....

For s0 = 1, a = 2, b = 3, and m = 5, the output should be
periodicSequence(s0, a, b, m) = 4.

The sequence would look like this: 1, 0, 3, 4, 1, 0, 3, 4, 1, 0, 3, 4....
"""



def periodicSequence(s0, a, b, m):
    s = [s0]
    i = 1
    memo = {}
    while True:
        value = (a * s[i-1] + b) % m
        if value not in memo:
            memo[value] = i
        else:
            return i - memo[value]

        s.append((a * s[i-1] + b) % m)
        i += 1