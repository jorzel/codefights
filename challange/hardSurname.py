"""
for commentators it is a huge trouble! It is a real challenge for them to pronounce such complicated names that they are dealing with.



Given the surname of a player, determine how hard it is to pronounce. We assume that the difficulty of the surname is the maximum number of consecutive consonants in it.

Example

For surname = "Blaszczykowski", the output should be
hardSurname(surname) = 6;
For surname = "Papastathopoulos", the output should be
hardSurname(surname) = 2.
"""

def hardSurname(n):
    v = "aeiouAEIOU"
    c, l = 0, 0
    for s in n:
        if s not in v:
            c += 1
            if c > l:
                l = c
        else:
            c = 0
    return l
