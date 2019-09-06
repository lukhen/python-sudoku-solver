# Data definitions:
# Board: listOf Squares, length - 81
# Square: oneOf:
#          - Value
#          - None
# Value: Integer[1, 9]

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

BOX_INDICES = [[0, 1, 2, 9, 10, 11, 18, 19, 20],
               [3, 4, 5, 12, 13, 14, 21, 22, 23],
               [6, 7, 8, 15, 16, 17, 24, 25, 26],
               [27, 28, 29, 36, 37, 38, 45, 46, 47],
               [30, 31, 32, 39, 40, 41, 48, 49, 50],
               [33, 34, 35, 42, 43, 44, 51, 52, 53],
               [54, 55, 56, 63, 64, 65, 72, 73, 74],
               [57, 58, 59, 66, 67, 68, 75, 76, 77],
               [60, 61, 62, 69, 70, 71, 78, 79, 80]]

UNIT_INDICES = ROW_INDICES + COLUMN_INDICES + BOX_INDICES
# fmt: on


def is_empty(bd: "Board") -> bool:
    return not any(bd)


def has_duplicates(row):
    row_without_blanks = [sq for sq in row if sq is not None]
    return len(row_without_blanks) != len(set(row_without_blanks))


def is_valid(bd: "Board") -> bool:
    if is_empty(bd):
        return True

    units = [[bd[i] for i in unit] for unit in UNIT_INDICES]

    if any([has_duplicates(unit) for unit in units]):
        return False
    else:
        return True


def replace_square(bd, square, value):
    return [*bd[:square], value, *bd[square + 1 :]]


def solve(bd: "Board") -> "Board" or False:
    """
    Produce board with all squares filled,
    or False if it's unsolvable
    """
    if not is_valid(bd):
        return False

    if all(bd):
        return bd

    if has_exactly_one_blank_square(bd):
        possible_boards_with_first_blank_square_filled = [
            valid_board
            for valid_board in [
                replace_square(bd, find_single_blank_square(bd), val)
                for val in range(1, 10)
            ]
            if is_valid(valid_board)
        ]
        if possible_boards_with_first_blank_square_filled:
            return possible_boards_with_first_blank_square_filled[0]
    elif squares_0_and_1_blank(bd) or squares_0_and_2_blank(bd):
        possible_boards_with_first_blank_square_filled = [
            valid_board
            for valid_board in [
                replace_square(bd, find_first_blank_square(bd), value)
                for value in range(1, 10)
            ]
            if is_valid(valid_board)
        ]
        possible_boards_with_both_blank_squares_filled = [
            valid_board
            for valid_board in [
                replace_square(
                    partial_solution, find_first_blank_square(partial_solution), value
                )
                for value in range(1, 10)
                for partial_solution in possible_boards_with_first_blank_square_filled
            ]
            if is_valid(valid_board)
        ]

        if possible_boards_with_both_blank_squares_filled:
            return possible_boards_with_both_blank_squares_filled[0]

    return False


def find_first_blank_square(bd):
    for i in range(0, 81):
        if bd[i] is None:
            return i


def squares_0_and_2_blank(bd):
    return bd[0] is None and bd[2] is None


def squares_0_and_1_blank(bd):
    return bd[0] is None and bd[1] is None


def has_exactly_one_blank_square(bd):
    return find_single_blank_square(bd) is not None


def find_single_blank_square(bd):

    blank_square = None
    for i in range(0, 81):
        if bd[i] is None and all([*bd[:i], *bd[i + 1 :]]):
            blank_square = i

    return blank_square
