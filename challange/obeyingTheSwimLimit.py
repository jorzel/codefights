"""
Medium

Codewriting

1000

Summer's here! You can't think of a better way to spend the day than going for a swim at the local beach! However, the normal lifeguard (let's call him Larry) isn't on duty. It's his pain of an accomplice, Robert.

Now Bob is pretty strict. Rumor has it that he can't swim. Therefore, to protect himself, he enforces a strict no swimming after eating rule. Here are the parts of the rule:

Calories Consumed	Time to Wait (minutes)
0-600	0
601-1400	15
1401-2000	30
2001+	60
Given an array of various foods eaten, output how long you should wait before swimming.

Food	Calories
Banana	100
Apple	80
Pizza	300
Chocolate	500
Roast Beef	850
Milk	110
Chicken	300
Deluxe Burger
"""

def time_to_wait(calories):
    if calories in range(0, 601):
        return 0
    elif calories in range(601, 1401):
        return 15
    elif calories in range(1401, 2001):
        return 30
    else:
        return 60

def obeyingTheSwimLimit(intake):
    table = {
        'Banana': 100,
        'Apple': 80,
        'Pizza': 300,
        'Chocolate': 500,
        'Roast Beef': 850,
        'Milk': 110,
        'Chicken': 300,
        'Deluxe Burger': 1000
    }    

    return time_to_wait(sum([table[p] for p in intake]))
