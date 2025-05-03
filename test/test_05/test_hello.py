from .hello import hello


def test_argument():
    assert hello("Pierre") == "Hello, Pierre"


