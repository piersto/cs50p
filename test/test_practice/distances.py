distances = {
    "voyager": "163",
    "pioner": "80"
    }


def main():
    while True:
        spacecraft = input("Enter spacecraft's name: ")
        try:
            au = float(distances[spacecraft])
        except ValueError:
            print(f"Can't convert '{distances[spacecraft]}' to number")
        except KeyError:
            print(f"I don't have information for {spacecraft}. Try another one")
        else:
            break
    m = convert(au)
    print(f"m away {m}")


def convert(au):
    return au * 149597870700


if __name__ == '__main__':
    main()
