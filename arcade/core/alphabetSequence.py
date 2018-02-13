"""
Check whether the given string is a subsequence of the plaintext alphabet.

Example

For s = "effg" or s = "cdce", the output should be
alphabetSubsequence(s) = false;
For s = "ace" or s = "bxz", the output should be
alphabetSubsequence(s) = true.
"""


def alphabetSubsequence(string):
    alphabet = []
    for i, s in enumerate(string):
        if s.isalpha() and s not in alphabet:
            if i == 0 or (ord(s) > ord(string[i - 1])):
                alphabet.append(s)
            else:
                return False
        else:
            return False
    return True
