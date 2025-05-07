def main():
    name = input("what's your name? ")
    print(hello(name))


def hello(greeting="world"):
    try:
        greeting.isalpha()
    except AttributeError:
        print("This is not string but number")
    else:
        return f"Hello, {greeting}"


if __name__ == '__main__':
    main()
