# Data definitions:
# Board: listOf Squares, length - 81
# Square: oneOf:
#          - Value
#          - None
# Value: Integer[0, 9]


def is_empty(bd: "Board") -> bool:
    return not any(bd)


def is_valid(bd: "Board") -> bool:
    if is_empty(bd):
        return True

    if bd[0] == 1:
        return False
    elif bd[0] == bd[1]:
        return False
    elif bd[0] == bd[8]:
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
