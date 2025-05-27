from .seasons import get_delta, int_to_words
import pytest


def test_get_delta():
    s = "2024-05-21"
    assert get_delta(s) == 525600


def test_get_delta_two_years():
    s = "2023-05-21"
    assert get_delta(s) == 1052640


def test_get_delta_invalid_empty_str():
    s = ""
    with pytest.raises(SystemExit) as sample:
        get_delta(s)
    assert sample.type == SystemExit
    assert sample.value.code == 1


def test_get_delta_invalid():
    s = "12:00 AM to 20:59 PM"
    with pytest.raises(SystemExit) as sample:
        get_delta(s)
    assert sample.type == SystemExit
    assert sample.value.code == 1


def test_get_delta_invalid_2():
    s = "12:00 AM to 20:59 PM"
    with pytest.raises(SystemExit) as sample:
        get_delta(s)
    assert sample.type == SystemExit
    assert sample.value.code == 1


def test_get_delta_invalid_3():
    s = "31-01-2000"
    with pytest.raises(SystemExit) as sample:
        get_delta(s)
    assert sample.type == SystemExit
    assert sample.value.code == 1


def test_int_to_words():
    i = "2024-05-21"
    s_out = int_to_words(i)
    assert s_out == 'Five hundred twenty-five thousand, six hundred'
