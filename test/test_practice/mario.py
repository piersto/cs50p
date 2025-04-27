def main():
    print_square(3)


def print_square(size):
    # for each brick in row
    for i in range(size):
        # print brick
        for j in range(size):
            print("#", end="")
        print()


# def main():
#     print_column(3)
#     print_row(4)
#
#
# def print_column(height):
#     for _ in range(height):
#         print("#")
#
#
# def print_row(width):
#     print("?" * width)
#
#
main()
