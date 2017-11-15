"""
Given two strings, find the number of common characters between them.

Example

For s1 = "aabcc" and s2 = "adcaa", the output should be
commonCharacterCount(s1, s2) = 3.

Strings have 3 common characters - 2 "a"s and 1 "c".
"""


def character_counter(string):
    counter = {}
    for s in string:
        if s not in counter.keys():
            counter[s] = 1
        else:
            counter[s] += 1
    return counter

def commonCharacterCount(s1, s2):
    counter1 = character_counter(s1)
    counter2 = character_counter(s2)
    count = 0
    for c in counter1.keys():
        count1 = counter1[c]
        count2 = counter2.get(c, 0)
        count += min(count1, count2)
    return count
