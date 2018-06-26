"""
If you didn't know already, there is a very robus US based job platform on this website. We partner with hundreds of top tier tech companies to help our users get discovered and find their dream job by demonstrating their skills. As part of that, we've built a matching engine that identifies which candidates currently looking for a job are a good match for which jobs from our partner companies. The matching engine takes a lot of attributes into account, but location is one of the trickier ones. Your challenge is to build a highly simplified version of the matching engine limiting the scope to location matching only.

You're given a list of candidate locations in the following form "city, state, country", for example:

San Francisco, California, United States
..., ..., ...
..., ..., ...
Return the number of candidates matching the given job location criteria. The criteria can have one of the following 3 forms:

San Francisco, California, United States - candidates from the given city
California, United States - candidates from the given state
United States - candidates from the given country
Note that there can be multiple cities with the same name in different states, and there can be multiple states with the same name in different countries.

Example

For
locations = ["San Francisco, California, United States",
             "San Mateo, California, United States",
             "Columbia, South Carolina, United States",
             "Columbia, California, United States"]
and criteria = "United States", the output should be jobMatchingScore(locations, criteria) = 4.

All candidate locations match the given criteria (country only).

For
locations = ["San Francisco, California, United States",
             "San Mateo, California, United States",
             "Columbia, South Carolina, United States",
             "Columbia, California, United States"]
and criteria = "Columbia, South Carolina, United States", the output should be jobMatchingScore(locations, criteria) = 1.
"""


def jobMatchingScore(locations, criteria):
    criteria_split = criteria.split(', ')
    criteria_count = len(criteria_split)
    if criteria_count == 1:
        return len([x for x in locations if x.split(', ')[2] == criteria_split[0]])
    elif criteria_count == 2:
        return len([x for x in locations if x.split(', ')[1] == criteria_split[0] and x.split(', ')[2] == criteria_split[1]])
    else:
        return len([x for x in locations if x == criteria])
