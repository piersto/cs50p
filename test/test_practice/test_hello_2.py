import pytest
from .hello_2 import hello


#
# def test_hello():
#     with pytest.raises(AttributeError):
#         hello(1)


def test_hello_default():
    assert hello("David") == "Hello, David"


def test_hello_default():
    assert hello() == "Hello, world"
