"""
Given two cells on the standard chess board, determine whether they have the same color or not.

Example

For cell1 = "A1" and cell2 = "C3", the output should be
chessBoardCellColor(cell1, cell2) = true.


For cell1 = "A1" and cell2 = "H3", the output should be
chessBoardCellColor(cell1, cell2) = false.
"""

def prepare_tuple(cell):
    table = {
        'A': 1,
        'B': 2,
        'C': 3,
        'D': 4,
        'E': 5,
        'F': 6,
        'G': 7,
        'H': 8
    }
    return (int(table[cell[0]]), int(cell[1]))

def get_color(input_tuple):
    l = input_tuple[0] % 2
    r = input_tuple[1] % 2
    return ((r and l) or (not r and not l)) == 0

def chessBoardCellColor(cell1, cell2):
    return get_color(prepare_tuple(cell1)) == get_color(prepare_tuple(cell2))
