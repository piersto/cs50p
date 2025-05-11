import pytest
from .convert import convert


def test_convert_int():
    assert convert(1) == 1 * 149597870700
    assert convert(50) == 50 * 149597870700


def test_error():
    with pytest.raises(TypeError):
        convert("1")


def test_convert_float():
    assert convert(99.99) == 99.99 * 149597870700
    assert convert(0.001) == pytest.approx(149597870.71, abs=1e-2)  # 1e-2 equals 0.01 or 1/100!
    print(0.001 * 149597870700)  # 149597870.70000002
