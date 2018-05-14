"""
You're given a substring s of some cyclic string. What's the length of the smallest possible string that can be concatenated to itself many times to obtain this cyclic string?

Example

For s = "cabca", the output should be
cyclicString(s) = 3.

"cabca" is a substring of a cycle string "abcabcabcabc..." that can be obtained by concatenating "abc" to itself. Thus, the answer is 3.
"""


def cyclicString(s):
    _length = len(s)
    for i in range(1, _length + 1):
        cycle_string = _length * ''.join(s[:i])
        if s in cycle_string:
            return i

