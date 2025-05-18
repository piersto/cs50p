import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):

    try:
        pattern = r"(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$"

        match = re.match(pattern, ip)
        first_group = match.group(1)
        second_group = match.group(2)
        third_group = match.group(3)
        fourth_group = match.group(4)

        if not match:
            print(f"False")
            return False
        elif int(first_group) > 255 or int(first_group) < 0:
            print(f"False")
            return False
        elif int(second_group) > 255 or int(first_group) < 0:
            print(f"False")
            return False
        elif int(third_group) > 255 or int(first_group) < 0:
            print(f"False")
            return False
        elif int(fourth_group) > 255 or int(first_group) < 0:
            print(f"False")
            return False
        else:
            print("True")
            return True
    except AttributeError:
        print("False")
        return False


if __name__ == "__main__":
    main()