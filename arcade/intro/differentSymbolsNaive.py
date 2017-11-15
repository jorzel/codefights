"""
Given a string, find the number of different characters in it.

Example

For s = "cabca", the output should be
differentSymbolsNaive(s) = 3.

There are 3 different characters a, b and c
"""

def differentSymbolsNaive(string):
    symbols = dict()
    for s in string:
        if s not in symbols:
            symbols[s] = 1
        else:
            symbols[s] += 1
    return len(symbols)
