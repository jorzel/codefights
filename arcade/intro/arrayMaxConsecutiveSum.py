"""
Given array of integers, find the maximal possible sum of some of its k consecutive elements.

Example

For inputArray = [2, 3, 5, 1, 6] and k = 2, the output should be
arrayMaxConsecutiveSum(inputArray, k) = 8.
All possible sums of 2 consecutive elements are:

2 + 3 = 5;
3 + 5 = 8;
5 + 1 = 6;
1 + 6 = 7.
Thus, the answer is 8.
"""

def arrayMaxConsecutiveSum(inputArray, k):
    max_sum = 0
    for i in range(k):
        max_sum += inputArray[i]

    current_sum = max_sum
    for i in xrange(k, len(inputArray)):
        current_sum = current_sum + inputArray[i] - inputArray[i-k]
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum


