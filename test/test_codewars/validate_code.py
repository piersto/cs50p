import re


def main():
    inpt = input("")
    validator(inpt)


def validator(code):

    pattern = r"^1|^2|^3\d*$"

    match = re.search(pattern, str(code))

    if match:
        return True
    else:
        return False


main()