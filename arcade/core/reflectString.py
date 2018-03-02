"""
Define an alphabet reflection as follows: a turns into z, b turns into y, c turns into x, ..., n turns into m, m turns into n, ..., z turns into a.

Define a string reflection as the result of applying the alphabet reflection to each of its characters.

Reflect the given string.

Example

For inputString = "name", the output should be
reflectString(inputString) = "mznv".
"""


def reflectString(inputString):
    return ''.join([chr(ord('a') + (122 - ord(s))) for s in inputString])
