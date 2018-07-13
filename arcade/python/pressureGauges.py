"""
Easy

Recovery

100

Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
Harry dropped out of school to pursue his dreams and work in Pipes Corporations. He is now in charge of a lot of pipes, and his task is to check the gauges twice a day. By analyzing the morning and evening pressures of each pipe, Harry should write a report about the minimum and the maximum pressure during the day.

Given the pressures Harry wrote down for each pipe, return two lists: the first one containing the minimum, and the second one containing the maximum pressure of each pipe during the day.

Example

For morning = [3, 5, 2, 6] and evening = [1, 6, 6, 6],
the output should be
pressureGauges(morning, evening) = [[1, 5, 2, 6], [3, 6, 6, 6]].
"""


def pressureGauges(morning, evening):
    return zip(*[(min(x,y), max(x,y)) for x,y in zip(morning, evening)])