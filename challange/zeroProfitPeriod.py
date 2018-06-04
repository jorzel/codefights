"""
Lindsey, a small fox, has a bank account. She has a list of her transactions during some period of time. Negative transactions[i] means that the money leaves the account, and positive transactions[i] means that money is added to the account.

Lindsey refers to the sum of consecutive transactions as the profit of these transactions. She wants to find the maximum number of non-overlapping periods of consecutive transactions with zero profit. Please, help the fox.

Example

For transactions = [1, 1, 2, -3, 0, 1000, 6, -6, 1, 1, 1, -3, 2], the output should be
zeroProfitPeriods(transactions) = 4.

The periods [1, 2, -3], [0], [6, -6], [1, 1, 1, -3] are each zero-profit. Also, the periods [1, 2, -3], [0], [6, -6], [1, -3, 2] are zero-profit as well.
"""

def prefix_sums(A):
    n = len(A)
    P = [0] * (n + 1)
    for k in xrange(1, n + 1):
        P[k] = P[k - 1] + A[k - 1]
    return P

def zeroProfitPeriods(transactions):
    counter = 0
    _length = len(transactions)
    _prefix_sums = prefix_sums(transactions)
    occurance = {}
    for i, s in enumerate(_prefix_sums):
        if s not in occurance:
            occurance[s] = i
        else:       
            counter += 1
            occurance = {s: i}
    return counter