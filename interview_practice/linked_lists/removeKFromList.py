"""
Given a singly linked list of integers l and an integer k, remove all elements from list l that have a value equal to k.

Example

For l = [3, 1, 2, 3, 4, 5] and k = 3, the output should be
removeKFromList(l, k) = [1, 2, 4, 5];
For l = [1, 2, 3, 4, 5, 6, 7] and k = 10, the output should be
removeKFromList(l, k) = [1, 2, 3, 4, 5, 6, 7].
"""

# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def removeKFromList(l, k):
    if not l:
        return None
    elif l.value == k:
        l = l.next
    n = l
    while True:
        if not n or not n.next:
            break
        if n.next.value == k:
            n.next = n.next.next
        else:
            n = n.next
    
    if n and n.value == k:
        l = l.next
    return l