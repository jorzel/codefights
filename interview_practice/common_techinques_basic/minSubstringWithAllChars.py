"""
You have two strings, s and t. The string t contains only unique elements. Find and return the minimum consecutive substring of s that contains all of the elements from t.

It's guaranteed that the answer exists. If there are several answers, return the one which starts from the smallest index.

Example

For s = "adobecodebanc" and t = "abc", the output should be
minSubstringWithAllChars(s, t) = "banc".
"""


def all_in(substring, t):
    return all([s in substring for s in t])


def minSubstringWithAllChars(string, t):
    left, right = 0, 0
    min_string = ""
    if string == "" or t == "":
        return min_string

    while right < len(string) + 1:
        slice_ = string[left:right]
        if all([s in slice_ for s in t]):
            if not min_string:
                min_string = slice_
            else:
                if len(slice_) < len(min_string):
                    min_string = slice_
            left = left + 1
        else:
            right = right + 1
    return min_string
