"""
Medium

Codewriting

1000

A sequence of integers is called a zigzag sequence if each of its elements is either strictly less than all its neighbors or strictly greater than all its neighbors. For example, the sequence 4 2 3 1 5 3 is a zigzag, but 7 3 5 5 2 and 3 8 6 4 5 aren't. Sequence of length 1 is also a zigzag.

For a given array of integers return the length of its longest contiguous sub-array that is a zigzag sequence.

Example

For a = [9, 8, 8, 5, 3, 5, 3, 2, 8, 6], the output should be
zigzag(a) = 4.

The longest zigzag sub-arrays are [5, 3, 5, 3] and [3, 2, 8, 6] and they both have length 4.

For a = [4, 4], the output should be
zigzag(a) = 1.

The longest zigzag sub-array is [4] - it has only one element, which is strictly greater than all its neighbors (there are none of them).

"""


def is_zigzag(a, i):
    if (a[i - 1] > a[i] and a[i + 1] > a[i]) or (a[i - 1] < a[i] and a[i + 1] < a[i]):
        return True
    return False

def zigzag(a):
    if not a:
        return 0
    if len(a) == 1:
        return 1
    if len(a) == 2:
        if a[0] != a[1]:
            return 2
        else:
            return 1
    
    _max = 2
    _current = 2
    for i in range(1, len(a) - 1):
        if is_zigzag(a, i):
            _current += 1
            if _current > _max:
                _max = _current
        else:
            _current = 2
    return _max

