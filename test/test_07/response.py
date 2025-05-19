from validator_collection import checkers, validators


def main():
    print(validate(input("What's your email address? ")))


def validate(mail):
    is_valid = checkers.is_email(mail)

    if is_valid:
        return "Valid"
    else:
        return "Invalid"


if __name__ == "__main__":
    main()
