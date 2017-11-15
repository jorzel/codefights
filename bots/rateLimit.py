"""
Your company decides to give Kik a try and write a chat bot to be used on the platform. You've worked hard and it's almost finished, and all that's left to do now is test it. One of the things you want to check is whether the number of messages your bot sends exceeds the per user rate limit.

The purpose of the per user rate limit is to prevent bots from sending an excessively high number of messages to individual users every day. This limit is defined on a per-user basis: at midnight each day (00:00 in local server time, which also happens to be Coordinated Universal Time) the baseline limit is reset to startingAllowance. Once your bot sends a message to a given user that day, the per user rate limit (for that user) is decreased by 1. Whenever a user messages the bot, the per user rate limit increases by 1 (for that user). If at some point your bot tries to send a message to a user whose current per user rate limit equals 0, the sending fails.

Importantly, the rate limit is applied to batches of messages sent to multiple users. For example, if a batch of 25 messages is sent to various users, but the rate limit of at least one of them is 0, then the whole batch fails and no message is sent to any of the users.

You're given the logs of the sentBatches of messages your bot sent without setting the per user rate limit, and information about the receivedMessages. Which of the sent batches would fail if there was a per user rate limit with the initial value of startingAllowance?

Example

For

sentBatches = [[1471040000, 736273, 827482, 2738283],
               [1471040005, 736273, 2738283],
               [1471040010, 827482, 2738283],
               [1471040015, 2738283],
               [1471040025, 827482],
               [1471046400, 736273, 827482, 2738283]]
receivedMessages = [[1471040001, 2738283],
                    [1471040002, 2738283],
                    [1471040010, 827482],
                    [1471040020, 2738283]]
and startingAllowance = 1, the output should be

rateLimit(sentBatches, receivedMessages, startingAllowance) = [1, 4].

Here is why:

There are 3 recipients: 736273, 827482, 2738283. The per user rate limit for each of them is initially startingAllowance = 1.
At 1471040000 the first batch of messages is sent to each of the recipients, their per user rate limit after that equals 0.
At 1471040001 the first message is received from 2738283, so their per user rate limit is now equal to 1.
At 1471040002 the second message from 2738283 is received, increasing their per user limit to 2.
At 1471040005 the second batch of messages is sent. However, the current per user limit of the recipient 736273 is 0, so no new messages can be sent. The sending of the entire batch is canceled.
At 1471040010 two events happen almost simultaneously:
The user 827482 sends a message, which increases their per user limit by 1 (it's 1 now).
The third batch is sent. Now, the recipients limits are 0, 0, 1, respectively.
At 1471040015 the fourth batch is successfully sent.
At 1471040020 user 2738283 sends another message making their per user limit equal to 1.
At 1471040025 the fifth batch is supposed to be sent. However, user 827482 has per user limit equal to 0, so the batch isn't sent.
At 1471046400 the per user limits of all users are set to startingAllowance again (it's 00:00 in local server time). Thus, the last batch is successfully sent.
So, batches 2 and 5 (1 and 4 0-based) aren't sent.
"""



def rateLimit(sent_batches, received_messages, starting_allowance):
    rmessages = [(r[0], 'received', i, r[1:]) for i, r in enumerate(received_messages)]
    smessages = [(r[0], 'sent', i, r[1:]) for i, r in enumerate(sent_batches)]
    messages = rmessages + smessages
    messages.sort()

    users = {}
    not_sent = []
    previous_day = None
    for _utime, _type, _id, user_ids in messages:
        day = _utime / (24 * 3600)
        if previous_day is None or day - previous_day > 0:
            for uid in users:
                users[uid]['allowance'] = starting_allowance
        previous_day = day
        if _type == 'received':
            uid = user_ids[0]
            if uid not in users:
                users[uid] = {}
                users[uid]['allowance'] = starting_allowance
            users[uid]['allowance'] += 1

        if _type == 'sent':
            can_send = True
            for uid in user_ids:
                if uid not in users:
                    users[uid] = {}
                    users[uid]['allowance'] = starting_allowance
                if users[uid]['allowance'] == 0:
                    can_send = False
                    not_sent.append(_id)
                    break
            if can_send:
                for uid in user_ids:
                    users[uid]['allowance'] = max(0, users[uid]['allowance'] - 1)
    return not_sent
