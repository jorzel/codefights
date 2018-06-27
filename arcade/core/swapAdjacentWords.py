"""
You are given a string consisting of words separated by whitespace characters, where the words consist only of Latin letters. Your task is to swap pairs of consecutive words and return the result.

Example

For s = "CodeFight On", the output should be
swapAdjacentWords(s) = "On CodeFight";
For s = "How are you today guys", the output should be
swapAdjacentWords(s) = "are How today you guys".
"""

import re

def swapAdjacentWords(s):
    return re.sub(r'(\w+)(\W+)(\w+)', r'\3\2\1', s)
