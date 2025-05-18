import re


def main():
    i = input("")
    case_id(i)


def case_id(c_str):
    kebab_case = r"^[a-z]+(-[a-z]+)*$"
    match_k_c = re.search(kebab_case, c_str)

    snake_case = r"^[a-z]+(_[a-z]+)*$"
    match_s_c = re.match(snake_case, c_str)

    camel_case = r"^[a-z]+([A-Z][a-z]+)*$"
    match_c_c = re.match(camel_case, c_str)

    if match_c_c:
        print('camel')
        return 'camel'
    elif match_s_c:
        print('snake')
        return 'snake'
    elif match_k_c:
        print('kebab')
        return 'kebab'
    else:
        print("none")
        return 'none'

main()
