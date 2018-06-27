"""
Not long ago, a spam campaign originated on some of the major social networks, and it's started to affect Kik users as well. Most of the spam comes from a limited number of highly-motivated individuals, possibly from a single group, who constantly update their spam software. What started off as some simple message-sending bots has now evolved into something that requires a large team of engineers to fight against it.

At the beginning, the bots weren't that clever. The spam detection could essentially be narrowed down to checking messages against several simple criteria. For a user's stream of messages over a given time period, the spammer could be identified if:

More than 90 % of all messages had fewer than 5 words (here, a word is defined as a sequence of consecutive letters which is neither immediately preceded nor followed by another letter);
More than 50 % of messages to any one user had the same content, assuming that there were at least 2 messages to that user;
More than 50 % of all messages had the same content, assuming that there were at least 2 messages;
More than 50 % of all messages contained at least one of the words from the given list of spamSignals (the case of the letters doesn't matter).
You are applying to the Anti-Spam Team at Kik, so you want to make sure you understand how this basic spam detection program worked. Implement a function that, given a stream of messages and a list of spamSignals, determines whether it's possible that the user might be a spammer by checking against the criteria above.

Example

For

messages = [["Sale today!", "2837273"],
            ["Unique offer!", "3873827"],
            ["Only today and only for you!", "2837273"],
            ["Sale today!", "2837273"],
            ["Unique offer!", "3873827"]]
and spamSignals = ["sale", "discount", "offer"], the output should be

spamDetection(messages, spamSignals) = [
  "passed",
  "failed: 2837273 3873827",
  "passed",
  "failed: offer sale"
]
Here are the results of the checks per criterion:

4 out of 5 (80 %) messages have fewer than five words, which is within acceptable parameters = "passed";
2 out of 3 messages to user 2837273 are the same and both messages to user 3873827 are the same, which is a good indicator that they might be spam = "failed: 2837273 3873827";
2 out of 5 (40 %) messages have the same content, which is within acceptable parameters = "passed";
4 out of 5 (80 %) messages contain words from spamSignals. The two words that appear in the messages are offer and sale and offer is the lexicographically smaller of the two, so the output = "failed: offer sale".
For

messages = [["Check Codefights out", "7284736"],
            ["Check Codefights out", "7462832"],
            ["Check Codefights out", "3625374"],
            ["Check Codefights out", "7264762"]]
and spamSignals = ["sale", "discount", "offer"], the output should be

spamDetection(messages, spamSignals) = [
  "failed: 1/1",
  "passed",
  "failed: Check Codefights out",
  "passed"
]
Since all users in messages received only one message each, it's impossible to check the second criterion. The fourth criterion doesn't match: there are not any words from spamSignals in the messages. However, the first and the third criteria failed, since all the messages contain 4 words ("failed: 1/1") and have the exact same content ("failed: Check Codefights out").

82/300
"""

import re
from fractions import Fraction

def criterium_one(wc, messages):
    tresh = 90
    message_count = len(messages)
    c1 = 100.0 * wc / message_count
    result = Fraction(wc, message_count)
    result = '1/1' if result == 1 else str(result)
    return "passed" if c1 < tresh else "failed: {}".format(result)


def criterium_two(users):
    tresh = 50
    dup_users = []
    for u, u_messages in users.items():
        if len(u_messages) > 1:
            for m in u_messages:
                dup_rate = 100.0 * sum([1 for x in u_messages if x == m]) / len(u_messages)
                if dup_rate > tresh:
                    dup_users.append(u)
                    break
    dup_users.sort()
    return "passed" if not dup_users else "failed: " + " ".join(dup_users)


def criterium_three(messages):
    tresh = 50
    dup_message = None
    if len(messages) > 1:
        for m in messages:
            dup_rate = 100.0 * sum([1 for x in messages if x == m]) / len(messages)
            if dup_rate > tresh:
                dup_message = m
                break
    return "passed" if dup_message is None else "failed: " + dup_message


def criterium_four(spam_signals, messages):
    tresh = 50
    spam_words = []
    counter = 0
    for s in spam_signals:
        pattern = re.compile(s + '([^a-zA-Z]|$)', re.IGNORECASE)
        for m in messages:
            if re.search(pattern, m):
                if s not in spam_words:
                    spam_words.append(s)
                counter += 1
    signaled_words = []

    if 100.0 * counter / len(messages) > tresh:
        signaled_words = spam_words
        signaled_words.sort()
    return "passed" if not signaled_words else "failed: " + " ".join(signaled_words)    


def spamDetection(messages, spam_signals):
    wc = 0
    users = {}
    contents = []
    for m in messages:
        content = m[0]
        contents.append(content)
        user_id = m[1]
        if user_id not in users:
            users[user_id] = [content]
        else:
            users[user_id].append(content)
        if len(content.split()) < 5:
            wc += 1

    return [criterium_one(wc, messages),
            criterium_two(users),
            criterium_three(contents),
            criterium_four(spam_signals, contents)]
