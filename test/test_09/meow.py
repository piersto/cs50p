def meow(n: int) -> str:
    """Meow n times

    :param n: Number of times to meow
    :type n: int
    :raise TypeError: If n is not an int
    :return String of n meows, one per line
    :rtype str
    """
    return "meow\n" * n

number: int = int(input("Number: "))
meows :str = meow(number)

print(meows, end="")