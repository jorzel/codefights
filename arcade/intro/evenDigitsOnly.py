"""
Check if all digits of the given integer are even.

Example

For n = 248622, the output should be
evenDigitsOnly(n) = true;
For n = 642386, the output should be
evenDigitsOnly(n) = false.
"""


def evenDigitsOnly(n):
    el_list = [int(i) for i in str(n)]
    for p in el_list:
        if p % 2 != 0:
            return False
    return True
