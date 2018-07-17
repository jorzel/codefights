"""
Medium

Codewriting

2000

While you were watching a soccer match, you noticed that the commentator was talking about a player's offside position.

For simplicity, let's say that a player is in the offside position if there are fewer than 2 opponents that are closer to the opposing goal line (or equidistant to it). In other words, the player is offside if there are only 1 or 0 opponents ahead of them (or beside them).

We can represent the field on a Cartesian plane with one corner at (0, 0) and the opposite corner at (100, 64); however, since we're only concerned with the horizontal position of each player, we'll only be looking at the x values.

You are given an array teams, which contains two arrays of integers, representing the x positions of all the players of each team. The first team's net is at the left (x value of 0) and the second team's net is at the right (x value of 100).

You need to find out whether there are any players in an offside position on the field or not.

Example

For teams = [[5, 22, 30, 40, 30, 50, 30, 50, 50, 60, 50], [96, 20, 30, 25, 25, 40, 60, 70, 80, 70, 40]], the output should be offsidePosition(teams) = true.



A player from the blue team is in the offside position since there is only one player on the opposing team with an x value less than 20.

For teams = [[5, 22, 30, 40, 30, 50, 30, 50, 50, 60, 50], [96, 28, 30, 25, 25, 40, 60, 70, 80, 70, 40]], the output should be offsidePosition(teams) = false.



There are no players with fewer than 2 opponents closer to the opposing goal line, so no one is offside.

For teams = [[5, 20, 30, 40, 30, 50, 30, 50, 50, 60, 50], [96, 20, 30, 25, 25, 40, 60, 70, 80, 70, 40]], the output should be offsidePosition(teams) = false.



No player from the blue team has fewer than 2 opponents strictly closer to the opposing goal line. They are at the same distance as the second-closest opponent to the goal line, so they're not offside.
 """


def offsidePosition(t):
    t[0].sort()
    t[1].sort()
    return True if t[1][0] < t[0][1] or t[0][-1] > t[1][-2] else False
