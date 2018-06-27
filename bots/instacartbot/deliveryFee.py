"""
To make sure that groceries can always be delivered, Instacart tries to equally distribute delivery requests throughout the day by including an additional delivery fee during busy periods.

Each day is divided into several intervals that do not overlap and cover the whole day from 00:00 to 23:59. For each i the delivery fee in the intervals[i] equals fees[i].

Given the list of delivery requests deliveries, your task is to check whether the delivery fee is directly correlated to the order volume in each interval i.e. the interval_fee / interval_deliveries value is constant for each interval throughout the day.

Example

For
intervals = [0, 10, 22], fees = [1, 3, 1] and

deliveries = [[8, 15],
              [12, 21], 
              [15, 48], 
              [20, 17], 
              [23, 43]]
the output should be
deliveryFee(intervals, fees, deliveries) = true.

The day is divided into 3 intervals:

from 00:00 to 09:59, the first delivery was made, fees[0] / 1 = 1;
from 10:00 to 21:59, the 2nd, 3rd and 4th deliveries were made, fees[1] / 3 = 1;
from 22:00 to 23:59, the last delivery was made, fees[2] / 1 = 1.
interval_fee / interval_deliveries = 1 for each interval, so the answer is true.

Check out the image below for better understanding:
"""


from collections import defaultdict

def deliveryFee(intervals, fees, deliveries):
    counter = defaultdict(int)
    for hour, minutes in deliveries:
        counter[hour] += 1
    interval_counter = defaultdict(int)
    intervals.append(24)
    for i in range(len(intervals) - 1):
        for j in range(intervals[i], intervals[i+1]):
            if j in counter:
                interval_counter[intervals[i]] += counter[j]

    if len(fees) != len(interval_counter):
        return False
    value = None
    for fee, count in zip(fees, interval_counter.values()):
        if fee == 0:
            if count != 0:
                return False
        if value is None:
            value = count / float(fee) 
        else:
            if count / float(fee) != value:
                return False
    return True