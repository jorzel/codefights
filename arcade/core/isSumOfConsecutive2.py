"""
Find the number of ways to express n as sum of some (at least two) consecutive positive integers.

Example

For n = 9, the output should be
isSumOfConsecutive2(n) = 2.

There are two ways to represent n = 9: 2 + 3 + 4 = 9 and 4 + 5 = 9.

For n = 8, the output should be
isSumOfConsecutive2(n) = 0.

There are no ways to represent n = 8.
"""


def isSumOfConsecutive2(n):
    left, right = 1, 1
    sum_, counter = 1, 0
    while left < (n / 2) + 1:
        if sum_ < n:
            right += 1
            sum_ += right

        elif sum_ > n:
            sum_ -= left
            left += 1
        else:
            counter += 1
            sum_ -= left
            left += 1
    return counter
