"""
N candles are placed in a row, some of them are initially lit. For each candle from the 1st to the Nth the following algorithm is applied: if the observed candle is lit then states of this candle and all candles before it are changed to the opposite. Which candles will remain lit after applying the algorithm to all candles in the order they are placed in the line?

Example

For a = [1, 1, 1, 1, 1], the output should be
switchLights(a) = [0, 1, 0, 1, 0].

Check out the image below for better understanding:

For a = [0, 0], the output should be
switchLights(a) = [0, 0].

The candles are not initially lit, so their states are not altered by the algorithm.
"""


def switchLights(a):
    counter = sum(a)
    for i, n in enumerate(a):
        if counter % 2 != 0:
            a[i] = abs(n - 1)
        if n == 1:
            counter -= 1
    return a
