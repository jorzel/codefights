"""
Given two lists lst1 and lst2, your task is to return a list formed by the elements of lst1 followed by the elements of lst2.

Note: this is a bugfix task, which means that the function is already implemented but there is a bug in one of its lines. Your task is to find and fix it.

Example

For lst1 = [2, 2, 1] and lst2 = [10, 11], the output should be
listsConcatenation(lst1, lst2) = [2, 2, 1, 10, 11].
"""

def listsConcatenation(lst1, lst2):
    res = lst1
    res.extend(lst2)
    return res
