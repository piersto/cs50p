import re


def main():
    code = input("Hexadecimal color code: ").upper()

    pattern = r"^#[A-F0-9]{6}$"

    match = re.search(pattern, code)

    if match:
        print(f"Valid. Matched with {match.group()}")
    else:
        print("Invalid")


main()
