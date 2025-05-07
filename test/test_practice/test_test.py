def test_twitter():

    s = "ahotenusi"
    l = list(s)
    tw_as_list = []
    letters_to_be_excluded = ["a", "o", "e", "u", "i", "y"]

    for i in range(len(l)):
        if l[i] not in letters_to_be_excluded:
            tw_as_list.append(l[i])

    print(tw_as_list)
    print(''.join(tw_as_list))
