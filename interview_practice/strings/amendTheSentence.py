"""
You have been given a string s, which is supposed to be a sentence. However, someone forgot to put spaces between the different words, and for some reason they capitalized the first letter of every word. Return the sentence after making the following amendments:

Put a single space between the words.
Convert the uppercase letters to lowercase.
Example

For s = "CodefightsIsAwesome", the output should be
amendTheSentence(s) = "codefights is awesome";
For s = "Hello", the output should be
amendTheSentence(s) = "hello".
"""

import re

def amendTheSentence(s):
    ind = 0
    for i in range(len(s)):
        if s[i].isupper() is True:
            ind = i
            break
    words = re.findall('[A-Z][^A-Z]*', s[ind:])
    for i in range(len(words)):
        words[i] = words[i].lower()
    prefix = '' if ind == 0 else s[:ind] + ' '
    return prefix + ' '.join([w for w in words])
