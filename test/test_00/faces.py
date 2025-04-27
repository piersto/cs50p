def main():
    s = input()
    convert(s)


def convert(s):
    s = s.replace(":)", "🙂")
    s = s.replace(":(", "🙁")
    print(s)


main()
