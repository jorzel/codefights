"""
Easy

Codewriting

1500

You are climbing a staircase that has n steps. You can take the steps either 1 or 2 at a time. Calculate how many distinct ways you can climb to the top of the staircase.

Example

For n = 1, the output should be
climbingStairs(n) = 1;

For n = 2, the output should be
climbingStairs(n) = 2.

You can either climb 2 steps at once or climb 1 step two times.
"""

def fib(n):
    if n == 0 or n == 1:
        return n
    old, new = 0, 1
    for _ in range(n):
        old, new = new, old + new
    return new

def climbingStairs(n):
    return fib(n)

    
    

def climbingStaircase(n, k):
    if n == 0:
        return [[]]
    return climbing(n, k, [], [])