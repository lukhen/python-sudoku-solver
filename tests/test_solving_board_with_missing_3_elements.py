from sudoku_solver import solve
import pytest
import itertools

B = None


# @pytest.mark.slow
# @pytest.mark.parametrize(
#     "name, blank_indices",
#     [
#         ("{}".format(indices), indices)
#         for indices in itertools.combinations(range(0, 81), 3)
#     ],
# )
# def test_missing_3_elements(name, blank_indices):
#     # fmt: off
#     bd_solved = [3, 9, 6, 2, 7, 8, 4, 5, 1,
#                  4, 8, 5, 9, 1, 3, 7, 2, 6,
#                  2, 7, 1, 6, 4, 5, 8, 3, 9,
#                  5, 4, 7, 8, 2, 9, 6, 1, 3,
#                  8, 1, 2, 7, 3, 6, 5, 9, 4,
#                  6, 3, 9, 4, 5, 1, 2, 8, 7,
#                  1, 5, 8, 3, 6, 4, 9, 7, 2,
#                  7, 6, 3, 5, 9, 2, 1, 4, 8,
#                  9, 2, 4, 1, 8, 7, 3, 6, 5]

#     bd_unsolved = bd_solved[:]
#     for blank_index in blank_indices:
#         bd_unsolved[blank_index] = B

#     assert solve(bd_unsolved) == bd_solved
# fmt: on
