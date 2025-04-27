def main():
    r = get_fraction()
    result(r)


def get_fraction():
    f = input("Fraction: ")
    return f


def result(f):
    while True:
        try:
            x, y = f.split("/")
        except ValueError:
            get_fraction()
        else:
            break
    while True:
        try:
            int(y) <= 0 or int(x) > int(y)
        except ValueError:
            get_fraction()
        else:
            break
    while True:
        try:
            int(x) / int(y)
        except ZeroDivisionError:
            get_fraction()
        else:
            break

    if int(x) > int(y):
        get_fraction()
    else:
        o = round((int(x) / int(y)) * 100)
        if 100 >= o >= 99:
            print("F")
        elif 1 >= o >= 0:
            print("E")
        else:
            print(str(o) + "%")


main()