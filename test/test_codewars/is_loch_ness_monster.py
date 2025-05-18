import re


def main():

    inpt = input("")
    is_loch_ness_monster(inpt)


def is_loch_ness_monster(string):

    if re.findall("3\.50 | tree fiddy", string):
        print("Match")
        return True
    elif re.findall("three fifty", string):
        print("Match: three fifty")
        return True

    else:
        print("Nope")
        return False

main()