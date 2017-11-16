"""
Given an array of integers, find the maximum possible sum you can get from one of its contiguous subarrays. The subarray from which this sum comes must contain at least 1 element.

Example

For inputArray = [-2, 2, 5, -11, 6], the output should be
arrayMaxConsecutiveSum2(inputArray) = 7.

The contiguous subarray that gives the maximum possible sum is [2, 5], with a sum of 7.
"""


def arrayMaxConsecutiveSum2(A):
    max_a = max(A)
    initial = max_a if max_a < 0 else 0
    max_ending = max_slice = initial
    for a in A:
        max_ending = max(initial, max_ending + a)
        max_slice = max(max_slice, max_ending)
    return max_slice
