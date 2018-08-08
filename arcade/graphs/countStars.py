"""
Medium

Codewriting

300

You decided to create an automatic image recognizer that will determine the object in the image based on its contours. The main recognition system is already implemented, and now you need to start the teaching process.

Today you want to teach your program to recognize star patterns in the image of the night sky, which means that you need to implement a function that, given the adjacency matrix representing a number of contours in the sky, will find the number of stars in it.

The graph representing some contour is cosidered to be a star if it is a tree of size 2 or if it is a tree of size k > 2 with one internal node (which is a tree root at the same time) and k - 1 leaves.
Here is an example of some stars:

Stars

Given the sky objects' contours as an undirected graph represented by its adjacency matrix adj, calculate the number of stars in it.

Example

For

adj = [[false, true, false, false, false],
       [true, false, false, false, false],
       [false, false, false, true, false],
       [false, false, true, false, false],
       [false, false, false, false, false]]
the output should be
countStars(adj) = 2.

Here's what the given graph looks like:

"""


from collections import defaultdict

def build_graph(adj):
    graph = defaultdict(set)
    for i, row in enumerate(adj):
        for j, x in enumerate(row):
            if x is True:
                graph[i] |= {j}
    return graph

def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited
    
def is_star(graph, component):
    _length = len(component)
    if _length == 1:
        return 0
    expected = [1 for _ in range(_length - 1)]
    expected.append(_length - 1)
    for vertex in component:
        edges_count = len(graph[vertex])
        if edges_count not in expected:
            return 0
        expected.remove(edges_count)
    return 0 if expected else 1

def countStars(adj):
    graph = build_graph(adj)
    visited = set()
    counter = 0
    print graph
    for vertex in graph:
        if vertex not in visited:
            _visited = dfs(graph, vertex)
            visited |= _visited
            counter += is_star(graph, _visited)
    return counter
