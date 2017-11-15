"""
Given the string, check if it is a palindrome.

Example

For inputString = "aabaa", the output should be
checkPalindrome(inputString) = true;
For inputString = "abac", the output should be
checkPalindrome(inputString) = false;
For inputString = "a", the output should be
checkPalindrome(inputString) = true.
"""


def checkPalindrome(inputString):
    size = len(inputString)
    if size == 1:
        return True
    for i in xrange(0, size / 2):
        if inputString[i] != inputString[(size - 1) - i]:
            return False
    return True
