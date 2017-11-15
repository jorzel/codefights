"""
Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.

Given a ticket number n, determine if it's lucky or not.

Example

For n = 1230, the output should be
isLucky(n) = true;
For n = 239017, the output should be
isLucky(n) = false.
"""

def get_sum(string):
    result = 0
    for s in string:
        result += int(s)
    return result

def isLucky(n):
    str_n = str(n)
    length = len(str_n)
    return get_sum(str_n[:length / 2]) == get_sum(str_n[length / 2:])
