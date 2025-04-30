# Shorts Dictionaries
# https://cs50.harvard.edu/python/2022/shorts/dictionaries/#dictionaries

distances = {
    "Voyager 1": 163,
    "Voyager 2": 136,
}


def main():
    for name in distances.keys():
        print(f"{distances[name]} {name}")


if __name__ == '__main__':
    main()
