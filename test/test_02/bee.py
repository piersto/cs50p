# https://www.youtube.com/watch?v=3zJoCpvKhx4&ab_channel=CS50

WORDS = {"PAIR": 4, "HAIR": 4, "CHAIR": 5, "GRAPHIC": 7}


def main():
    print("Welcom to spelling bee")
    print("Your letters are: A I P C R H G")

    # while len(WORDS) > 0:
    #     print(f"{len(WORDS)} words lelf!")
    #     guess = input("Guess word: ")
    #
    #     if guess.strip().upper() == "GRAPHIC":
    #         WORDS.clear()
    #         print("You have won!")
    #     if guess.strip().upper() in WORDS:
    #         points = WORDS.pop(guess)
    #
    #         print(f"Good job! You scored{points} points")
    # print("That's the game")

    for i in WORDS:
        print(f"{WORDS(i)} {WORDS[i]}")


if __name__ == '__main__':
    main()
