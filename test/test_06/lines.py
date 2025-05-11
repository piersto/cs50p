import sys
counter = 0
# Open file
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")
else:
    try:
        with open(sys.argv[1]) as file:
            for line in file:
                if line.strip().startswith("#"):
                    pass
                elif line.isspace():
                    pass
                elif line.strip() and not line.find(".", 0, 1):
                    pass
                else:
                    counter += 1
                    print(line)
    except FileNotFoundError:
        sys.exit("File does not exist")
print(str(counter))
