import re


def validate_pin(pin):
    pattern = r"(\d{4})|(\d{6})"
    match = re.fullmatch(pattern, pin)
    if match:
        return True
    else:
        return False
