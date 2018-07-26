"""
Medium

Codewriting

2000

Sometimes a player is offered so many quests during a game that it's difficult to complete them all. Time is short, and naturally each player wants to complete as many quests as possible while maximizing the points they earn. Here is the scenario:

PlayerOne has a long list of quests, but only timeForQuests hours to complete them. The ith quest should be completed in hi hours, and the reward for it is pointsi. Each quest can be completed only once. Calculate the maximum number of points that PlayerOne can earn.

Example

For h = [1, 4, 2], points = [2, 3, 2], and timeForQuests = 4, the output should be
questEfficiencyItem(h, points, timeForQuests) = 4.

PlayerOne has 4 hours to complete the quests, so it is possible to earn:

2 points for the first quest;
3 points for the second quest;
2 points for the third quest;
2 + 2 = 4 points for the first and the third quests.
So, the maximum number of points PlayerOne can earn is 4.

For h = [1, 4, 2], points = [2, 5, 2], and timeForQuests = 4, the output should be
questEfficiencyItem(h, points, timeForQuests) = 5.

Completing the second quest gives 5 points, which is greater than solving the first and the third quests (2 + 2 = 4 points)

KNAPSACK PROBLEM

"""


def questEfficiencyItem(h, points, timeForQuests):
    memo = [[0 for _ in range(timeForQuests+1)] for _ in range(len(h)+1)]
    for i in range(1, len(h)+1):
        for j in range(timeForQuests+1):
            if h[i-1] > j:
                memo[i][j] = memo[i-1][j]
            else:
                memo[i][j] = max(memo[i-1][j], memo[i-1][j-h[i-1]] + points[i-1])
    return memo[-1][-1]
                
