def is_valid(s):
    if s[0] == 1:
        return False
    else:
        return True


def solve(s):
    if is_valid(s):
        return s
    else:
        return False
