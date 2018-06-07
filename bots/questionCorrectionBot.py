"""
When a user asks a question on Quora, the system automatically tries to improve the question's formatting before showing it to more users. Given a question as an input string, perform formatting corrections according to the following rules:

Strip excessive whitespaces:
Remove whitespaces at the start and end, as well as multiple spaces in a row
Fix spacing around punctuation:
Each comma should have a trailing space, but no space preceding it
Questions should start with a capital letter
Questions should end with a single question mark (not 0 or more than one).
Example

For question = " this isn't a relevant question , is it??? ", the output should be
questionCorrectionBot(question) = "This isn't a relevant question, is it?";
For question = "Is this answer correct?", the output should be
questionCorrectionBot(question) = "Is this answer correct?".
"""

import re

def questionCorrectionBot(question):
    question = question.strip().replace(',', ', ')
    question = re.sub(' +',' ', question)
    question = re.sub('\\?+', '?', question)
    question = re.sub(' +,', ',', question)
    if question[-1] != '?':
        question += '?'
    return question[0].upper() + question[1:]