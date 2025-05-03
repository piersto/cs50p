import random

cards = ["queen", "king", "as"]


def main():
    # setting seed will cancel randomness 
    random.seed(0)
    print(random.choice(cards))
    # can make the same choice as chosen one is back to the list
    # print(random.choices(cards, k=2))
    # print(random.sample(cards, k=2))
    print((random.choices(cards, weights=[66, 22, 33], k=2)))












main()