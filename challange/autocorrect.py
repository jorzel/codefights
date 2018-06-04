"""
Hey, let's do one more text editor themed challenge!

Autocorrect is a feature commonly found in mobile phones - when the user does a typo, it gets automatically replaced with the closest matching word from a list of known words.

Given a set of known words, trainingWords, and a sequence of words input by the user, typedWords, our task is to find the string we'll get once the elements of typedWords have been autocorrected. Since parsing words can be tedious, both trainingWords and typedWords are given as arrays of strings. The final text should be output as a single string (words joined by spaces).

How to select the closest word
To compare strings, we'll be using Levenshtein distance, which is basically a measure of how many edits would be required in order to transform one word into another. An edit is one of the following three operations:

insertion - add a new character to some part of the string
(eg: from "awkward" to "bawkward")
deletion - remove a character from some part of the string
(eg: from "friend" to "fiend")
replacement - replace one character in the string with a different character
(eg: from "nice" to "vice")
For any string in typedWords that doesn't occur in trainingWords, we'll replace it with the string from trainingWords that's considered closest according to Levenshtein distance. If there's a tie for the closest match, choose the one that appears earliest in trainingWords. Comparisons are case-sensitive.

Example

For trainingWords = ["without", "night", "text", "cellar", "requirement", "some", "park", "instinct", "flourish", "computing", "vision", "mean", "round", "mistakes", "vain", "exemption", "fast"] and typedWords = ["some", "tex", "whith", "mistakesd"], the output should be autocorrect(trainingWords, typedWords) = "some text without mistakes".
"""


def lev(s1, s2):
    if len(s1) < len(s2):
        return lev(s2, s1)

    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1 
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    
    return previous_row[-1]

def autocorrect(trainingWords, typedWords):
    results = []
    _cache = {}
    for typed in typedWords:
        closest_index = 0
        min_distance = None
        for i, trained in enumerate(trainingWords):
            _key = typed + '_' + trained
            if _key in _cache:
                distance = _cache[_key]
            else:
                _cache[_key] = distance = lev(typed, trained)       
            if not min_distance or distance < min_distance:
                min_distance = distance
                closest_index = i
            if distance == 0:
                break
        results.append(trainingWords[closest_index])
    return ' '.join(results)
            