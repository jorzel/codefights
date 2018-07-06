"""
World Cup is going on! One of the most fascinating parts of it is the group stage that has recently ended. A lot of great teams face each other to reach the playoff stage. In the group stage, each pair of teams plays exactly one game and each team receives 3 points for a win, 1 point for a draw and 0 points for a loss.
You fell asleep. What a shame. While you were sleeping, your team has played a lot of games! Now you know how many matches your team has played, how many goals it has scored and how many has missed. Now you need to find out the maximum amount of points your team can have.

Example

For matches = 2, goalsFor = 1 and goalsAgainst = 2, the output should be
maxPoints(matches, goalsFor, goalsAgainst) = 3;
For matches = 2, goalsFor = 3 and goalsAgainst = 2, the output should be
maxPoints(matches, goalsFor, goalsAgainst) = 4.
"""


def maxPoints(matches, goalsFor, goalsAgainst):
    points = 0
    while goalsFor > 0 and matches > 1:
        goalsFor -= 1
        matches -= 1
        points += 3
    while matches > 1:
        points += 1
        matches -= 1
    if goalsAgainst == goalsFor:
        points += 1
    elif goalsFor > goalsAgainst:
        points += 3
    return points

