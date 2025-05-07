from .bank import value


def test_value_hello():
    greeting = "hello"
    cash = value(greeting)
    assert 0 == cash


def test_value_hi():
    greeting = "hi"
    cash = value(greeting)
    assert 20 == cash


def test_value_whatsup():
    greeting = "what's up?"
    cash = value(greeting)
    assert 100 == cash


def test_value_special_character():
    greeting = "¿Qué pasa?"
    cash = value(greeting)
    assert 100 == cash


def test_value_digit():
    greeting = "100% good?"
    cash = value(greeting)
    assert 100 == cash


def test_value_case_insensitive():
    greeting = "Hello"
    cash = value(greeting)
    assert 0 == cash
