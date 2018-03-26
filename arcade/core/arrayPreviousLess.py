"""
Given array of integers, for each position i, search among the previous positions for the last (from the left) position that contains a smaller value. Store this value at position i in the answer. If no such value can be found, store -1 instead.

Example

For items = [3, 5, 2, 4, 5], the output should be
arrayPreviousLess(items) = [-1, 3, -1, 2, 4].
"""


def arrayPreviousLess(items):
    results = []
    found = False
    for i, n in enumerate(items):
        if i == 0:
            results.append(-1)
            continue
        for p in reversed(items[:i]):
            if p < n:
                results.append(p)
                found = True
                break
        if not found:
            results.append(-1)
        found = False
    return results
