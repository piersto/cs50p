from .um import count


def test_count_10():
    s = " um "
    length = count(s)
    assert length == 1


def test_count_9():
    s = "Um? Mum? Is this that album where, um, umm, the clumsy alums play drums?"

    length = count(s)

    assert length == 2


def test_count_8():
    s = "album "
    length = count(s)
    assert length == 0


def test_count_7():
    s = "Um "
    length = count(s)
    assert length == 1


def test_count_6():
    s = "This is, um... CS50."
    length = count(s)
    assert length == 1


def test_count_5():
    s = " um, "
    length = count(s)
    assert length == 1


def test_count_4():
    s = " um "
    length = count(s)
    assert length == 1


def test_count_3():
    s = "Um, album"
    length = count(s)
    assert length == 1


def test_count_2():
    s = "Um, "
    length = count(s)
    assert length == 1


def test_count_1():
    s = "Um"
    length = count(s)
    assert length == 1


def test_count():
    s = ""
    length = count(s)
    assert length == 0