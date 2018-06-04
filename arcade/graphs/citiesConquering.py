"""
Once upon a time, in a kingdom far, far away, there lived a king Byteasar VII. He reigned during the Dark Times, so very little is known about those times. It is known that when he ascended the throne, there were n cities in the kingdom, connected by several two-way roads. But before the young king managed to start ruling, the enemy came to the gates: the evil emperor Bugoleon invaded the kingdom and started to conquer the cities day after day.

It is not known how long it took to capture each of the cities, but you've recently discovered an ancient chronicle saying that each day Bugoleon captured all the cities that had at most 1 neighboring free city at the moment. Knowing this fact, the number of cities n and all the roads of the kingdom, determine in how many days each of the cities was conquered.

Example

For n = 10 and

roads = [[1, 0], [1, 2], [8, 5], [9, 7], 
         [5, 6], [5, 4], [4, 6], [6, 7]]
the output should be
citiesConquering(n, roads) = [1, 2, 1, 1, -1, -1, -1, 2, 1, 1].
"""

def build_graph(n, roads):
    graph = {}
    for node in range(n):
        graph[node] = list()
    for edge in roads:
        left, right = edge[0], edge[1]
        left1, right1 = edge[1], edge[0]
        for l,r in zip([left, right], [left1, right1]):
            graph[l] += [r]
    return graph

def citiesConquering(n, roads):
    graph = build_graph(n, roads)
    counter = {node: -1 for node in range(n)}
    day = 1
    while True:
        nodes = graph.keys()
        to_remove = []
        for node in nodes:
            edges_count = len(graph[node])
            if edges_count < 2:
                edges = graph[node]
                if edges_count == 1:
                    to_remove.append((edges[0], node))
                counter[node] = day
                graph.pop(node)
        for edge in to_remove:
            if edge[0] in graph:
                graph[edge[0]].remove(edge[1])
        day += 1
        if not to_remove:
            break
    return counter.values()