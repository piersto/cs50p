import pytest

from .jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0


def test_init_size():
    jar = Jar()
    assert jar.size == 0


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    with pytest.raises(ValueError):
        jar = Jar()
        jar.deposit(13)


def test_withdraw():
    jar = Jar()
    jar.deposit(12)
    jar.withdraw(10)
    assert jar.size == 2
