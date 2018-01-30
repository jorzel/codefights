"""
A ciphertext alphabet is obtained from the plaintext alphabet by means of rearranging some characters. For example "bacdef...xyz" will be a simple ciphertext alphabet where a and b are rearranged.

A substitution cipher is a method of encoding where each letter of the plaintext alphabet is replaced with the corresponding (i.e. having the same index) letter of some ciphertext alphabet.

Given two strings, check whether it is possible to obtain them from each other using some (possibly, different) substitution ciphers.

Example

For string1 = "aacb" and string2 = "aabc", the output should be
isSubstitutionCipher(string1, string2) = true.

Any ciphertext alphabet that starts with acb... would make this transformation possible.

For string1 = "aa" and string2 = "bc", the output should be
isSubstitutionCipher(string1, string2) = false.
"""

def isSubstitutionCipher(string1, string2):
    alphabet1, alphabet2 = {}, {}
    
    for s1, s2 in zip(string1, string2):
        if s1 not in alphabet1:
            alphabet1[s1] = s2
        else:
            if alphabet1[s1] != s2:
                return False
        if s2 not in alphabet2:
            alphabet2[s2] = s1
        else:
            if alphabet2[s2] != s1:
                return False
    return True
