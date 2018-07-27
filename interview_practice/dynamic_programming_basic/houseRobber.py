"""
Medium

Codewriting

3000

You are planning to rob houses on a specific street, and you know that every house on the street has a certain amount of money hidden. The only thing stopping you from robbing all of them in one night is that adjacent houses on the street have a connected security system. The system will automatically trigger an alarm if two adjacent houses are broken into on the same night.

Given a list of non-negative integers nums representing the amount of money hidden in each house, determine the maximum amount of money you can rob in one night without triggering an alarm.

Example

For nums = [1, 1, 1], the output should be
houseRobber(nums) = 2.

The optimal way to get the most money in one night is to rob the first and the third houses for a total of 2.

"""



def _houseRobber(nums, memo):
    if nums in memo:
        return memo[nums]
    elif len(nums) == 1:
        memo[nums] = nums[0]
    elif len(nums) == 2:
        memo[nums] = max(nums[0], nums[1])

    take = nums[0] + _houseRobber(nums[2:], memo)
    leave = _houseRobber(nums[1:], memo)
    memo[nums] = max(take, leave)
    return memo[nums]

def houseRobber(nums):
    memo = {(): 0}
    return _houseRobber(tuple(nums), memo)
