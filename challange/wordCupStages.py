"""
Medium

Codewriting

2000

Before the World Cup starts, all teams are split into 8 groups, each containing 4 teams. After all the teams within each group have played each other, the two highest-performing teams move on to the next round - playoff.



You're given a list of group results in the following format:

[[A1, A2, A3, A4],
 [B1, B2, B3, B4],
 [C1, C2, C3, C4],
 ...
 [H1, H2, H3, H4]]
Here each row contains the results of one group (first element of the row is the command got 1st place, second element is for command on the 2nd place, etc.)

So for example, if the first row looks like ["Uruguay", "Russia", "Egypt", "Saudi Arabia"], it means that within group A, Uruguay is first, Russia is second, Egypt placed third, and Saudi Arabia placed fourth. Therefore, only Russia and Uruguay will move on to playoffs.

The matchups for the next round are the following: (A1, B2), (B1, A2), (C1, D2), (D1, C2), (E1, F2), (F1, E2), (G1, H2), (H1, G2) (the first place team from group A will face the second place team from group B, the first place team from group B will face the second place team from group A, the first place team from group C will face the second place team from group D, etc).

Given a matrix of results, your task is to return a table of matchups for the next round. The columns should be vertically aligned, with the team names aligned to the left.

Example

For

results = [
    ["Uruguay", "Russia", "Egypt", "Saudi Arabia"],
    ["Spain", "Portugal", "Iran", "Morocco"],
    ["France", "Denmark", "Peru", "Australia"],
    ["Croatia", "Argentina", "Nigeria", "Iceland"],
    ["Brazil", "Switzerland", "Serbia", "Costa Rica"],
    ["Sweden", "Mexico", "South Korea", "Germany"],
    ["Belgium", "England", "Tunisia", "Panama"],
    ["Colombia", "Japan", "Senegal", "Poland"]
]
the output should be

worldCupStages(results) = ["|Uruguay |Spain |France   |Croatia|Brazil|Sweden     |Belgium|Colombia|",
                           "|Portugal|Russia|Argentina|Denmark|Mexico|Switzerland|Japan  |England |"]

"""

def worldCupStages(results):
    firsts, seconds = [], []
    for group in results:
        firsts.append((group[0], len(group[0])))
        seconds.append((group[1], len(group[1])))
    output = ["|", "|"]
    for i in range(len(firsts)):
        if i % 2 == 0:
            j = i + 1
        else:
            j = i - 1
        first, second = firsts[i], seconds[j]
        width = max(first[1], second[1])
        output[0] += first[0] + (width - first[1]) * ' ' + '|'
        output[1] += second[0] + (width - second[1]) * ' ' + '|'
    return output