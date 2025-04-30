import random


def main():
    moisture = sample()

    while moisture > 20.00:
        moisture = sample()
        print("Moisture is " + str(moisture))

    print("Time to water!")


def sample():
    return random.random() * 100


if __name__ == '__main__':
    main()
