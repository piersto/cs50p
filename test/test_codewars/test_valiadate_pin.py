import re
import pytest
from .validate_pin import validate_pin


def test_validate_pin():
    pin = "123456.0"
    assert validate_pin(pin) is False
