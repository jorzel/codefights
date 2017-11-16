"""
Given an array strings, determine whether it follows the sequence given in the patterns array. In other words, there should be no i and j for which strings[i] = strings[j] and patterns[i] ≠ patterns[j] or for which strings[i] ≠ strings[j] and patterns[i] = patterns[j].

Example

For strings = ["cat", "dog", "dog"] and patterns = ["a", "b", "b"], the output should be
areFollowingPatterns(strings, patterns) = true;
For strings = ["cat", "dog", "doggy"] and patterns = ["a", "b", "b"], the output should be
areFollowingPatterns(strings, patterns) = false.
"""


def areFollowingPatterns(strings, patterns):
    d = {}
    for i in range(len(strings)):
        if strings[i] not in d.keys():
            if patterns[i] in d.values():
                return False
            d[strings[i]] = patterns[i]
        else:
            if d[strings[i]] != patterns[i]:
                return False
    return True
