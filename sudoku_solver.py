# Data definitions:
# Board: listOf Squares, length - 81
# Square: oneOf:
#          - Value
#          - None
# Value: Integer[0, 9]

# fmt: off
ROW_INDICES = [[0, 1, 2, 3, 4, 5, 6, 7, 8],
               [9, 10, 11, 12, 13, 14, 15, 16, 17],
               [18, 19, 20, 21, 22, 23, 24, 25, 26],
               [27, 28, 29, 30, 31, 32, 33, 34, 35],
               [36, 37, 38, 39, 40, 41, 42, 43, 44],
               [45, 46, 47, 48, 49, 50, 51, 52, 53],
               [54, 55, 56, 57, 58, 59, 60, 61, 62],
               [63, 64, 65, 66, 67, 68, 69, 70, 71],
               [72, 73, 74, 75, 76, 77, 78, 79, 80]]
# fmt: on


def is_empty(bd: "Board") -> bool:
    return not any(bd)


def has_duplicates(row):
    first_row_without_blanks = [sq for sq in row if sq is not None]
    return len(first_row_without_blanks) != len(set(first_row_without_blanks))


def is_valid(bd: "Board") -> bool:
    if is_empty(bd):
        return True

    first_row = [bd[i] for i in ROW_INDICES[0]]
    second_row = [bd[i] for i in ROW_INDICES[1]]
    third_row = [bd[i] for i in ROW_INDICES[2]]
    if has_duplicates(first_row):
        return False
    elif has_duplicates(second_row):
        return False
    elif has_duplicates(third_row):
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
