import inflect


def main():
    names = []
    while True:
        try:
            name = input("Name: ")
            names.append(name)
        except EOFError:
            p = inflect.engine()
            names_edited = p.join(names)
            print(f"Adieu, adieu, to {names_edited}")
            break


main()
