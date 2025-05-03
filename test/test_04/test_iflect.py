import inflect


def test_inflect():
    p = inflect.engine()
    l = ("pierre", "anais", "ivan")
    l_m = p.join(l)
    print(f"Hello {l_m}")
