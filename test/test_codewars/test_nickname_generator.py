import pytest
import re
from .nickname_generator import nickname_generator


def test_nickname_generator():
    s = "Robert"
    nick = nickname_generator(s)
    assert nick == "Rob"


def test_nickname_generator_1():
    s = "Jeannie"
    nick = nickname_generator(s)
    assert nick == "Jean"

