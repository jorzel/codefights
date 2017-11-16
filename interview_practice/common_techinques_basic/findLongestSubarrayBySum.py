"""
You have an unsorted array arr of non-negative integers and a number s. Find a longest contiguous subarray in arr that has a sum equal to s. Return two integers that represent its inclusive bounds. If there are several possible answers, return the one with the smallest left bound. If there are no answers, return [-1].

Your answer should be 1-based, meaning that the first position of the array is 1 instead of 0.

Example

For s = 12 and arr = [1, 2, 3, 7, 5], the output should be
findLongestSubarrayBySum(s, arr) = [2, 4].

The sum of elements from the 2nd position to the 4th position (1-based) is equal to 12: 2 + 3 + 7.

For s = 15 and arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], the output should be
findLongestSubarrayBySum(s, arr) = [1, 5].

The sum of elements from the 1st position to the 5th position (1-based) is equal to 15: 1 + 2 + 3 + 4 + 5.

For s = 15 and arr = [1, 2, 3, 4, 5, 0, 0, 0, 6, 7, 8, 9, 10], the output should be
findLongestSubarrayBySum(s, arr) = [1, 8].

The sum of elements from the 1st position to the 8th position (1-based) is equal to 15: 1 + 2 + 3 + 4 + 5 + 0 + 0 + 0.
"""


def prefix_sums(A):
    n = len(A)
    P = [0] * (n + 1)
    for i in xrange(1, n + 1):
        P[i] = P[i - 1] + A[i - 1]
    return P

def findLongestSubarrayBySum(s, A):
    P = prefix_sums(A)
    left, right, total = 0, 0, 0
    longest = -1
    ind = [-1]

    flag = False
    if len(A) == 1:
        if A[0] == s:
            return [1, 1]
        else:
            return [-1]
    while right < len(A) - 1:
        while right < len(A) - 1:
            if total >= s:
                if right + 1 < len(A) and A[right+1] == 0:
                    pass
                else:
                    flag = True
                    break
            right += 1
            total = P[right+1] - P[left]
        while total >= s and left <= right:
            flag = False
            if total == s:
                if right - left >= longest:
                    longest = right - left
                    ind = [left+1, right+1]
            left += 1
            total = P[right+1] - P[left]
        if flag:
            break
    return ind
