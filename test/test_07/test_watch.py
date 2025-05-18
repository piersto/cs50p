from .watch import parse


def test_parse():
    s = '<iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>'
    result = parse(s)
    assert result == "https://www.youtu.be/xvFZjo5PgG0"


def test_parse_2():
    s = '<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" ' \
        'title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; ' \
        'clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
    result = parse(s)
    assert result == "https://www.youtu.be/xvFZjo5PgG0"


def test_parse_3():
    s = '<iframe src="http://youtube.com/embed/xvFZjo5PgG0"></iframe>'
    result = parse(s)
    assert result == "https://www.youtu.be/xvFZjo5PgG0"


def test_parse_none():
    s = '<iframe width="560" height="315" src="https://www.com/embed/xvFZjo5PgG0" ' \
        'title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; ' \
        'clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
    assert parse(s) is None


def test_parse_none_2():
    s = '<iframe width="560" height="315" src="https://cs50.harvard.edu/python"></iframe>'
    assert parse(s) is None