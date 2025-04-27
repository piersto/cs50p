s = input("What's the name? ")
l = list(s)
for i in l:
    if i.islower():
        print(i, end="")
    else:
        print("_" + i.lower(), end="")
