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

COLUMN_INDICES = [[0, 9, 18, 27, 36, 45, 54, 63, 72],
                  [1, 10, 19, 28, 37, 46, 55, 64, 73],
                  [2, 11, 20, 29, 38, 47, 56, 65, 74],
                  [3, 12, 21, 30, 39, 48, 57, 66, 75],
                  [4, 13, 22, 31, 40, 49, 58, 67, 76],
                  [5, 14, 23, 32, 41, 50, 59, 68, 77],
                  [6, 15, 24, 33, 42, 51, 60, 69, 78],
                  [7, 16, 25, 34, 43, 52, 61, 70, 79],
                  [8, 17, 26, 35, 44, 53, 62, 71, 80]]
# fmt: on


def is_empty(bd: "Board") -> bool:
    return not any(bd)


def has_duplicates(row):
    row_without_blanks = [sq for sq in row if sq is not None]
    return len(row_without_blanks) != len(set(row_without_blanks))


def is_valid(bd: "Board") -> bool:
    if is_empty(bd):
        return True

    all_rows = [[bd[i] for i in row] for row in ROW_INDICES]
    all_cols = [[bd[i] for i in col] for col in COLUMN_INDICES]
    first_box = [bd[0], bd[1], bd[2], bd[9], bd[10], bd[11], bd[18], bd[19], bd[20]]
    second_box = [bd[3], bd[4], bd[5], bd[12], bd[13], bd[14], bd[21], bd[22], bd[23]]

    if any([has_duplicates(row) for row in all_rows]):
        return False
    elif any([has_duplicates(col) for col in all_cols]):
        return False
    elif has_duplicates(first_box):
        return False
    elif has_duplicates(second_box):
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
