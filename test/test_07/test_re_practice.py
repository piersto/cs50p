import re


def main():

    username = input("")
    validate_usr(username)


def validate_usr(username):

    pattern = r"^[a-z0-9_]{4,16}$"

    match = re.search(pattern, username)

    if match:
        print(f"Valid this part : {match.group()}")
    else:
        print("Invalid")


main()