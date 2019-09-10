import pytest
from sudoku_solver import solve

B = None  # Blank square
# fmt: off
s1 = [5, 3, B, B, 7, B, B, B, B,
      6, B, B, 1, 9, 5, B, B, B,
      B, 9, 8, B, B, B, B, 6, B,
      8, B, B, B, 6, B, B, B, 3,
      4, B, B, 8, B, 3, B, B, 1,
      7, B, B, B, 2, B, B, B, 6,
      B, 6, B, B, B, B, 2, 8, B,
      B, B, B, 4, 1, 9, B, B, 5,
      B, B, B, B, 8, B, B, 7, 9]

s1_solved = [5, 3, 4, 6, 7, 8, 9, 1, 2,
             6, 7, 2, 1, 9, 5, 3, 4, 8,
             1, 9, 8, 3, 4, 2, 5, 6, 7,
             8, 5, 9, 7, 6, 1, 4, 2, 3,
             4, 2, 6, 8, 5, 3, 7, 9, 1,
             7, 1, 3, 9, 2, 4, 8, 5, 6,
             9, 6, 1, 5, 3, 7, 2, 8, 4,
             2, 8, 7, 4, 1, 9, 6, 3, 5,
             3, 4, 5, 2, 8, 6, 1, 7, 9]
# fmt: on


def test_e2e():
    assert solve(s1) == s1_solved
