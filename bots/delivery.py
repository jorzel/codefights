"""
Instacart customers are able to set the delivery window during which they want to receive their groceries. There are always plenty of shoppers in the area ready to take a customer's order, but unfortunately they can't always do it right away. Before taking an order a shopper wants to ensure they will make it in time. They also don't want to stay idle, so arriving early isn't an option either.

Our task is to implement an algorithm that determines whether shoppers should take the given order or not.

For each shopper you know their travel speed, distance to the store and the estimated amount of time they will spend there. Figure out which of them can take the order, assuming it is known when the customer wants to receive the groceries and the distance between their house and the store.

Example

For order = [200, 20, 15] and shoppers = [[300, 40, 5], [600, 40, 10]], the output should be

delivery(order, shoppers) = [false, true].

The store is located 200 m away from the customer's house.

The customer will be ready to receive the groceries in 20 minutes, but they shouldn't be delivered more than 15 minutes late.

The first shopper is 300 m away from the store, his speed is 40 m/min, and he will spend 5 minutes in the store, which means that he will need (300 + 200) / 40 + 5 = 17.5 minutes to fulfill the order. This will leave him with 20 - 17.5 = 2.5 idle minutes, so he shouldn't take the order.

The second shopper is 600 m away from the store, his speed is 40 m/min, and he will spend 10 minutes in the store, which means it will take him (600 + 200) / 40 + 10 = 30 minutes to fulfill the order. The customer can wait for 20 + 15 = 35 minutes, which means that the shopper will make it in time.
"""


def count_time(distance, v, delta):
    return delta + distance / (1.0 * v)

def delivery(order, shoppers):
    result = []
    for s in shoppers:
        t = count_time(order[0] + s[0], s[1], s[2])
        if t >= order[1] and t <= order[1] + order[2]:
            result.append(True)
        else:
            result.append(False)
    return result
