"""
Easy

Recovery

100

Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
Fibonacci sequence is known to every programmer, and you're not an exception. It is believed that not all properties of Fibonacci numbers are yet studied, and in order to help your descendants, you'd like to implement a generator that will generate Fibonacci numbers infinitely. Who knows, maybe in the distant future your generator will help to make a breakthrough in this field!

To test your generator, you'd like to check the first few values. Given the number n, return the first n numbers of Fibonacci sequence.

Example

For n = 3, the output should be
fibonacciGenerator(n) = [0, 1, 1].

The first three Fibonacci numbers are 0, 1 and 1.
"""


def fibonacciGenerator(n):
    def fib():
        last = (0, 1)
        while True:
            yield last[0]
            last = last[0] + last[1], last[0]

    gen = fib()
    return [next(gen) for _ in range(n)]