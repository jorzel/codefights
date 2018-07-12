"""
You were supposed to prepare a presentation about lists in Python, but totally forgot about it. Now that you don't have enough time for it, you decide to show some usage examples instead and say with the poker face that this is how you understood the assignment.

Now you need to implement a function that will display a list in the console. Implement a function that, given a list lst, will return it as a string as follows: "This is your list: lst".

Example

For lst = [1, 2, 3, 4, 5], the output should be
printList(lst) = "This is your list: [1, 2, 3, 4, 5]".

"""


def printList(lst):
    return "This is your list: [%s]" % ', '.join([str(p) for p in lst])
