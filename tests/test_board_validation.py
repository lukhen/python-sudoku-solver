from sudoku_solver import is_valid

B = None


def test_empty_board():
    # fmt: off
    empty_bd = [B, B, B, B, B, B, B, B, B,
                B, B, B, B, B, B, B, B, B,
                B, B, B, B, B, B, B, B, B,
                B, B, B, B, B, B, B, B, B,
                B, B, B, B, B, B, B, B, B,
                B, B, B, B, B, B, B, B, B,
                B, B, B, B, B, B, B, B, B,
                B, B, B, B, B, B, B, B, B,
                B, B, B, B, B, B, B, B, B]
    # fmt: on
    assert is_valid(empty_bd) is True
