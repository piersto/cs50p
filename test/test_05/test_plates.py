import pytest
from .plates import is_valid


def test_is_valid_first_two_letters():
    assert is_valid("AA5555") == True


def test_is_valid_alphanumeric():
    assert is_valid("AA5555") == True
    assert is_valid("AAA555") == True
    assert is_valid("AAAA55") == True
    assert is_valid("AAAAA5") == True
    assert is_valid("AAAAAA") == True


def test_is_valid_is_alphanumeric():
    assert is_valid("AAA55@") == False
    assert is_valid("AAA5#@") == False
    assert is_valid("AAA$$@") == False
    assert is_valid("AA####") == False
    assert is_valid("A@####") == False
    assert is_valid("@@####") == False


def test_is_valid_is_min_characters():
    assert is_valid("A") == False


def test_is_valid_numbers():
    assert is_valid("44") == False


def test_zero_not_at_the_beginning():
    assert is_valid("AAA012") == False


def test_is_valid_is_max_characters():
    assert is_valid("AAA1234") == False


def test_is_valid_is_starts_with_letters():
    assert is_valid("123AAA") == False
    assert is_valid("50CS") == False
    assert is_valid("50") == False


def test_is_valid_is_no_digits_in_the_middle():
    assert is_valid("Aa3AAA") == False


def test_is_valid_first_letters():
    assert is_valid("A55555") == False


def test_is_valid_first_second_letters():
    assert is_valid("AA5555") == True


def test_is_valid_first_second_letters_2():
    assert is_valid("5A5555") == False


def test_is_valid_lowercase():
    assert is_valid("ABCDEF") == True


def test_is_valid_just_numbers():
    assert is_valid("111111") == False
