from datetime import *
import inflect
import sys


def main():
    try:
        date_of_birth = input("Date of Birth:")
    except ValueError:
        sys.exit(1)
    print(f"{int_to_words(date_of_birth)} minutes")


def get_delta(d):
    try:
        date_of_birth = date.fromisoformat(d)
    except ValueError:
        sys.exit(1)
    today = date.today()
    t_delta = today - date_of_birth
    delta_sec = t_delta.total_seconds() / 60
    delta_min = round(delta_sec)
    return delta_min


def int_to_words(d):
    p = inflect.engine()
    delta_as_str = p.number_to_words(get_delta(d))
    delta_as_str = delta_as_str.replace("and ", "")
    return delta_as_str.capitalize()


if __name__ == "__main__":
    main()
