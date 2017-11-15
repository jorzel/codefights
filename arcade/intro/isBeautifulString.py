"""
A string is said to be beautiful if b occurs in it no more times than a; c occurs in it no more times than b; etc.

Given a string, check whether it is beautiful.

Example

For inputString = "bbbaacdafe", the output should be
isBeautifulString(inputString) = true;
For inputString = "aabbb", the output should be
isBeautifulString(inputString) = false;
For inputString = "bbc", the output should be
isBeautifulString(inputString) = false.
"""

import collections

def isBeautifulString(inputString):
    cnt = collections.Counter(inputString)
    start = 'a'
    for i in xrange(1, 26):
        try: 
            if cnt[chr(ord(start) + i)] > cnt[chr(ord(start) + i - 1)]:
                return False
        except:
            return False
    return True
        
