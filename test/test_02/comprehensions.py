def main():
    words = ["get", "words", "Address", "txt", "address", "world"]
    lowercase_words = [word.lower() for word in words if len(word) > 4]
    counts = {word: lowercase_words.count(word) for word in lowercase_words}

    print(lowercase_words)
    print(counts)


if __name__ == '__main__':
    main()
