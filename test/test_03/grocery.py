def main():
    d = {}
    while True:
        try:
            item = input()
            item = item.strip().upper()
            if item in d:
                x = d[item] + 1
                d.update({item: x})
            else:
                d.update({item: 1})
        except EOFError:
            break

    k_list = sorted(list(d.keys()))
    for i in k_list:
        print(f"{d[i]} {i}")


if __name__ == '__main__':
    main()
