from sudoku_solver import solve

B = None


def test_finding_a_missing_3_at_position_0_0():
    # fmt: off
    bd = [B, 9, 6, 2, 7, 8, 4, 5, 1,
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
