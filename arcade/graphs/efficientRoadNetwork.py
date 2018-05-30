"""
Once upon a time, in a kingdom far, far away, there lived a king Byteasar III. As a smart and educated ruler, he did everything in his (unlimited) power to make every single system of his kingdom efficient. The king went down in history as a great road builder: during his reign a great number of roads were built, and the road system he created was the most efficient for those dark times.

When you started to learn about Byteasar's III deeds in your history classes, the creeping doubt crawled into the back of your mind: what if the famous king wasn't so great after all? According to the most recent studies, there were n cities in the Byteasar's kingdom, which were connected by the two-ways roads. You managed to get information about this roads from the university library, so now you can write a function that will determine whether the road system in Byteasar's kingdom was efficient or not.

A road system is considered efficient if it is possible to travel from any city to any other city by traversing at most 2 roads.

Example

For n = 6 and

roads = [[3, 0], [0, 4], [5, 0], [2, 1],
          [1, 4], [2, 3], [5, 2]]
the output should be
efficientRoadNetwork(n, roads) = true.

Here's how the road system can be represented:


For n = 6 and

roads = [[0, 4], [5, 0], [2, 1],
          [1, 4], [2, 3], [5, 2]]
the output should be
efficientRoadNetwork(n, roads) = false.

Here's how the road system can be represented:


As you can see, it's only possible to travel from city 3 to city 4 by traversing at least 3 roads.
"""

from itertools import combinations
from collections import defaultdict

def build_graph(roads):
    graph = defaultdict(set)
    for r in roads:
        left, right = r[0], r[1]
        left1, right1 = r[1], r[0]

        for l,r in zip([left, right], [left1, right1]):
            graph[l] |= {r}
    return graph

         
def generate_pairs(n):
    for p in combinations([i for i in range(n)], 2):
        yield p

def efficientRoadNetwork(n, roads):
    if not roads and n > 1:
        return False
    graph = build_graph(roads)
    for conn in generate_pairs(n):
        try:
            if not conn[0] in graph[conn[1]]: 
                if len(graph[conn[0]].intersection(graph[conn[1]])) == 0:
                    return False
        except KeyError:
            return False
    return True

    
