import pytest
from .explode import explode


def test_expload():
    s = "312"
    assert explode(s) == "333122"