from .working_2 import convert
import pytest


def test_working():
    w_hours = "9:00 AM to 5:00 PM"
    converted_w_h = convert(w_hours)
    print(converted_w_h)
    assert converted_w_h == "09:00 to 17:00"


def test_working_2():
    w_hours = "9 AM to 5 PM"
    converted_w_h = convert(w_hours)
    print(converted_w_h)
    assert converted_w_h == "09:00 to 17:00"


def test_working_3():
    w_hours = "9:00 AM to 5 PM"
    converted_w_h = convert(w_hours)
    print(converted_w_h)
    assert converted_w_h == "09:00 to 17:00"


def test_working_4():
    w_hours = "9 AM to 5:00 PM"
    converted_w_h = convert(w_hours)
    print(converted_w_h)
    assert converted_w_h == "09:00 to 17:00"


def test_working_5():
    w_hours = "10:30 PM to 8 AM"
    converted_w_h = convert(w_hours)
    print(converted_w_h)
    assert converted_w_h == "22:30 to 08:00"


def test_working_6():
    w_hours = "10 AM to 8:50 PM"
    converted_w_h = convert(w_hours)
    print(converted_w_h)
    assert converted_w_h == "10:00 to 20:50"


def test_working_7():
    w_hours = "12 AM to 12 PM"
    converted_w_h = convert(w_hours)
    print(converted_w_h)
    assert converted_w_h == "00:00 to 12:00"


def test_working_8():
    w_hours = "12 PM to 12 AM"
    converted_w_h = convert(w_hours)
    print(converted_w_h)
    assert converted_w_h == "12:00 to 00:00"


def test_working_invalid_string():
    w_hours = "10 AM to 8:50 PM "
    with pytest.raises(ValueError):
        convert(w_hours)


def test_working_invalid_hour_start():
    w_hours = "13 AM to 8:59 PM"
    with pytest.raises(ValueError):
        convert(w_hours)


def test_working_invalid_min_start():
    w_hours = "12:60 AM to 8:59 PM"
    with pytest.raises(ValueError):
        convert(w_hours)


def test_working_invalid_hour_end():
    w_hours = "12:00 AM to 20:59 PM"
    with pytest.raises(ValueError):
        convert(w_hours)


def test_working_invalid_min_end():
    w_hours = "12 AM to 8:60 PM"
    with pytest.raises(ValueError):
        convert(w_hours)


def test_working_invalid_no_to():
    w_hours = "12 AM    8:30 PM"
    with pytest.raises(ValueError):
        convert(w_hours)


def test_working_invalid_do_not_to():
    w_hours = "12 AM do 8:30 PM"
    with pytest.raises(ValueError):
        convert(w_hours)


def test_working_invalid_no_m():
    w_hours = "12 AD to 8:30 PM"
    with pytest.raises(ValueError):
        convert(w_hours)