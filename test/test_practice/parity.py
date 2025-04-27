def main():
    x = int(input("What is x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")


def is_even(x):
    return x % 2 == 0


main()

# x = int(input("What is x? "))
# if x % 2 == 0:
#     print("Even")
# else:
#     print("Odd")