"""
Medium

Codewriting

4000

When visualizing market data over a long period of time, it is often helpful to build an Open-high-low-close (OHLC) chart. However, to build an OHLC chart you first need to prepare some data. For each financial instrument consider each day when it was traded, and find the following prices the instrument had that day:

open price: the price of the first trade of the day;
high price: the highest trade of the day;
low price: the lowest trade of the day;
close price: the price of the last trade of the day.
Given a stream of trade data ordered by time, write a program to compute the OHLC by day and instrument (see output section for the format details).
If two trades happen to have equal timestamps, then their order is determined by the order of their timestamps in the timestamp array.

Example

For

timestamp = [1450625399, 1450625400, 1450625500, 
             1450625550, 1451644200, 1451690100, 1451691000]
instrument = ["HPQ", "HPQ", "HPQ", "HPQ", "AAPL", "HPQ", "GOOG"],
side = ["sell", "buy", "buy", "sell", "buy", "buy", "buy"],
price = [10, 20.3, 35.5, 8.65, 20, 10, 100.35], and
size = [10, 1, 2, 3, 5, 1, 10], the output should be

dailyOHLC(timestamp, instrument, side, price, size) = 
[["2015-12-20", "HPQ", "10.00", "35.50", "8.65", "8.65"],
 ["2016-01-01", "AAPL", "20.00", "20.00", "20.00", "20.00"],
 ["2016-01-01", "GOOG", "100.35", "100.35", "100.35", "100.35"],
 ["2016-01-01", "HPQ", "10.00", "10.00", "10.00", "10.00"]]
 """


from datetime import datetime

def format_price(price):
    return "{:.2f}".format(price)


def format_datetime(timestamp):
    return datetime.fromtimestamp(int(timestamp)).strftime('%Y-%m-%d')


def dailyOHLC(timestamps, instruments, sides, prices, sizes):
    table = {}
    results = []
    for timestamp, instrument, price in zip(timestamps, instruments, prices):
        current_date = format_datetime(timestamp)
        if current_date not in table:
            table[current_date] = {}
        if instrument not in table[current_date]:
            table[current_date][instrument] = [price, price, price, price]
        else:
            if price > table[current_date][instrument][1]:
                table[current_date][instrument][1] = price
            if price < table[current_date][instrument][2]:
                table[current_date][instrument][2] = price
            table[current_date][instrument][3] = price

    for current_date in table:
        for instrument in table[current_date]:
            results.append([
                current_date,
                instrument,
                format_price(table[current_date][instrument][0]),
                format_price(table[current_date][instrument][1]),
                format_price(table[current_date][instrument][2]),
                format_price(table[current_date][instrument][3])
            ])    
    return sorted(results)