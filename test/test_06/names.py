name = input("What's your name? ")

with open("names.txt", "a") as file:
    file.write(f"{name}\n")




# file = open("names.txt", "a")
# file.write(f"{name}\n")
# file.close()


# for _ in range(3):
#     names.append(input(f"What's your name? "))
#
# for name in sorted(names):
#     print(f"hello, {name}")
