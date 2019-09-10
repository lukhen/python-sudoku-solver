# Person is (name, list_of_person)
p1 = ("Andrea", [])
p2 = ("Bonnie", [])
p3 = ("Luise", [])
p4 = ("Andy", [])
p5 = ("Luke", [])
p6 = ("Bruce", [])
p7 = ("Jerry", [])
p16 = ("Eva", [])
p8 = ("Harry", [p1, p2])
p9 = ("John", [p8, p3])
p10 = ("Emily", [p4, p5])
p11 = ("Donald", [p7])
p12 = ("Roman", [p6, p11])
p13 = ("Ronald", [p12, p16])
p14 = ("Steve", [p9, p10, p13])


def find_names_d(root):
    def starts_with_d(p):
        l = [p[0]] if p[0].startswith("D") else []
        return l + find_names_d_list(p[1])

    def find_names_d_list(lop):
        res = []
        for p in lop:
            res += find_names_d(p)
        return res

    return starts_with_d(root)


def test_find_names_that_start_at_d():
    assert find_names_d(p14) == ["Donald"]


def find_first_donald(root):
    def find_donald_p(p):
        if p[0] == "Donald":
            return p
        else:
            return find_donald_lop(p[1])

    def find_donald_lop(lop):
        if len(lop) == 0:
            return False
        else:
            pom = find_donald_p(lop[0])
            if pom is not False:
                return pom
            else:
                return find_donald_lop(lop[1:])

    return find_donald_p(root)


def test_find_first_donald():
    assert find_first_donald(p14) == p11
