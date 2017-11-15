"""
If you have a task that you need to complete on a regular basis, you can set it up in Asana as a recurring task. This allows you to schedule the task to repeat on specific days of the week every k weeks.

For instance, you could set up a recurring task that reminds you to call your sister on Tuesday and Friday every 3 weeks. You set up the first instance of the task for Tuesday, March 1. The next instance will fall on Friday, March 4. The third instance will fall 3 weeks later on Tuesday, March 22, the fourth instance will fall on Friday, March 25, the fifth instance will fall on Tuesday, April 12, and so on.

Given a firstDate that represents the day your recurring task becomes active, an array daysOfTheWeek that indicates which days of the week the task should occur on, and a number k that represents the interval between weeks on which the task occurs, return an array that contains the first n dates on which the task is scheduled.

In this task, you'll likely need to know the how long the months are and the names of the days of week, provided here:

Month lengths from January to December: 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31.
During leap years February has 29 days.
Names of weekdays: "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday".
January 1, 2015 was a Thursday.
Example

For firstDate = "01/01/2015", k = 2, daysOfTheWeek = ["Monday", "Thursday"] and n = 4, the output should be

recurringTask(firstDate, k, daysOfTheWeek, n) = 
    ["01/01/2015", "05/01/2015", "15/01/2015", "19/01/2015"]


firstDate falls on a Thursday. The first Monday after it is January 5, "05/01/2015". Since k = 2, the next two days for which the task is scheduled are Thursday, January 15, and Monday, January 19.
"""


import datetime
from itertools import cycle, islice

days = {
    "Monday": 0,
    "Tuesday": 1,
    "Wednesday": 2,
    "Thursday": 3,
    "Friday": 4,
    "Saturday": 5,
    "Sunday": 6,
}


def recurringTask(first_date, k, days_of_the_week, n): 
    first_date = datetime.datetime.strptime(first_date, "%d/%m/%Y")
    day_name = first_date.strftime("%A")

    start_ind = [i for i, d in enumerate(days_of_the_week) if d == day_name][0]
    cycle_list = list(islice(cycle(days_of_the_week), start_ind, start_ind+n))

    diffs = [days[d] - days[day_name] if (days[d] - days[day_name]) >= 0 else (days[d] - days[day_name]) + 7 for d in cycle_list]

    counter, _diff = 0, 0
    deltas = []
    for i, d in zip(cycle_list, diffs):
        if counter == len(days_of_the_week):
            _diff += k * 7
            counter = 0
        counter += 1
        delta = datetime.timedelta(days=d + _diff)
        deltas.append((first_date + delta).strftime('%d/%m/%Y'))
    return deltas
