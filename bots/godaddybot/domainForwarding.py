"""
Domain name forwarding lets GoDaddy domain owners automatically redirect their site visitors to a different site URL. Sometimes the visitors have to go through multiple redirects before ending up on the correct site.

Using the DNS Manager, GoDaddy customers can view redirects in a simple visual format. One handy feature is the ability to group the domains by the final website they redirect to. Your task is to implement this feature.

For the given redirects list, organize its domains into groups where for a specific group each domain eventually redirects visitors to the same website.

Example

For

redirects = [["godaddy.net", "godaddy.com"], 
             ["godaddy.org", "godaddycares.com"], 
             ["godady.com", "godaddy.com"],
             ["godaddy.ne", "godaddy.net"]]
the output should be

domainForwarding(redirects) = [["godaddy.com", "godaddy.ne", "godaddy.net", "godady.com"], 
                               ["godaddy.org", "godaddycares.com"]]
In the first group, "godaddy.ne" redirects to "godaddy.net", which in turn redirects to "godaddy.com". "godady.com" redirects visitors to "godaddy.com" as well.
In the second group, "godaddy.org" redirects visitors to "godaddycares.com".

Note, that domains in each group are sorted lexicographically and groups themselves are sorted lexicographically by the domain they redirect to. So in the example, the first group goes before the second because "godaddy.com" is lexicographically smaller than "godaddycares.com".
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
