"""
Medium

Codewriting

2000

You and your friends had an enjoyable but challenging time rock climbing, so now you're aiming for something simpler - climbing trees! Since you weren't all able to climb the wall before, you'd like to find a tree where as many friends as possible can reach the top.

Given an array branches containing 2-element integer arrays of the form [height, weightLimit], and an array friends containing 2-element integer arrays of the form [reach, weight], find how many friends can reach the top of the tree.

Each friend is able to reach from one branch to another if their weight is less than or equal to the next branch's weightLimit and their reach is greater than or equal to the difference in height.

Since everyone is still a little sore from the rock climbing, no one will have the strength to help pull up the climber following below, so for this climb, each friend is on their own (but maybe we'll try again later once everyone's fully recovered).

NOTE: All friends start at a height of 0, so it's not guaranteed that the first branch is reachable

Example

For branches = [[3, 10], [6, 9], [7, 2], [10, 7], [11, 1], [12, 2], [18, 11]] and friends = [[4, 1], [7, 10], [6, 2], [7, 6]], the output should be treeClimbing(branches, friends) = 1.

Friend 0 only has a reach of 4, so they're not able to reach between the branches at heights 12 and 18
Friend 1 has a weight of 10, so they can only be supported by the branches at heights 3 and 18, but it would require a reach of 15 to get between them, so since their reach is only 7, they can't make it
Friend 2 has a weight of 2, so they can be supported by all the branches except the one at height 11. They can reach the top by grabbing the branches at heights 3, 6, 10, 12, and 18 (since the difference in heights is always less than or equal to their reach of 6)
Friend 3 can make it to the branch at height 10, but since they're too heavy for the branch at 12, and they can't quite reach from 10 to 18, they won't be able to reach the top
Since only one friend can climb this tree, it's not a very good choice. We should probably keep looking for a better climbing tree.

"""


def treeClimbing(branches, friends):
    counter = 0
    for reach, weight in friends:
        fail = False
        prev_height = 0
        _branches = [b for b in branches if b[1] >= weight]
        if _branches:
            if branches[-1] != _branches[-1]:
                continue
        else:
            continue
        for height, weight_limit in _branches:
            if height - prev_height > reach:
                fail = True
                break
            prev_height = height
        if not fail and _branches:
            counter += 1
    return counter
