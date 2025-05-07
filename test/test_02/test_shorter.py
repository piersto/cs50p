from .twttr_2 import shorten


def test_shorten_for_lowercase():
    twit = shorten("1a2o3e4u5i")
    assert twit == "12345"


def test_shorten_for_uppercase():
    twit = shorten("A1O2E3U4I5")
    assert twit == "12345"


def test_shorten_for_y_Y():
    twit = shorten("0Y9y")
    assert twit == "0Y9y"


def test_for_consonants():
    twit = shorten("B, C, D, F, G, H, J, K, L, M, N, P, Q, R, S, T, V, W, X, Y, Z")
    assert twit == "B, C, D, F, G, H, J, K, L, M, N, P, Q, R, S, T, V, W, X, Y, Z"


def test_special_characters():
    twit = shorten("´  & < > ’ ' @")
    assert twit == "´  & < > ’ ' @"
