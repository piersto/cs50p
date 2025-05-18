from .numb3rs import validate


def test_validate():
    ip = "255.255.255.255"
    assert validate(ip) is True


def test_validate_0():
    ip = "0.0.0.0"
    assert validate(ip) is True


def test_validate_256():
    ip = "256.0.0.0"
    assert validate(ip) is False


def test_validate_512_512_512_512():
    ip = "512.512.512.512"
    assert validate(ip) is False


def test_validate_1_2_3_1000():
    ip = "512.512.512.512"
    assert validate(ip) is False


def test_validate_cat():
    ip = "cat"
    assert validate(ip) is False


def test_validate_0_256():
    ip = "0.256.0.0"
    assert validate(ip) is False


def test_validate_invalid_string():
    ip = "0 . 256 . 0 . 0"
    assert validate(ip) is False


def test_validate_invalid_10_10_10_10_10():
    ip = "10.10.10.10.10"
    assert validate(ip) is False

def test_validate_valid_string():
    ip = "127.0.0.1"
    assert validate(ip) is True

