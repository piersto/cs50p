import random


def main():
    while True:
        n = input("Level: ")
        try:
            if not n.isdigit():
                continue
            elif not int(n) >= 1:
                continue
            else:
                break
        except ValueError:
            continue

    generated_number = random.randrange(1, int(n) + 1)
    print(f"This is generated number: {generated_number}")

    while True:
        guess_n = input("Guess: ")
        try:
            if not guess_n.isdigit():
                continue
            elif int(guess_n) > int(generated_number):
                print("Too large!")
                continue
            elif int(guess_n) < int(generated_number):
                print("Too small!")
                continue
            elif int(guess_n) == int(generated_number):
                print("Just right!")
            exit()
        except ValueError:
            continue


main()
