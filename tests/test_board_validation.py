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


def test_almost_empty_board():
    # fmt: off
    empty_bd = [7, B, B, B, B, B, B, B, B,
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


def test_properly_solved_board():
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
    assert is_valid(bd_solved) is True


def test_mostly_empty_but_invalid_first_row():
    # fmt: off
    bd = [7, 7, B, B, B, B, B, B, B,
          B, B, B, B, B, B, B, B, B,
          B, B, B, B, B, B, B, B, B,
          B, B, B, B, B, B, B, B, B,
          B, B, B, B, B, B, B, B, B,
          B, B, B, B, B, B, B, B, B,
          B, B, B, B, B, B, B, B, B,
          B, B, B, B, B, B, B, B, B,
          B, B, B, B, B, B, B, B, B]
    # fmt: on
    assert is_valid(bd) is False


def test_invalid_first_row_2():
    # fmt: off
    bd = [7, B, B, B, B, B, B, B, 7,
          B, B, B, B, B, B, B, B, B,
          B, B, B, B, B, B, B, B, B,
          B, B, B, B, B, B, B, B, B,
          B, B, B, B, B, B, B, B, B,
          B, B, B, B, B, B, B, B, B,
          B, B, B, B, B, B, B, B, B,
          B, B, B, B, B, B, B, B, B,
          B, B, B, B, B, B, B, B, B]
    # fmt: on
    assert is_valid(bd) is False


def test_invalid_second_row():
    # fmt: off
    bd = [B, B, B, B, B, B, B, B, B,
          7, B, B, 7, B, B, B, B, B,
          B, B, B, B, B, B, B, B, B,
          B, B, B, B, B, B, B, B, B,
          B, B, B, B, B, B, B, B, B,
          B, B, B, B, B, B, B, B, B,
          B, B, B, B, B, B, B, B, B,
          B, B, B, B, B, B, B, B, B,
          B, B, B, B, B, B, B, B, B]
    # fmt: on
    assert is_valid(bd) is False


def test_invalid_second_row_2():
    # fmt: off
    bd = [B, B, B, B, B, B, B, B, B,
          7, B, B, B, B, B, B, B, 7,
          B, B, B, B, B, B, B, B, B,
          B, B, B, B, B, B, B, B, B,
          B, B, B, B, B, B, B, B, B,
          B, B, B, B, B, B, B, B, B,
          B, B, B, B, B, B, B, B, B,
          B, B, B, B, B, B, B, B, B,
          B, B, B, B, B, B, B, B, B]
    # fmt: on
    assert is_valid(bd) is False


def test_invalid_third_row():
    # fmt: off
    bd = [B, B, B, B, B, B, B, B, B,
          B, B, B, B, B, B, B, B, B,
          B, B, 5, B, B, 5, B, B, B,
          B, B, B, B, B, B, B, B, B,
          B, B, B, B, B, B, B, B, B,
          B, B, B, B, B, B, B, B, B,
          B, B, B, B, B, B, B, B, B,
          B, B, B, B, B, B, B, B, B,
          B, B, B, B, B, B, B, B, B]
    # fmt: on
    assert is_valid(bd) is False


def test_invalid_last_row():
    # fmt: off
    bd = [B, B, B, B, B, B, B, B, B,
          B, B, B, B, B, B, B, B, B,
          B, B, B, B, B, B, B, B, B,
          B, B, B, B, B, B, B, B, B,
          B, B, B, B, B, B, B, B, B,
          B, B, B, B, B, B, B, B, B,
          B, B, B, B, B, B, B, B, B,
          B, B, B, B, B, B, B, B, B,
          B, B, B, B, 2, B, B, B, 2]
    # fmt: on
    assert is_valid(bd) is False


def test_invalid_first_column():
    # fmt: off
    bd = [1, B, B, B, B, B, B, B, B,
          B, B, B, B, B, B, B, B, B,
          B, B, B, B, B, B, B, B, B,
          B, B, B, B, B, B, B, B, B,
          1, B, B, B, B, B, B, B, B,
          B, B, B, B, B, B, B, B, B,
          B, B, B, B, B, B, B, B, B,
          B, B, B, B, B, B, B, B, B,
          B, B, B, B, B, B, B, B, B]
    # fmt: on
    assert is_valid(bd) is False


def test_invalid_first_column_2():
    # fmt: off
    bd = [1, B, B, B, B, B, B, B, B,
          B, B, B, B, B, B, B, B, B,
          B, B, B, B, B, B, B, B, B,
          B, B, B, B, B, B, B, B, B,
          B, B, B, B, B, B, B, B, B,
          B, B, B, B, B, B, B, B, B,
          1, B, B, B, B, B, B, B, B,
          B, B, B, B, B, B, B, B, B,
          B, B, B, B, B, B, B, B, B]
    # fmt: on
    assert is_valid(bd) is False


def test_invalid_first_column_3():
    # fmt: off
    bd = [B, B, B, B, B, B, B, B, B,
          B, B, B, B, B, B, B, B, B,
          B, B, B, B, B, B, B, B, B,
          B, B, B, B, B, B, B, B, B,
          B, B, B, B, B, B, B, B, B,
          B, B, B, B, B, B, B, B, B,
          B, B, B, B, B, B, B, B, B,
          1, B, B, B, B, B, B, B, B,
          1, B, B, B, B, B, B, B, B]
    # fmt: on
    assert is_valid(bd) is False


def test_invalid_second_column():
    # fmt: off
    bd = [B, 1, B, B, B, B, B, B, B,
          B, B, B, B, B, B, B, B, B,
          B, B, B, B, B, B, B, B, B,
          B, B, B, B, B, B, B, B, B,
          B, B, B, B, B, B, B, B, B,
          B, B, B, B, B, B, B, B, B,
          B, B, B, B, B, B, B, B, B,
          B, B, B, B, B, B, B, B, B,
          B, 1, B, B, B, B, B, B, B]
    # fmt: on
    assert is_valid(bd) is False


def test_invalid_last_column():
    # fmt: off
    bd = [B, B, B, B, B, B, B, B, B,
          B, B, B, B, B, B, B, B, 1,
          B, B, B, B, B, B, B, B, B,
          B, B, B, B, B, B, B, B, B,
          B, B, B, B, B, B, B, B, B,
          B, B, B, B, B, B, B, B, B,
          B, B, B, B, B, B, B, B, B,
          B, B, B, B, B, B, B, B, 1,
          B, B, B, B, B, B, B, B, B]
    # fmt: on
    assert is_valid(bd) is False


def test_invalid_middle_column():
    # fmt: off
    bd = [B, B, B, B, B, B, B, B, B,
          B, B, B, 1, B, B, B, B, B,
          B, B, B, B, B, B, B, B, B,
          B, B, B, B, B, B, B, B, B,
          B, B, B, B, B, B, B, B, B,
          B, B, B, 1, B, B, B, B, B,
          B, B, B, B, B, B, B, B, B,
          B, B, B, B, B, B, B, B, B,
          B, B, B, B, B, B, B, B, B]
    # fmt: on
    assert is_valid(bd) is False
