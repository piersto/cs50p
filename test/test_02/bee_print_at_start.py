# https://www.youtube.com/watch?v=3zJoCpvKhx4&ab_channel=CS50

WORDS = {"PAIR": 4, "HAIR": 4, "CHAIR": 5, "GRAPHIC": 7}


def main():
    print("Welcom to spelling bee")

    for key, value in WORDS.items():
        print(f"{key} was worth {value} points")


if __name__ == '__main__':
    main()
