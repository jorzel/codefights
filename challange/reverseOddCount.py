"""
Medium

Codewriting

2000

Reverse the order of all characters in a string that occur an odd amount of times (spaces included). All other characters should remain in the same position; only odd-frequency characters are eligible to swap with each other.

Case-sensitivity is important, so for example "a" is considered different than "A" when counting character frequencies.

Example

For str = "hello world", the output should be reverseOddCount(str) = "dlrwo loleh".

example

Occurrences:
h: 1 (reverse because it occurs an odd # of times)
e: 1 (reverse because it occurs an odd # of times)
l: 3 (reverse because it occurs an odd # of times)
o: 2 (leave it in place because it occurs an even # of times)
w: 1 (reverse because it occurs an odd # of times)
r: 1 (reverse because it occurs an odd # of times)
d: 1 (reverse because it occurs an odd # of times)
"""


from collections import defaultdict

def reverseOddCount(str):
    counter = defaultdict(int)
    _length = len(str)
    for index in xrange(_length):
        counter[str[index]] += 1
    to_reverse = []
    output = list(str)   
    for index in  xrange(_length):
        if counter[str[index]] % 2:
            to_reverse.append(index)
    left = 0
    reverse_count = len(to_reverse)
    for index in to_reverse:
        output[index] = str[to_reverse[reverse_count - 1 - left]]
        left += 1
    return "".join(output)
