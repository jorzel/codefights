"""
Define a word as a sequence of consecutive English letters. Find the longest word from the given string.

Example

For text = "Ready, steady, go!", the output should be
longestWord(text) = "steady".
"""


def longestWord(text):
    return sorted([(len(n), n) for n in re.compile("([\w][\w]*'?\w?)").findall(text)], reverse=True)[0][1]
