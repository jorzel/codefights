"""
Medium

Codewriting

300

You decided to create an automatic image recognizer that will determine the object in the image based on its contours. The main recognition system is already implemented, and now you need to start the teaching process.

Today you want to teach your program to recognize wheel patterns, which means that you need to implement a function that, given the adjacency matrix representing the contour, will determine whether it's a wheel or not.

The wheel contour can be thought of as a single center vertex and a regular polygon with n (n > 2) vertices which are all connected to the center. Here is an example:

A wheel

Given the object's contour as an undirected graph represented by its adjacency matrix adj determine whether it's a wheel or not.

Example

For

adj = [[false, true, true, true, true],
       [true, false, true, false, true],
       [true, true, false, true, false],
       [true, false, true, false, true],
       [true, true, false, true, false]]
the output should be
isWheel(adj) = true.

Here's what the given graph looks like:

"""


def isWheel(adj):
    counter = []
    size = len(adj)
    for y, row in enumerate(adj):
        _counter = 0
        for x, val in enumerate(row):
            if val is True:
                if x == y:
                    return False
                _counter += 1
        counter.append(_counter)
    if size == 0 and counter == [1,1,1]:
        return True
    expected = [3 for _ in range(size - 1)]
    expected.append(size - 1)
    for edges_count in counter:
        if edges_count not in expected:
            return False
        expected.remove(edges_count)
    return False if expected else True
