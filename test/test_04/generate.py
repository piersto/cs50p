import random
for i in range(1):

    coin = random.choices(["heads", "tails"])
    integer = random.randint(1, 100)
    coint_as_str = str(coin)
    cards = ["king", "queen", "as", "valet"]
    random.shuffle(cards)
    for card in cards:
        print(f"{card} ",  sep=" | ")
