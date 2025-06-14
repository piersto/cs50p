def main():
    yell("This", "is", "CS50")


def yell(*words):
    #  usage of map function to build a list
    uppercased = map(str.upper, words)

    #  list comprehension -->
    uppercased = [word.upper() for word in words]

    print(*uppercased)


main()
