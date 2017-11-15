"""
Given an integer product, find the smallest positive (i.e. greater than 0) integer the product of whose digits is equal to product. If there is no such integer, return -1 instead.

Example

For product = 12, the output should be
digitsProduct(product) = 26;
For product = 19, the output should be
digitsProduct(product) = -1.
"""


def digitsProduct(product):
    divisor = 9
    result = []
    if product == 0:
        return 10
    if product < 10:
        return product
    while product != 1:
        if divisor == 1:
            return -1
        if product % divisor != 0:
            divisor -= 1
            continue
        result.append(divisor)
        product = product / divisor
    return int(''.join([str(n) for n in result])[::-1])

