"""
Easy

Recovery

100

Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
At CodeSignal the users can get to the top of the leaderboard by earning XP (experience points) in different modes. The leaderboard is sorted by players XP in descending order, and in case of a tie - by their ids in ascending order.

Your task is to implement an algorithm that will return the state of the weekly leaderboard given a list of users.

Example

For

users = [["warrior", "1", "1050"],
         ["Ninja!",  "21", "995"],
         ["recruit", "3", "995"]]
the output should be
sortCodesignalUsers(users) = ["warrior", "recruit", "Ninja!"].

"""


def sortCodesignalUsers(users):
    res = [CodeSignalUser(*user) for user in users]
    res.sort(reverse=True)
    return map(str, res)

class CodeSignalUser(object):
    def __init__(self, *args):
        self.name = args[0]
        self._id = int(args[1])
        self.xp = int(args[2])
    
    def __lt__(self, other):
        return (self.xp, -self._id) < (other.xp, -other._id)

    def __str__(self):
        return self.name