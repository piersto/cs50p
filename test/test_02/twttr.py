s = input("Input: ")

t = list(s)

for j in t:
    if j == "i" \
            or j == "I" \
            or j == "A" \
            or j == "a" \
            or j == "O" \
            or j == "o" \
            or j == "E" \
            or j == "e"\
            or j == "U" \
            or j == "u":
        pass
    else:
        print(j, end="")
