def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if is_alphanumeric(s) is True \
            and first_two_letters(s) is True \
            and max_min_characters(s) is True \
            and numbers_at_the_end(s) is True \
            and zero_not_at_the_beginning(s) is True:

        return True
    else:
        return False


def first_two_letters(s):
    l1 = s[0:1]
    l2 = s[1:2]
    if l1.isalpha() and l2.isalpha():
        return True


def max_min_characters(s):
    if 7 > len(s) > 2:
        return True
    else:
        return False


def is_alphanumeric(s):
    if s.isalnum():
        return True
    else:
        return False


def numbers_at_the_end(s):
    l3 = s[2:3]
    l4 = s[3:4]
    l5 = s[4:5]
    l6 = s[5:6]
    if len(s) == 4 and l3.isdigit() and l4.isalpha():
        return False
    elif len(s) == 5 and l3.isdigit() and l4.isalpha():
        return False
    elif len(s) == 5 and l3.isdigit() and l5.isalpha():
        return False
    elif len(s) == 5 and l4.isdigit() and l5.isalpha():
        return False
    elif len(s) == 6 and l3.isdigit() and l4.isalpha():
        return False
    elif len(s) == 6 and l3.isdigit() and l5.isalpha():
        return False
    elif len(s) == 6 and l3.isdigit() and l6.isalpha():
        return False
    elif len(s) == 6 and l4.isdigit() and l5.isalpha():
        return False
    elif len(s) == 6 and l4.isdigit() and l6.isalpha():
        return False
    elif len(s) == 6 and l5.isdigit() and l6.isalpha():
        return False
    else:
        return True


def zero_not_at_the_beginning(s):
    s_list = list(s)
    n_list = []

    for i in s_list:
        if i.isdigit():
            n_list.append(i)
        else:
            pass
    if len(n_list) == 0:
        return True
    elif n_list[0] != "0":
        return True


main()


# AI code :
def is_valid_vanity_plate(plate):
    # Check length constraints
    if not (2 <= len(plate) <= 6):
        return False

    # Ensure first two characters are letters
    if not plate[:2].isalpha():
        return False

    # Check that numbers, if present, are only at the end
    index = 0
    while index < len(plate) and plate[index].isalpha():
        index += 1

    if index < len(plate):  # A number was found
        if plate[index] == '0':  # First number must not be '0'
            return False
        while index < len(plate):
            if not plate[index].isdigit():
                return False  # A letter appears after numbers, which is invalid
            index += 1

    return True


# Ask for user input
user_plate = input("Enter your vanity plate: ").strip().upper()  # Convert to uppercase for consistency
if is_valid_vanity_plate(user_plate):
    print("Valid")
else:
    print("Invalid")
