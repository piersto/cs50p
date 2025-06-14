from .test_test import calculate_age


def test_test():

    a = "2012"
    b = "2012"

    assert calculate_age(a, b ) == "You were born this very year!"


def test_test_2():

    a = "900"
    b = "2900"

    assert calculate_age(a, b ) == "You are 2000 years old."


def test_test_3():

    a = "2900"
    b = "900"

    assert calculate_age(a, b ) == "You will be born in 2000 years."

def test_test_4():

    a = "2000"
    b = "2001"

    assert calculate_age(a, b ) == "You are 1 year old."

def test_test_5():

    a = "2001"
    b = "2000"

    assert calculate_age(a, b ) == "You will be born in 1 year."