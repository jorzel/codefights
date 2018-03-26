
"""
You've just started constructing a military academy. It will take t seconds to erect the building, but given that you're in a hurry you decide this is too long to wait.

Fortunately, your Alliance offers you help to speed up construction - this is called a boost. Each member of the Alliance can decrease the time needed to finish the building either by 10% of the initial construction time or by 1 minute (whichever is greater). However, you can't get more than 10 boosts for a given construction project. Assuming that your Alliance members act optimally, find the shortest possible time it will take to build the academy.

Note:

If 10% of the total construction time doesn't equal an integer number of seconds, then the time bonus you get is rounded down (for each of the Alliance members independently).
If time decreased using boosts becomes negative you should return 0.
Example

For t = 1000 and allianceSize = 10, the output should be
allianceHelp(t, allianceSize) = 0.
If each member of the Alliance boosts the building by 10% (i.e. by 100 seconds), your new academy will be finished instantly.

For t = 999 and allianceSize = 11, the output should be
allianceHelp(t, allianceSize) = 9.
Any 10 of your 11 allies can speed the construction up by 10% (which equals 99 seconds since 99.9 is rounded down).

For t = 100 and allianceSize = 1, the output should be
allianceHelp(t, allianceSize) = 40.
Your only Alliance member will boost the construction by 1 minute (i.e. 60 seconds).
"""
import math

def allianceHelp(t, allianceSize):
    help_time = int(0.1 * t)  if int(0.1 * t)  > 60 else 60
    help_size = allianceSize if allianceSize < 10 else 10
    result = t - help_size * help_time
    return result if result > 0 else 0
