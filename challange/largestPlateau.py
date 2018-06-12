"""
Your terraforming crew is busy at work on a mountaintop, but it's time to break for lunch. In order to allow everyone to have lunch together, we'd like to find a plateau on the mountain where everyone can sit.

Given a topographic map in the form of a matrix of integers map, find the area of the largest plateau.

Example

For

map = [[1,0,0,2,2,0],
       [0,0,2,1,0,2],
       [0,1,1,2,2,2],
       [1,2,1,0,2,1]]
the output should be largestPlateau(map) = 5. The crew could either choose the plateau with elevation 0 or the one with elevation 2; both of which have an area of 5:
"""



from collections import defaultdict

def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited

def build_graph(maps):
    graph = defaultdict(set)
    rows = len(maps)
    cols = len(maps[0])
    for y in range(rows):
        for x in range(cols):
            neighbours = [(x - 1, y),
                          (x, y - 1),
                          (x + 1, y),
                          (x, y + 1)]
            while True:
                p = neighbours.pop(0)
                if p[1] >= 0 and p[1] < rows and p[0] >= 0 and p[0] < cols:
                    if maps[p[1]][p[0]] == maps[y][x]:
                        graph[(y, x)] |= {(p[1], p[0])}
                if not neighbours:
                    break
    return graph


def largestPlateau(maps):
    if not maps:
        return 0

    graph = build_graph(maps)
    
    rows = len(maps)
    cols = len(maps[0])
    visited = set()
    max_plateu = 0
    for y in range(rows):
        for x in range(cols):
            if (y, x) not in visited:
                plateu = dfs(graph, (y,x))
                visited |= plateu
                if len(plateu) > max_plateu:
                    max_plateu = len(plateu)
    return max_plateu