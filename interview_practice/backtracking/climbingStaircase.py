"""
Medium

Codewriting

3000

You need to climb a staircase that has n steps, and you decide to get some extra exercise by jumping up the steps. You can cover at most k steps in a single jump. Return all the possible sequences of jumps that you could take to climb the staircase, sorted.

Example

For n = 4 and k = 2, the output should be

climbingStaircase(n, k) =
[[1, 1, 1, 1],
 [1, 1, 2],
 [1, 2, 1],
 [2, 1, 1],
 [2, 2]]
There are 4 steps in the staircase, and you can jump up 2 or fewer steps at a time. There are 5 potential sequences in which you jump up the stairs either 2 or 1 at a time.
 """


def climbing(n, k, result, results):
    if n == 0:
        results.append(result)
    else:
        for i in range(1, k + 1):
            if n-i >= 0:
                climbing(n-i, k, result + [i], results)
    return results
    

def climbingStaircase(n, k):
    if n == 0:
        return [[]]
    return climbing(n, k, [], [])