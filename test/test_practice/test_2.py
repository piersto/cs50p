n = input("What's the number ")

while True:
    try:
        n = int(n)
        if not int(n) >= 1:
            n = input("What's the number ")
            print(str(n))
        else:
            break
    except ValueError:
        n = input("What's the number ")

    guesse_n = input("Guess the  the number? ")
    while True:
        try:
            guesse_n = int(n)
        except ValueError:
            guesse_n = input("What's the number? ")
        else:
            if guesse_n > 0:
                pass

























