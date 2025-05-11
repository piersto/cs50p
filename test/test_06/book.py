def main():
    with open("alice.txt", encoding='utf-8') as f:
        content = f.readlines()
        print(content[0])

    chapter_I = content[52:262]
    print(chapter_I[0])

    with open("chapter_I.txt", "w") as f:
        f.writelines(chapter_I)



if __name__ == '__main__':
    main()