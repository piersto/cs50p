import random


def main():
    get_level()
    ...


def get_level():
    while True:
        level = input("Level: ")
        try:
            if not level.isdigit():
                continue
            elif not 0 < int(level) < 4:
                continue
            else:
                break
        except ValueError:
            continue
    return int(level)


def generate_integer(level):
    pass

    # level 1
    # generate 2 lists of


if __name__ == "__main__":
    main()
