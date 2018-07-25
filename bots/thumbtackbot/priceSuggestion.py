"""
Medium

Codewriting

1000

When a customer submits a job request on Thumbtack, this information is sent to Pros in the area who might be interested in it. If it looks like there's a fit, a Pro can respond with a custom quote that includes a personal message and a price estimate.

Thumbtack tries to help Pros pick a price estimate range using historical contractData, which contains prices for the same job type in the same area. You have been asked to implement the following two-step price suggestion algorithm:

In the first step, contractData, which is guaranteed to have an even length, is sorted and divided into two groups:
the first group contains the first half of the elements in contractData.
the second group contains the other half;
In the second step, the median values of the first and the second groups are found:
the median of the first group is rounded down and returned as the lower price bound;
the median of the second group is rounded up and returned as the upper price bound.
If the data is insufficient (i.e. contractData contains fewer than 2 elements), a suggestion cannot be made, so nothing should be returned.
Using the given contractData, find the lower and the upper bounds of the suggested price estimate range.

Example

For contractData = [10, 15, 14, 7, 11, 15], the output should be
priceSuggestion(contractData) = [10, 15].
The first step produces groups [7, 10, 11] and [14, 15, 15];
The second step returns 10 and 15.
For contractData = [], the output should be
priceSuggestion(contractData) = [].
"""


from math import ceil

def median(arr):
    _length = len(arr)
    if _length % 2 == 0:
        return (arr[_length/2-1] + arr[_length/2]) / 2.0
    else:
        return arr[_length/2]

def priceSuggestion(contractData):
    _length = len(contractData)
    if _length < 2:
        return []
    contractData = sorted(contractData) 
    first = contractData[:_length/2]
    second = contractData[_length/2:]
    if len(first) % 2 == 0:
        return [int(median(first)), ceil(median(second))]
    else:
        return [median(first), median(second)]