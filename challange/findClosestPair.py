"""
Given an array of integers numbers, we'd like to find the closest pair of elements that add up to sum. Return the distance between the closest pair (absolute difference between the two indices). If there isn't a pair that adds up to sum, return -1.

Example

For numbers = [1, 0, 2, 4, 3, 0] and sum = 5 the output should be findClosestPair(numbers, sum) = 2. 1 and 4 have a sum of 5, but 2 and 3 are closer.

for numbers = [2, 3, 7] and sum = 8 the output should be findClosestPair(numbers, sum) = -1. There are no pairs that have a sum of 8.
"""

import sys
from collections import defaultdict

def get_min_distance(elements1, elements2):
    _min = sys.maxint
    distance = -1
    for el1 in elements1:
        for el2 in elements2:
            if el1 == el2:
                continue
            distance = abs(el1 - el2)
            if distance < _min:
                _min = distance
    return _min

def findClosestPair(numbers, total):
    d = defaultdict(list)
    for i, n in enumerate(numbers):
        d[n].append(i)
    min_distance = sys.maxint
    for value, indices in d.iteritems():
        complementary = total - value
        if complementary in d:
            distance = get_min_distance(indices, d[complementary])
            if distance < min_distance:
                min_distance = distance
    if min_distance == sys.maxint:
        min_distance = -1
    return min_distance