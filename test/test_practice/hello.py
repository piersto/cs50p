# name = input("What's your name? ").capitalize().title()
#
# first, second = name.split(" ")
# print("Hello,", first)
#
# print("Mr.", second, "you are awesome!!!")


def hello(to="world"):
    print("Hello, " + to)

name = input("What's your name? ")
hello()
hello(name)
# print(name)


def main():
    print("Hello, world!")
    print("This is CS50P")

main()