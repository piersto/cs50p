from .response import validate


def test_validate():
    s = "malan@harvard.edu"
    r = validate(s)
    assert r is "Valid"


def test_validate_2():
    s = "psto@yahoo.co.uk"
    r = validate(s)
    assert r is "Valid"


def test_validate_3():
    s = "malan@@@harvard.edu"
    r = validate(s)
    assert r is "Invalid"


def test_validate_4():
    s = "psto@.yahoo..com"
    r = validate(s)
    assert r is "Invalid"
