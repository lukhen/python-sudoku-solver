from sudoku_solver import solve


def test_already_solved():
    # fmt: off
    bd_solved = [3, 9, 6, 2, 7, 8, 4, 5, 1,
                 4, 8, 5, 9, 1, 3, 7, 2, 6,
                 2, 7, 1, 6, 4, 5, 8, 3, 9,
                 5, 4, 7, 8, 2, 9, 6, 1, 3,
                 8, 1, 2, 7, 3, 6, 5, 9, 4,
                 6, 3, 9, 4, 5, 1, 2, 8, 7,
                 1, 5, 8, 3, 6, 4, 9, 7, 2,
                 7, 6, 3, 5, 9, 2, 1, 4, 8,
                 9, 2, 4, 1, 8, 7, 3, 6, 5]
    # fmt: on
    assert solve(bd_solved) == bd_solved


def test_full_and_invalid():
    # fmt: off
    # '1' twice in first column and row
    bd_full_invalid = [1, 9, 6, 2, 7, 8, 4, 5, 1,
                       4, 8, 5, 9, 1, 3, 7, 2, 6,
                       2, 7, 1, 6, 4, 5, 8, 3, 9,
                       5, 4, 7, 8, 2, 9, 6, 1, 3,
                       8, 1, 2, 7, 3, 6, 5, 9, 4,
                       6, 3, 9, 4, 5, 1, 2, 8, 7,
                       1, 5, 8, 3, 6, 4, 9, 7, 2,
                       7, 6, 3, 5, 9, 2, 1, 4, 8,
                       9, 2, 4, 1, 8, 7, 3, 6, 5]
    # fmt: on
    assert solve(bd_full_invalid) is False
