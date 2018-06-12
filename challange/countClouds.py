"""
Given a 2D grid skyMap composed of '1's (clouds) and '0's (clear sky), count the number of clouds. A cloud is surrounded by clear sky, and is formed by connecting adjacent clouds horizontally or vertically. You can assume that all four edges of the skyMap are surrounded by clear sky.

Example

For

skyMap = [['0', '1', '1', '0', '1'],
          ['0', '1', '1', '1', '1'],
          ['0', '0', '0', '0', '1'],
          ['1', '0', '0', '1', '1']]
the output should be
countClouds(skyMap) = 2;

For

skyMap = [['0', '1', '0', '0', '1'],
          ['1', '1', '0', '0', '0'],
          ['0', '0', '1', '0', '1'],
          ['0', '0', '1', '1', '0'],
          ['1', '0', '1', '1', '0']]
the output should be
countClouds(skyMap) = 5.
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
            if maps[y][x] == '1':
                while True:
                    p = neighbours.pop(0)
                    if p[1] >= 0 and p[1] < rows and p[0] >= 0 and p[0] < cols:
                        if maps[p[1]][p[0]] == maps[y][x]:
                            graph[(y, x)] |= {(p[1], p[0])}
                    if not neighbours:
                        break
    return graph


def countClouds(maps):
    if not maps:
        return 0

    graph = build_graph(maps)
    
    rows = len(maps)
    cols = len(maps[0])
    visited = set()
    counter = 0
    for y in range(rows):
        for x in range(cols):
            if maps[y][x] == '1' and (y, x) not in visited:
                visited |= dfs(graph, (y,x))
                counter += 1
    return counter
