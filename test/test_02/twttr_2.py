def main():

    word = input("Input: ")
    print(shorten(word))


def shorten(word):
    word_as_list = list(word)
    tw_as_list = []
    letters_to_be_excluded = ["a", "o", "e", "u", "i", "A", "O", "E", "U", "I"]

    for i in range(len(word_as_list)):
        if word_as_list[i] not in letters_to_be_excluded:
            tw_as_list.append(word_as_list[i])

    return ''.join(tw_as_list)


if __name__ == '__main__':
    main()
