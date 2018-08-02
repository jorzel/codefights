"""
Medium

Recovery

100

Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
In a large and famous supermarket a new major campaign was launched. From now on, each nth customer has a chance to win a prize: a brand new luxury car! However, it's not that simple. A customer wins a prize only if the total price of their purchase is divisible by d. This number is kept as a secret, so the customers don't know in advance how much they should spend on their purchases. The winners will be announced once the campaign is over.

Your task is to implement a function that will determine the winners. Given the purchases of some customers over time, return the 1-based indices of all the customers who won the prize, i.e. each nth who spend on their purchases amount of money divisible by d.

Example

For purchases = [12, 43, 13, 465, 1, 13], n = 2, and d = 3,
the output should be
superPrize(purchases, n, d) = [4].

Each second customer has a chance to win a car, which makes customers 2, 4 and 6 potential winners. Customer number 2 spent 43 on his purchase, which is not divisible by 3. 13 also is not divisible by 3, so the sixth customer also doesn't get the price. Customer 4, however, spent 465, which is divisible by 3, so he is the only lucky guy.
"""

class Prizes(object):
    def __init__(self, purchases, n, d):
        self.i = 1
        self.purchases = purchases
        self.n = n
        self.d = d

    def __iter__(self):
        return self

    def next(self):
        if self.i < len(self.purchases) + 1:
            i = self.i
            self.i += 1
            if i % self.n == 0 and self.purchases[i-1] % self.d == 0:
                return i
            else:
                return self.next()        
        else:
            raise StopIteration

def superPrize(purchases, n, d):
    return list(Prizes(purchases, n, d))
