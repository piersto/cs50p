import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):

    x = re.findall(r"\b[uU]m\b", s)
    # for i in x:
    #     print(i)
    return len(x)


if __name__ == "__main__":
    main()
