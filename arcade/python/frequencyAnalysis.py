"""

Easy

Recovery

100

Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
You've recently read "The Gold-Bug" by Edgar Allan Poe, and was so impressed by the cryptogram in it that decided to try and decipher an encrypted text yourself. You asked your friend to encode a piece of text using a substitution cipher, and now have an encryptedText that you'd like to decipher.

The encryption process in the story you read involves frequency analysis: it is known that letter 'e' is the most frequent one in the English language, so it's pretty safe to assume that the most common character in the encryptedText stands for 'e'. To begin with, implement a function that will find the most frequent character in the given encryptedText.

Example

For encryptedText = "$~NmiNmim$/NVeirp@dlzrCCCCfFfQQQ",
the output should be
frequencyAnalysis(encryptedText) = 'C'.

Letter 'C' appears in the text more than any other character (4 times), which is why it is the answer.
"""

from collections import Counter

def frequencyAnalysis(encryptedText):
    return sorted(Counter(encryptedText).items(), key=lambda x: x[1])[-1][0]
