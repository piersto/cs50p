import pytest

from .hello import hello


def test_argument():
    assert hello("Pierre") == "Hello, Pierre"


def test_default():
    assert hello() == "Hello, world"


def test_hello_exception():
    with pytest.raises(ValueError):
        hello(1)


