# https://cs50.harvard.edu/python/2022/psets/4/figlet/


import sys
from pyfiglet import Figlet
import random


def main():
    figlet = Figlet()
    list_of_fonts = figlet.getFonts()

    if len(sys.argv) == 1:
        s = input_text()
        font = random.choice(list_of_fonts)
        figlet.setFont(font=font)
        print(f"Output: {figlet.renderText(s)}")

    elif len(sys.argv) == 3 \
            and sys.argv[1] == "-f" or sys.argv[1] == "--font" \
            and sys.argv[2] in list_of_fonts:
        s = input_text()
        font = sys.argv[2]
        figlet.setFont(font=font)
        print(f"Output: {figlet.renderText(s)}")
    else:
        sys.exit("Invalid usage")


def input_text():
    s = input("Input: ")
    return s


main()
