import re
import sys


def main():
    print(parse(input("HTML: ")))
    # print(parse('<iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>'))


def parse(s):
    pattern = r'^<iframe .*(src="http)(s)?(://)(www\.)?(youtube\.com/embed/)([a-zA-Z0-9]+).*></iframe>$'
    match = re.match(pattern, s)
    if not match:
        return None

    return f"https://youtu.be/{match.group(6)}"


if __name__ == "__main__":
    main()
