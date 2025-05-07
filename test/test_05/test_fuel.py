from .fuel_2 import *
import pytest


def test_gauge():
    assert gauge(77) == "77%"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(1) == "E"
    assert gauge(0) == "E"


def test_convert():
    assert convert("6/6") == 100
    assert convert("99/100") == round((99/100)*100)
    assert convert("1/100") == round((1/100)*100)
    assert convert("100/100") == 100
    assert convert("7/8") == round((7/8)*100)


def test_convert_exceptions():
    with pytest.raises(ValueError):
        convert("50")
    with pytest.raises(ValueError):
        convert("3/2")
    with pytest.raises(ZeroDivisionError):
        convert("5/0")
