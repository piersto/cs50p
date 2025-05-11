import csv
import sys


def main():
    try:
        if len(sys.argv) < 3:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 3:
            sys.exit("Too many command-line arguments")
        elif not sys.argv[1].endswith(".csv"):
            sys.exit("Not a .csv file")

        students = []
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append({"name": row["name"], "house": row["house"]})
    except FileNotFoundError:
        sys.exit("Could not read invalid_file.csv")
    except ValueError:
        sys.exit("Could not read invalid_file.csv")

    write_file = sys.argv[2]
    with open(write_file,  'w', newline='') as file:
        fieldnames = ['first', 'last', 'house']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for row in students:
            last, first = row["name"].split(",")
            last = last.strip()
            first = first.strip()
            house = row["house"]
            writer.writerow({"first": first, "last": last, "house": house})


if __name__ == '__main__':
    main()
