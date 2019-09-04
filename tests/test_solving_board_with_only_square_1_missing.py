from sudoku_solver import solve

B = None


def test_missing_1():
    # fmt: off
    bd = [2, B, 3, 4, 5, 6, 7, 8, 9,
          7, 8, 9, 2, 1, 3, 4, 5, 6,
          4, 5, 6, 7, 8, 9, 2, 1, 3,
          3, 2, 1, 8, 4, 5, 9, 6, 7,
          6, 9, 7, 3, 2, 1, 8, 4, 5,
          8, 4, 5, 6, 9, 7, 3, 2, 1,
          1, 3, 2, 5, 7, 4, 6, 9, 8,
          9, 6, 8, 1, 3, 2, 5, 7, 4,
          5, 7, 4, 9, 6, 8, 1, 3, 2]

    assert solve(bd) == \
        [2, 1, 3, 4, 5, 6, 7, 8, 9,
         7, 8, 9, 2, 1, 3, 4, 5, 6,
         4, 5, 6, 7, 8, 9, 2, 1, 3,
         3, 2, 1, 8, 4, 5, 9, 6, 7,
         6, 9, 7, 3, 2, 1, 8, 4, 5,
         8, 4, 5, 6, 9, 7, 3, 2, 1,
         1, 3, 2, 5, 7, 4, 6, 9, 8,
         9, 6, 8, 1, 3, 2, 5, 7, 4,
         5, 7, 4, 9, 6, 8, 1, 3, 2]
    # fmt: on
