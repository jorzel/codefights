"""
Medium

Codewriting

2000

BONUS CHALLENGE
This challenge is a simplified version of the climbingStaircase problem from the interview practice section. @zero_cool will be solving this one first during the facebook livestream to help scaffold a discussion about recursion, memoization, dynamic programming, and backtracking.

You need to climb a staircase that has n steps, and you decide to get some extra exercise by jumping up the steps. You can cover at most k steps in a single jump. Return the number of possible sequences of jumps that you could take to climb the staircase.

Example

For n = 4 and k = 2, the output should be climbingStaircasePrequel(n, k) = 5.

There are 5 different sequences of steps you could take:

[[1, 1, 1, 1],
 [1, 1, 2],
 [1, 2, 1],
 [2, 1, 1],
 [2, 2]]
"""


def climbing(n, k, memo):
    if n == 0:
        return 1
    if n in memo:
        return memo[n]
    sum = 0
    for jump in range(1, min(k + 1, n + 1)):
        if n-jump >= 0:
            sum += climbing(n-jump, k, memo)
    memo[n] = sum
    return sum
    

def climbingStaircasePrequel(n, k):
    return climbing(n, k, {})

