"""
Easy

Codewriting

1000

Given a sorted integer array that does not contain any duplicates, return a summary of the number ranges it contains.

Example

For nums = [-1, 0, 1, 2, 6, 7, 9], the output should be
composeRanges(nums) = ["-1->2", "6->7", "9"].

"""



import sys

def composeRanges(nums):
    if not nums:
        return []

    _max = max(nums)
    nums.append(sys.maxint)
    
    start = nums[0]
    results = []
    
    for i in range(1, len(nums)):
        if (nums[i] - nums[i-1]) != 1:
            if start == nums[i-1]:
                results.append(str(start))
            else:
                results.append("{}->{}".format(start, nums[i-1]))
            start = nums[i]
        
    return results
