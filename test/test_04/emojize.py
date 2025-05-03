import emoji


def main():
    e = input("Input: ")
    print(emoji.emojize(e, language='alias'))


if __name__ == '__main__':

    main()
