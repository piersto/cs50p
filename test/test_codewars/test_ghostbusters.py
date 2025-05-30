import pytest
from .ghostbusters import ghostbusters


def test_ghostbusters():
    s = "Sky scra per"
    assert ghostbusters(s) == "Skyscraper"
