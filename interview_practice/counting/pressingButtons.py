"""
Easy

Codewriting

2000

Given a string of digits, return all of the possible non-empty letter combinations that the number could represent. The mapping of digits to letters is the same as you would find on a telephone's buttons, as in the example below:



The resulting array should be sorted lexicographically.

Example

For buttons = "42", the output should be
pressingButtons(buttons) = ["ga", "gb", "gc", "ha", "hb", "hc", "ia", "ib", "ic"].
"""


from itertools import product

def pressingButtons(buttons):
    if not buttons:
        return []

    table = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'      
    }
    
    return [''.join(p) for p in list(product(*[table[b] for b in buttons]))]