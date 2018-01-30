"""
You are given two strings s and t of the same length, consisting of uppercase English letters. Your task is to find the minimum number of "replacement operations" needed to get some anagram of the string t from the string s. A replacement operation is performed by picking exactly one character from the string s and replacing it by some other character.

Example

For s = "AABAA" and t = "BBAAA", the output should be
createAnagram(s, t) = 1;
For s = "OVGHK" and t = "RPGUC", the output should be
createAnagram(s, t) = 4.
"""

def createAnagram(s, t):
    duplicates = 0
    t = list(t)
    for s1 in s:
        if s1 in t:
            duplicates += 1
            t.remove(s1)
    return len(s) - duplicates
