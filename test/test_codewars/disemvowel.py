import re

def main():
    print(disemvowel("how are you "))


def disemvowel(string_):
    string_ = re.sub(r"[aoeui]", "", string_)
    return string_

main()