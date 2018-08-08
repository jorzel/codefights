"""

Easy

Codewriting

300

You decided to create an automatic image recognizer that will determine the object in the image based on its contours. The main recognition system is already implemented, and now you need to start the teaching process.

Today you want to teach your program to recognize butterfly patterns, which means that you need to implement a function that, given the adjacency matrix representing the contour, will determine whether it's a butterfly or not.

The butterfly contour looks like this:

A butterfly

Given the object's contour as an undirected graph represented by adjacency matrix adj determine whether it's a butterfly or not.

Example

For

adj = [[false, true, true, false, false],
       [true, false, true, false, false],
       [true, true, false, true, true],
       [false, false, true, false, true],
       [false, false, true, true, false]]
the output should be
isButterfly(adj) = true.

Here's what the given graph looks like:

"""


def isButterfly(adj):
    size = 5
    counter = []
    for y in range(size):
        _counter = 0
        for x in range(size):
            if x == y and adj[y][x] is True:
                return False
            if adj[y][x] is True:
                _counter += 1
        counter.append(_counter)
    expected = [4, 2, 2, 2, 2]
    for e in expected:
        if e not in counter:
            return False
        counter.remove(e)        
    return False if counter else True