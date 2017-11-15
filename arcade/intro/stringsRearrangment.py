"""
Given an array of equal-length strings, check if it is possible to rearrange the strings in such a way that after the rearrangement the strings at consecutive positions would differ by exactly one character.

Example

For inputArray = ["aba", "bbb", "bab"], the output should be
stringsRearrangement(inputArray) = false;

All rearrangements don't satisfy the description condition.

For inputArray = ["ab", "bb", "aa"], the output should be
stringsRearrangement(inputArray) = true.

Strings can be rearranged in the following way: "aa", "ab", "bb"
"""


from itertools import permutations

def check_similarity(s1, s2):
    count = 0
    for i, s in enumerate(s1):
        if (s1[i] != s2[i]):
            count += 1
    return count == 1

def stringsRearrangement(inputArray):
    permutation_list = list(permutations(inputArray))
    feasible = []
    for perm in permutation_list:
        for i in xrange(1, len(perm)):
            flag = True
            if not check_similarity(perm[i - 1], perm[i]):
                flag = False
                break
        if flag:
            feasible.append(1)
        else:
            feasible.append(0)
    return sum(feasible)

