"""
FIFA World Cup 2018 is going on! A group stage has recently ended and you want to see how many matches with your favorite team ended in a draw and how many ended in a win in the group stage. Unfortunately, you don't have match results and you know only how many teams were in the group and how many points your team has scored. As you probably know, in the group stage each pair of teams plays exactly one game and each team gets 0 points for a loss, 1 for a draw and 3 for a win.
Now you want to calculate the number of draws and the number of wins of your favorite team. If there are several possible options, return all of them.

Example

For teams = 5 and points = 10, the output should be drawsAndWins(teams, points) = [[1, 3]];
For teams = 5 and points = 4, the output should be drawsAndWins(teams, points) = [[1, 1], [4, 0]].
"""

def drawsAndWins(teams, points):
    if teams in (0,1):
        return [[0,0]]
    
    WIN, DRAW = 3, 1
    
    results = []
    matches = teams - 1
    max_win = points / WIN
    
    for i in reversed(range(max_win + 1)):
        remaining_points = points - i * WIN
        remaining_matches = matches - i
        if remaining_matches >= remaining_points and points >= 0:
            results.append([remaining_points,i])
    return results
