"""
Two strings are called anagrams, if they contain the same characters, but the order of the characters may be different.

Given a string consisting of lowercase letters and question marks, s1, and another string consisting of lowercase letters, s2, determine whether these two strings could become anagrams by replacing each ? character in s1 with a letter.

Examples

For s1 = listen and s2 = silent, the output should be couldBeAnagram(s1, s2) = true. The letters of s1 could be rearranged to form s2.

For s1 = cat and s2 = dog, the output should be couldBeAnagram(s1, s2) = false. There's no way s2 could be formed using the letters of s1.

For s1 = n?ce and s2 = nice, the output should be couldBeAnagram(s1, s2) = true. By replacing the ? with i in s1, the two strings will have the same characters.
"""

def couldBeAnagram(s1, s2):
    if len(s1) != len(s2):
        return False
    s1_dict = {}
    for s in s1:
        if s not in s1_dict:
            s1_dict[s] = 1
        else:
            s1_dict[s] += 1
    for s in s2:
        if s in s1_dict and s1_dict[s] > 0:
            s1_dict[s] -= 1
            if s1_dict[s] == 0:
                s1_dict.pop(s)
        elif '?' in s1_dict and s1_dict['?'] > 0:
            s1_dict['?'] -= 1
            if s1_dict['?'] == 0:
                s1_dict.pop('?')
        else:
            return False
    return True if not s1_dict else False
