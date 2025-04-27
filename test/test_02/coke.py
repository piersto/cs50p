amount_due = 50

while amount_due > 0:
    print("Amount due: " + str(amount_due))
    inserted_coin = input("Insert coin: ")
    if inserted_coin == "5" or inserted_coin == "10" or inserted_coin == "25":
        amount_due = amount_due - int(inserted_coin)
    else:
        continue
print("Change Owed: " + str((amount_due*-1)))


# AI code:
def main():
    amount_due = 50  # Initial cost of a Coke
    accepted_coins = {25, 10, 5}  # Set of valid coin denominations

    while amount_due > 0:
        print(f"Amount due: {amount_due}")
        coin = int(input("Insert coin: "))

        if coin in accepted_coins:
            amount_due -= coin

    change_owed = abs(amount_due)  # If the user overpays, calculate change
    print(f"Change Owed: {change_owed}")

if __name__ == "__main__":
    main()
