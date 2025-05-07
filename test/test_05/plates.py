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
    l1 = s[0:2]
    # l2 = s[1:2]
    if l1.isalpha(): #and l2.isalpha():
        return True
    else:
        return False


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


if __name__ == '__main__':

    main()


