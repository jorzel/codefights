"""
Medium

Codewriting

2000

You're probably used to measuring temperature in Celsius degrees, but there's also a lesser known temperature scale called Fahrenheit, which is used in only 5 countries around the world.

You can convert a Celsius temperature (C) to Fahrenheit (F), by using the following formula:

F = 9 * C / 5 + 32

Your friend lives in Palau (where the Fahrenheit system is used), and you've been trying to find out which of you lives in a warmer climate, so you've each kept track of your respective daily temperatures for the past n days.

Given two arrays of integers yourTemps and friendsTemps (each of length n), representing the local daily temperatures (in Celsius and Fahrenheit, respectively), find how many days were hotter in Palau.

Example

For yourTemps = [25, 32, 31, 27, 30, 23, 27] and friendsTemps = [78, 83, 86, 88, 86, 89, 79], the output should be celciusVsFahrenheit(yourTemps, friendsTemps) = 3.

Converting your recorded temperatures to Fahrenheit gives the results [77, 89.6, 87.8, 80.6, 86, 73.4, 80.6], which can be compared to the temperatures your friend recorded:

your temps	friend's temps
77	78
89.6	83
87.8	86
80.6	88
86	86
73.4	89
80.6	79
There were 3 days where your friend recorded hotter temperatures, so the answer is 3.

"""


def to_fahrenheit(temp):
    return float(9 * temp) / 5 + 32 

def celsiusVsFahrenheit(yourTemps, friendsTemps):
    counter = 0
    for you, friend in zip(yourTemps, friendsTemps):
        if friend > to_fahrenheit(you):
            counter += 1
    return counter