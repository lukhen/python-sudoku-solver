# Data definitions:
# Board: listOf Squares, length - 81
# Square: oneOf:
#          - Value
#          - None
# Value: Integer[0, 9]


def is_valid(bd: "Board") -> bool:
    if bd[0] == 1:
        return False
    else:
        return True


def solve(bd: "Board") -> "Board" or False:
    """
    Produce board with all squares filled,
    or False if it's unsolvable
    """
    if is_valid(bd):
        return bd
    else:
        return False
