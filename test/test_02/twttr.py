# def main():
#
#     word = input("Input: ")
#     print(shorten(word))


# def shorten():
word = "ahotenusis"
t = list(word)
shorten_word = ""

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
        shorten_word.join(j)
        print(shorten_word)
print (shorten_word)
#
#
# if __name__ == '__main__':
#     main()
