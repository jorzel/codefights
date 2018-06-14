"""
A jeweler is given an order to make a crown. He is given a set of n precious stones of sizes s1, ..., sn. The size of each stone is proportional to its value.

To make the crown perfect, he has decided to attach two rows of stones of equal length to the front of the crown. All the stones in a row must be of the same size, and the jeweler can't have any leftovers, so he must use all available stones of that size.

In order to make the crown as valuable as possible, the jeweler would like to use the maximum total number of stones. If there are multiple choices for maximizing the number of stones, he should choose the one that has the larger maximum size of stone.

You need to help the jeweler choose the stones for the two rows. Return the largest stone size that would be attached to the most valuable possible crown, or -1 if it is impossible to design the crown with the given set of stones.

Example

For stones = [1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6, 5], the output should be stonesForCrown(stones) = 2.

There are 4 possibilities for the sets of stones the jeweler could use: (2, 2, 2, 1, 1, 1), (4, 4, 3, 3), (6, 6, 4, 4) and (6, 6, 3, 3). Although (6, 6, 4, 4) would have the largest stones, (2, 2, 2, 1, 1, 1) has the most stones, so the answer is 2.

For stones = [1, 1, 2, 2, 3, 3, 7], the output should be stonesForCrown(stones) = 3.

There are 3 possible crowns that could be made from these stones: (2, 2, 1, 1), (3, 3, 1, 1), and (3, 3, 2, 2). All of these contain the same number of stones, and the largest size is 3, so the answer is 3.

For stones = [1, 2, 2, 7, 7, 7], the output should be stonesForCrown(stones) = -1.

It's not possible for the jeweler to make 2 rows of equal length from these stones (remember: he must use all the stones of each chosen size).
"""


from collections import Counter, defaultdict

def stonesForCrown(stones):
    counter = Counter(stones)
    values = defaultdict(list)
    for value, count in counter.iteritems():
        values[count] += [value]
    for count, numbers in sorted(values.iteritems(), reverse=True):
        _length = len(numbers)
        if _length > 1:
            return sorted(numbers, reverse=True)[0]
    return -1