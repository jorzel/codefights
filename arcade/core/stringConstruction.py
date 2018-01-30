"""
How many strings equal to a can be constructed using letters from the string b? Each letter can be used only once and in one string only.

Example

For a = "abc" and b = "abccba", the output should be
stringsConstruction(a, b) = 2.

We can construct 2 strings a with letters from b.
"""

import copy

def stringsConstruction(a, b):
    stack_b = list(b)
    counter = 0
    while True:
        stack_a = list(a)
        temp_b = copy.deepcopy(stack_b)
        for s in temp_b:
            if s in stack_a:
                stack_a.remove(s)
                stack_b.remove(s)
            if len(stack_a) == 0:
                counter += 1
                break
        if len(stack_a) > 0:
            break
            
    return counter