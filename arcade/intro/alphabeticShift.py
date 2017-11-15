"""
Given a string, replace each its character by the next one in the English alphabet (z would be replaced by a).

Example

For inputString = "crazy", the output should be
alphabeticShift(inputString) = "dsbaz".
"""

def alphabeticShift(inputString):
    output = ''
    for i, s in enumerate(inputString):
        if s == 'z':
            output += 'a'
        else:
            r = chr(ord(s) + 1)
            output += r
    return output
