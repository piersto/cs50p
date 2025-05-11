import sys
import csv
from tabulate import tabulate


def main():
    price_list = []
    try:
        if len(sys.argv) < 2:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")
        elif not (sys.argv[1]).endswith(".csv"):
            sys.exit("Not a CSV file")
        else:
            with open(sys.argv[1]) as file:
                reader = csv.reader(file)
                for pizza, small, large in reader:
                    price_list.append({"pizza": pizza, "small": small, "large": large})
        print(tabulate(price_list, headers="firstrow", tablefmt="grid"))

    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == '__main__':
    main()
