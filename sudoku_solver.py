# Data definitions:
# Board: listOf Squares, length - 81
# Square: oneOf:
#          - Value
#          - None
# Value: Integer[0, 9]


def is_empty(bd: "Board") -> bool:
    return not any(bd)

def has_duplicates(row):
    first_row_without_blanks = [sq for sq in row if sq is not None]
    return len(first_row_without_blanks) != len(set(first_row_without_blanks))

def is_valid(bd: "Board") -> bool:
    if is_empty(bd):
        return True

    first_row = [bd[0], bd[1], bd[2], bd[3], bd[4], bd[5], bd[6], bd[7], bd[8]]
    if has_duplicates(first_row):
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
