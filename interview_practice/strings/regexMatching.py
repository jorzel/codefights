"""
Given a pattern string and a test string, your task is to implement regex substring matching. If pattern is preceded by a ^, the pattern, excluding the ^, will be matched with the starting position of the test string. If pattern is followed by a $, the pattern, excluding the $, will be matched with the ending position of the test string. If no such markers are present, check whether pattern is a substring of test, regardless of its position.

Example

For pattern = "^code" and test = "codefights", the output should be
regexMatching(pattern, test) = true;
For pattern = "hts$" and test = "codefights", the output should be
regexMatching(pattern, test) = true;
For pattern = "hello" and test = "world", the output should be
regexMatching(pattern, test) = false.
"""


def regexMatching(pattern, test):
    result = False
    if pattern[0] == '^' or pattern[-1] == '$':
        if pattern[0] == '^':
            temp = pattern.replace('^', '').replace('$', '')
            if temp == test[:len(temp)]:
                result = True
        if pattern[-1] == '$':
            temp = pattern.replace('^', '').replace('$', '')
            if temp == test[len(test) - len(temp):]:
                result = True
    else:
        if pattern in test:
            result = True
    return result
