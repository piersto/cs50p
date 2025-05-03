from .calculator import square


def main():
    test_square()


def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-3) == 9
    assert square(-2) == 4
    # if square(2) != 4:
    #     print("All bad!!!")
    # if square(3) != 9:
    #     print("All bad")


if __name__ == '__main__':
    main()
