"""
Once you complete your own job application you can refer your friends and make some cash once they get hired! Your unique referral URL is located on the right sidebar (you can also find the same URL here).



In order to track all referrals we save referrerIds in JSON user objects in our databse. A simplified user object has the following fields.

{
  "_id": "glwer6kn7767spok",
  "username": "JohnSmith",
  "country": "US",
  "referrerId": "wsa2fsf43hfsfdsddd"
}
Note that referrerId can be null or missing from the object, which means that no other user has referred them.

Since we pay $500 per hired referral, we want to track how much we would potentially owe to each user in case all of their referrals get hired by our partner companies.

More specifically, you are given an array of user objects (stringified JSONs) and you need to return an array of strings in the following form username $x which means that username can earn at most $x in referral bonuses. Output must be sorted by lexicographical order of usernames.

Example

For
userInfo = "[{\"_id\": \"glwer6kn7767spok\",\"username\": \"JohnSmith\",\"country\": \"US\",\"referrerId\": \"wsa2fsf43hfsfdsddd\"},{\"_id\": \"wsa2fsf43hfsfdsddd\",\"username\": \"Michael\",\"country\": \"US\"},{\"_id\": \"tt222hbakq23asddd\",\"username\": \"Frank01\",\"country\": \"UK\",\"referrerId\": \"wsa2fsf43hfsfdsddd\"}]", the output should be referFriends(userInfo) = ["Frank01 $0", "JohnSmith $0", "Michael $1000"].;
"""

import collections
import json

def referFriends(userInfo):
    users = collections.defaultdict(dict)
    userInfo = json.loads(userInfo)
    for user in userInfo:
        users[user.get('_id')] = {
            'earned': 0,
            'username': user.get('username')
        }
    for user in userInfo:
        if user.get('referrerId'):
            users[user['referrerId']]['earned'] += 500
    return sorted(["{0} ${1}".format(d['username'], d['earned']) for d in users.values()])