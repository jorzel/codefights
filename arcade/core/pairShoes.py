"""
Yesterday you found some shoes in the back of your closet. Each shoe is described by two values:

type indicates if it's a left or a right shoe;
size is the size of the shoe.
Your task is to check whether it is possible to pair the shoes you found in such a way that each pair consists of a right and a left shoe of an equal size.

Example

For

shoes = [[0, 21], 
         [1, 23], 
         [1, 21], 
         [0, 23]]
the output should be
pairOfShoes(shoes) = true;

For

shoes = [[0, 21], 
         [1, 23], 
         [1, 21], 
         [1, 23]]
the output should be
pairOfShoes(shoes) = false.
"""


def pairOfShoes(shoes):
    stack = {}
    for foot, nr in shoes:
        if nr in stack:
            if abs(foot-1) in stack[nr]:
                stack[nr].remove(abs(foot-1))
            else:
                stack[nr].append(foot)
        else:
            stack[nr] = [foot]
        if not stack[nr]:
            del stack[nr]
    return True if len(stack) is 0 else False
