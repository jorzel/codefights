"""
Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.

Example

For inputArray = [3, 6, -2, -5, 7, 3], the output should be
adjacentElementsProduct(inputArray) = 21.

7 and 3 produce the largest product.
"""


def adjacentElementsProduct(inputArray):
    size = len(inputArray)
    max_product = 1000 * -1000
    for i in xrange(0, size - 1):
        product = inputArray[i] * inputArray[i + 1]
        if product > max_product:
            max_product = product
    return max_product
