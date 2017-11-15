"""
Let's define digit degree of some positive integer as the number of times we need to replace this number with the sum of its digits until we get to a one digit number.

Given an integer, find its digit degree.

Example

For n = 5, the output should be
digitDegree(n) = 0;
For n = 100, the output should be
digitDegree(n) = 1.
1 + 0 + 0 = 1.
For n = 91, the output should be
digitDegree(n) = 2.
9 + 1 = 10 -> 1 + 0 = 1.
"""


"""
Let's define digit degree of some positive integer as the number of times we need to replace this number with the sum of its digits until we get to a one digit number.

Given an integer, find its digit degree.

Example

For n = 5, the output should be
digitDegree(n) = 0;
For n = 100, the output should be
digitDegree(n) = 1.
1 + 0 + 0 = 1.
For n = 91, the output should be
digitDegree(n) = 2.
9 + 1 = 10 -> 1 + 0 = 1.
"""


def sum_number(n):
    number_list = [int(i) for i in str(n)]
    return sum(number_list)

def len_number(n):
    number_list = [int(i) for i in str(n)]
    return len(number_list)

def digitDegree(n):
    if n < 10:
        return 0
    times = 0
    length = 2
    while length > 1:
        n = sum_number(n)
        length = len_number(n)
        times += 1
    return times