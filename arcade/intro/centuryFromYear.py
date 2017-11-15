"""
Given a year, return the century it is in. The first century spans from the year 1 up to and including the year 100, the second - from the year 101 up to and including the year 200, etc.

Example

For year = 1905, the output should be
centuryFromYear(year) = 20;
For year = 1700, the output should be
centuryFromYear(year) = 17.
"""


def centuryFromYear(year):
    listed = map(int, str(year))
    temp = listed[-4:-2]
    if temp:
        first_double = int(''.join(map(str, temp)))
    else:
        first_double = 0

    second_double = int(''.join(map(str, listed[-2:])))
    if second_double == 0:
        appendinx = 0
    else:
        appendinx = 1
    return first_double + appendinx
