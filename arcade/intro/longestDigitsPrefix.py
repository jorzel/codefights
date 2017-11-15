"""
Given a string, output its longest prefix which contains only digits.

Example

For inputString="123aa1", the output should be
longestDigitsPrefix(inputString) = "123".
"""


def longestDigitsPrefix(inputString):
    max_seq = ""
    for i, el in enumerate(inputString):
        if i == 0 and not el.isdigit():
            return ""
        if el.isdigit():
            max_seq += el
        else:
            break
    return max_seq
