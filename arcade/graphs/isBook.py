"""
Medium

Codewriting

300

You decided to create an automatic image recognizer that will determine the object in the image based on its contours. The main recognition system is already implemented, and now you need to start the teaching process.

Today you want to teach your program to recognize book patterns, which means that you need to implement a function that, given the adjacency matrix representing the contour, will determine whether it's a book or not.

A book consists of a base and may have any number of pages.
The book's base consists of a single edge connecting two nodes, and it is a common edge for all the pages. Besides that, every page has only one node connected to both sides of the base.
Here is an example of a book:

Book

Given the object's contour as an undirected graph represented by its adjacency matrix adj determine whether it's a book or not.

Example

For

adj = [[false, true, true, true],
       [true, false, true, true],
       [true, true, false, false],
       [true, true, false, false]]
the output should be
isBook(adj) = true.

Here's how the given graph looks like:

"""


def isBook(adj):
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
    if size == 2 and counter == [1, 1]:
        return True
    expected = [2 for _ in range(size - 2)]
    expected.extend([size - 1, size - 1])
    for edges_count in counter:
        if edges_count not in expected:
            return False
        expected.remove(edges_count)
    return False if expected else True
