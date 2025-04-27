"""""
input item
verify if in dic
if yes display total >> in
if no input item
"""


def main():
    d = {
        "baja taco": 4.25,
        "burrito": 7.50,
        "bowl": 8.50,
        "nachos": 11.00,
        "quesadilla": 8.50,
        "super burrito": 8.50,
        "super quesadilla": 9.50,
        "taco": 3.00,
        "tortilla salad": 8.00
    }
    total = float(0.00,)
    while True:
        try:
            item = (input("Item: "))
            item = item.strip().lower()
            if item in d:
                item_price = d[item]
                total = total + item_price
                print("$" + f"{total:.2f}")
        except KeyError:
            pass
        except EOFError:
            break


if __name__ == '__main__':
    main()
