"""
Given a string, find the shortest possible string which can be achieved by adding characters to the end of initial string to make it a palindrome.

Example

For st = "abcdc", the output should be
buildPalindrome(st) = "abcdcba".
"""

def isPalindrome(st):
    for i in range(len(st) / 2):
        if st[i] != st[-1 - i]:
            return False
    return True

def buildPalindrome(st):
    if isPalindrome(st):
        return st
    rev = st[::-1]
    for i in range(len(st)):
        if isPalindrome(rev[:i + 1]):
            index = i
    return st + rev[index + 1:]
