"""
Medium

Codewriting

1000

As part of a successful war campaign you just took control of a major city. This is where you will make your new Forward Operating Base, and where your troops will house their new barracks. However, when your troops are in the city they consume k units of food (for some integer k) as upkeep at the beginning of every hour (i.e. at HH:00:00 where HH stands for an hour). This upkeep happens even when you're offline and not actively playing.

Given the timestamps of logout and login performed consecutively and the amount of food you had at those moments, find how much food your troops consume each hour.

For simplicity's sake, assume that you are neither logged in nor logged out at the beginning of each hour.

Example

For logOut = [1451604600, 100] and logIn = [1451660401, 36], the output should be
resourceCatchUp(logOut, logIn) = 4.

1451604600 corresponds to 31 December, 2015, 23:30:00;
1451660401 corresponds to 1 January, 2016, 15:00:01;
thus, food consumption took place exactly 16 times while you were logged out;
your amount of food was reduced by 64 units. This means that each hour your troops consumed 4 units of food.
Check out the image below for better understanding:
"""


from datetime import datetime

def resourceCatchUp(logOut, logIn):
    out_dt = datetime.fromtimestamp(logOut[0])
    in_dt = datetime.fromtimestamp(logIn[0])
    consumption = math.ceil((in_dt - out_dt).total_seconds() / float(3600))
    return (logOut[1] - logIn[1]) / consumption

