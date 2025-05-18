import re


def main():
    code = input("IP address: ")

    pattern = r"(\d{1,3})/(\d{1,3})/(\d{1,3})/(\d{1,3})"

    match = re.match(pattern, code)
    first_group = match.group(1)
    second_group = match.group(2)
    third_group = match.group(3)
    fourth_group = match.group(4)
    print(first_group)

    if not match:
        print(f"False")
    elif int(first_group) > 255 or int(first_group) < 0:
        print(f"False")
    elif int(second_group) > 255 or int(first_group) < 0:
        print(f"False")
    elif int(third_group) > 255 or int(first_group) < 0:
        print(f"False")
    elif int(fourth_group) > 255 or int(first_group) < 0:
        print(f"False")
    else:
        print("True")

main()
