import random


def main():
    level = get_level()
    score = 0
    for _ in range(10):
        n1 = generate_integer(level)
        n2 = generate_integer(level)
        i = 0
        while i < 3:
            try:
                result = input(f"{str(n1)} + {str(n2)} = ")
                if int(result) != n1 + n2:
                    print("EEE")
                    i += 1
                    continue
                else:
                    score += 1
                    break
            except ValueError:
                i += 1
                print("EEE")
                continue
        else:
            print(f"{str(n1)} + {str(n2)} = {str(n1 + n2)}")
    print(f"Score: {str(score)}")


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
    if level == 1:
        n = random.randint(0, 9)
    elif level == 2:
        n = random.randint(10, 99)
    else:
        n = random.randint(100, 999)
    return n


if __name__ == "__main__":
    main()
