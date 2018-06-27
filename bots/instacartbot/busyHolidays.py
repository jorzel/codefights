"""
To celebrate Cyber Monday, Instacart has decided to give its shoppers (employees that shop at grocery stores and deliver orders to customers) a break. For a 24h period, every shopper only has to make 1 delivery, after which his/her workday is over. However, since providing customers with a reliable shopping experience is Instacart's #1 priority, it is important to ensure that each order is fulfilled and delivered as promised.

You are given a list of orders with the time periods when they should be completed, and the time leadTime it takes to fulfill each order. Knowing the time period each shopper is available (shoppers), find out whether the current number of shoppers is enough to fulfill all orders.

A shopper can fulfill an order if he/she can both start and finish it in the time period specified for this order.

Example

For

shoppers = [["15:10", "16:00"], 
            ["17:40", "22:30"]]
orders = [["17:30", "18:00"], 
          ["15:00", "15:45"]]
and leadTime = [15, 30], the output should be
busyHolidays(shoppers, orders, leadTime) = true.

The first shopper can take the second order, and the second shopper can take the first one.

For

shoppers = [["15:10", "16:00"], 
            ["17:50", "22:30"], 
            ["13:00", "14:40"]]
orders = [["14:30", "15:00"]]
and leadTime = [15], the output should be
busyHolidays(shoppers, orders, leadTime) = false.

None of the shoppers can fulfill the given order. The first two will be unavailable at the time of the order and the last one won't be able to finish it in time, since the earliest time the order can be completed is 14:30 + 15 minutes = 14:45."""


from datetime import timedelta


def convert(str_time):
    h, m = str_time.split(':')
    return timedelta(minutes=int(m), hours=int(h))


def busyHolidays(shoppers, orders, leadTime):
    for o, lt in zip(orders, leadTime):
        start_task, end_task = convert(o[0]), convert(o[1])
        candidates = []
        for s in shoppers:
            start_shift, end_shift = convert(s[0]), convert(s[1])
            task_time = timedelta(minutes=int(lt))
            start = max(start_task, start_shift)
            end = min(end_task, end_shift)
            if end - start >= task_time:
                candidates.append((end_shift - start_shift, s))
        if len(candidates) > 0:
            orders.remove(o)
            candidates.sort()
            shoppers.remove(candidates[0][1])
    return len(orders) == 0
