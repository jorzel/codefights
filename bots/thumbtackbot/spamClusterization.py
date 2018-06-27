"""
Thumbtack tries to identify spam coming from multiple user accounts by comparing job request descriptions and identifying clusters that have high similarity. Their data analysis engineers are testing out a new clusterization algorithm that uses the Jaccard index. As a prospective team member, you've been asked to implement this algorithm.

You are given a list of requests and ids of the users who submitted them. Implement the following algorithm to identify possible spammers:

first, split each request into a set of words and convert them to lowercase. We formally define a word as a substring consisting of English letters, such that characters to the left of the leftmost letter and to the right of the rightmost letter are not letters;
next, calculate the Jaccard index of each pair of sets;
divide the sets into clusters so that:
each set belongs to some cluster;
if Jaccard index of two sets A and B is not less than the given threshold (meaning they are too similar), they belong to the same cluster. Note that if A and B as well as B and C satisfy this criteria, then A, B and C belong to the same cluster;
for each cluster that has more than one element, return the list of their author IDs in ascending order.
Example

For

requests = ["I need a new window.",
            "I really, really want to replace my window!",
            "Replace my window.",
            "I want a new window.",
            "I want a new carpet, I want a new carpet, I want a new carpet.",
            "Replace my carpet"]
ids = [374, 2845, 83, 1848, 1837, 1500] and
threshold = 0.5, the output should be
spamClusterization(requests, ids, threshold) = [[83, 1500], [374, 1837, 1848]].

The sets of words obtained after the first step are:

{"i", "need", "a", "new", "window"} - 5 elements;
{"i", "really", "want", "to", "replace", "my", "window"} - 7 elements;
{"replace", "my", "window"} - 3 elements;
{"i", "want", "a", "new", "window"} - 5 elements;
{"i", "want", "a", "new", "carpet"} - 5 elements (note that a set consists only of unique elements);
{"replace", "my", "carpet"} - 3 elements.
Here's a table of Jaccard indices for each pair of request (there are 6 requests in total):

1	2	3	4	5	6
1	-	2/10 = 1/5	1/7	4/6 = 2/3	3/7	0/8 = 0
2	1/5	-	3/7	3/9 = 1/3	2/10 = 1/5	2/8 = 1/4
3	1/7	3/7	-	1/7	0/8 = 0	2/4 = 1/2
4	4/6	3/9	1/7	-	4/6 = 2/3	0/8 = 0
5	3/7	1/5	0	2/3	-	1/7
6	0	1/4	1/2	0	1/7	-
Since threshold = 0.5, there are two clusters with more than one element. The first one contains the third and the sixth requests, and the second one contains requests number one, four and five (since Jaccard index of the first and fourth requests and of the fourth and fifth requests is larger than threshold, they all belong to the same cluster). After sorting their author ids, we arrive at the answer.
"""

import re
from itertools import combinations


def jaccard_index(A, B):
    return len(A.intersection(B)) / (1.0 * (len(A | B)))


def return_element(val, l):
    for i, el in enumerate(l):
        if val in el:
            return i
    return None

def get_connected_components(connections):
    components = []
    for i, conn in enumerate(connections):
        if i == 0:
            components.append([p for p in conn])
        else:
            exist = False
            for p in conn:
                ind = return_element(p, components)
                if ind is not None:
                    components[ind] += [x for x in conn if x not in components[ind]]
                    exist = True
            if not exist:
                components.append([p for p in conn])
    return components


def spamClusterization(requests, ids, threshold):
    sets = [(set([w.lower() for w in re.sub(r'([^\s\w]|_)+', '', r).split()]), _id) for r, _id in zip(requests, ids)]
    pairs = []
    for p in combinations(sets, 2):
        pair = (p[0][0], p[1][0])
        pair_ids = (p[0][1], p[1][1])
        if jaccard_index(pair[0], pair[1]) >= threshold:
            pairs.append([pair_ids[0], pair_ids[1]])

    components = pairs
    while True:
        results = get_connected_components(components)
        if results == components:
            break
        else:
            components = results

    for c in components:
        c.sort()
    components.sort()
    return components
