"""
Before delivery, all orders at Jet are packed into boxes to protect them from damage.

Consider a package pkg of a given size that needs to be packed into a box chosen from a list of available boxes. The package should fit inside the box, keeping in mind that the size of the package should not exceed the size of the box in any dimension (note that the package can be rotated to fit and it can be positioned upside down). For the sake of efficiency, among the available boxes that fit, the one with smallest volume should be chosen.

Given a package pkg and available boxes, find the 0-based index of the smallest-by-volume box such that the package fits inside it, or return -1 if there is no such box.

Example

For pkg = [4, 2, 5] and boxes = [[4, 3, 5], [5, 2, 5]], the output should be
packageBoxing(pkg, boxes) = 1.
The package fits into both boxes, but the volume of the first one (4 * 3 * 5 = 60) is greater than the volume of the second (5 * 5 * 2 = 50).

For pkg = [4, 4, 2] and boxes = [[2, 4, 4], [4, 4, 3]], the output should be
packageBoxing(pkg, boxes) = 0.
The package can fit into the first box if it is rotated, and into the second box as-is, but the first box is chosen because it has less volume overall.

For pkg = [4, 5, 3] and boxes = [[3, 10, 2], [2, 6, 7], [1, 1, 1]], the output should be
packageBoxing(pkg, boxes) = -1.
The package doesn't fit into any of the available boxes.
"""


import sys

def get_volume(box):
    return box[0] * box[1] * box[2]

def rotate(box):
    box = [x for x in box]
    a = min(box)
    c = max(box)
    box.remove(a)
    box.remove(c)
    return a, box[0], c
    
def packageBoxing(pkg, boxes):
    volume = get_volume(pkg)
    pkg = rotate(pkg)
    min_volume = sys.maxint
    index = -1
    for i, box in enumerate(boxes):
        box = rotate(box)
        if box[0] >= pkg[0] and box[1] >= pkg[1] and box[2] >= pkg[2]:
            volume = get_volume(box)
            if volume < min_volume:
                index = i
                min_volume = volume
    return index
