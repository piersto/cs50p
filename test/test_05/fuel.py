def main():
    print(gauge(convert()))


def convert():

    while True:
        f = input("Fraction: ")
        try:
            x, y = f.split("/")
        except ValueError:
            continue
        else:
            try:
                int(y) <= 0 or int(x) > int(y)
            except ValueError:
                continue
            else:
                try:
                    int(x) / int(y)
                except ZeroDivisionError:
                    continue
                else:
                    if int(x) > int(y):
                        continue
                    else:
                        return round((int(x) / int(y)) * 100)


def gauge(percentage):
    if 100 >= percentage >= 99:
        return "F"
    elif 1 >= percentage >= 0:
        return "E"
    else:
        return str(percentage) + "%"


if __name__ == '__main__':
    main()
