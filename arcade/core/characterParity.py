"""
Given a character, check if it represents an odd digit, an even digit or not a digit at all.

Example

For symbol = '5', the output should be
characterParity(symbol) = "odd";
For symbol = '8', the output should be
characterParity(symbol) = "even";
For symbol = 'q', the output should be
characterParity(symbol) = "not a digit".
"""


def characterParity(symbol):
    if symbol.isdigit():
        return "even" if int(symbol) % 2 == 0 else "odd"
    else:
        return "not a digit"
