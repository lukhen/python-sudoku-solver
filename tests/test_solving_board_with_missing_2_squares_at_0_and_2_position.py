from sudoku_solver import solve

B = None


def test_missing_3_and_6():
    # fmt: off
    bd = [B, 9, B, 2, 7, 8, 4, 5, 1,
          4, 8, 5, 9, 1, 3, 7, 2, 6,
          2, 7, 1, 6, 4, 5, 8, 3, 9,
          5, 4, 7, 8, 2, 9, 6, 1, 3,
          8, 1, 2, 7, 3, 6, 5, 9, 4,
          6, 3, 9, 4, 5, 1, 2, 8, 7,
          1, 5, 8, 3, 6, 4, 9, 7, 2,
          7, 6, 3, 5, 9, 2, 1, 4, 8,
          9, 2, 4, 1, 8, 7, 3, 6, 5]
    
    assert solve(bd) == \
        [3, 9, 6, 2, 7, 8, 4, 5, 1,
         4, 8, 5, 9, 1, 3, 7, 2, 6,
         2, 7, 1, 6, 4, 5, 8, 3, 9,
         5, 4, 7, 8, 2, 9, 6, 1, 3,
         8, 1, 2, 7, 3, 6, 5, 9, 4,
         6, 3, 9, 4, 5, 1, 2, 8, 7,
         1, 5, 8, 3, 6, 4, 9, 7, 2,
         7, 6, 3, 5, 9, 2, 1, 4, 8,
         9, 2, 4, 1, 8, 7, 3, 6, 5]
    # fmt: on


def test_missing_1_and_3():
    # fmt: off
    bd = [B, 2, B, 4, 5, 6, 7, 8, 9,
          7, 8, 9, 1, 2, 3, 4, 5, 6,
          4, 5, 6, 7, 8, 9, 1, 2, 3,
          3, 1, 2, 8, 4, 5, 9, 6, 7,
          6, 9, 7, 3, 1, 2, 8, 4, 5,
          8, 4, 5, 6, 9, 7, 3, 1, 2,
          2, 3, 1, 5, 7, 4, 6, 9, 8,
          9, 6, 8, 2, 3, 1, 5, 7, 4,
          5, 7, 4, 9, 6, 8, 2, 3, 1]
    
    assert solve(bd) == \
        [1, 2, 3, 4, 5, 6, 7, 8, 9,
         7, 8, 9, 1, 2, 3, 4, 5, 6,
         4, 5, 6, 7, 8, 9, 1, 2, 3,
         3, 1, 2, 8, 4, 5, 9, 6, 7,
         6, 9, 7, 3, 1, 2, 8, 4, 5,
         8, 4, 5, 6, 9, 7, 3, 1, 2,
         2, 3, 1, 5, 7, 4, 6, 9, 8,
         9, 6, 8, 2, 3, 1, 5, 7, 4,
         5, 7, 4, 9, 6, 8, 2, 3, 1]

    # fmt: on


def test_missing_2_and_3():
    # fmt: off
    bd = [B, 1, B, 4, 5, 6, 7, 8, 9,
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


def test_missing_5_and_4():
    # fmt: off
    bd = [B, 3, B, 6, 7, 8, 9, 1, 2,
          6, 7, 2, 1, 9, 5, 3, 4, 8,
          1, 9, 8, 3, 4, 2, 5, 6, 7,
          8, 5, 9, 7, 6, 1, 4, 2, 3,
          4, 2, 6, 8, 5, 3, 7, 9, 1,
          7, 1, 3, 9, 2, 4, 8, 5, 6,
          9, 6, 1, 5, 3, 7, 2, 8, 4,
          2, 8, 7, 4, 1, 9, 6, 3, 5,
          3, 4, 5, 2, 8, 6, 1, 7, 9]

    assert solve(bd) == \
        [5, 3, 4, 6, 7, 8, 9, 1, 2,
         6, 7, 2, 1, 9, 5, 3, 4, 8,
         1, 9, 8, 3, 4, 2, 5, 6, 7,
         8, 5, 9, 7, 6, 1, 4, 2, 3,
         4, 2, 6, 8, 5, 3, 7, 9, 1,
         7, 1, 3, 9, 2, 4, 8, 5, 6,
         9, 6, 1, 5, 3, 7, 2, 8, 4,
         2, 8, 7, 4, 1, 9, 6, 3, 5,
         3, 4, 5, 2, 8, 6, 1, 7, 9]
    # fmt: on
