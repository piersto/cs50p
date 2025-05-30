import re


def main():
    n = input("What's your name ")
    print(nickname_generator(n))


def nickname_generator(name):
    # cons = r"[bcdfghjklmnpqrstvwxyz]"
    vowl = r"[aoeui]"
    #   If the 3rd letter is a consonant, return the first 3 letters.
    # match_c = re.match(cons, name[2])
    #  If the 3rd letter is a vowel, return the first 4 letters.
    match_v = re.search(vowl, name[2:3])

    if len(name) < 4:
        return "Error: Name too short"
    elif match_v:
        return name[:4]
    else:
        pass
    return name[:3]


if __name__ == '__main__':
    main()
