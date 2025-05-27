def count_developers(lst):
    counter = 0
    for row in lst:
        if row["continent"] == "Europe" and row["language"] == "JavaScript":
            counter += 1
        else:
            continue
    print(str(counter))
    return counter


def main():
    lst = [
        {'firstName': 'Noah', 'lastName': 'M.', 'country': 'Switzerland', 'continent': 'Europe', 'age': 19,
         'language': 'JavaScript'},
        {'firstName': 'Maia', 'lastName': 'S.', 'country': 'Tahiti', 'continent': 'Oceania', 'age': 28,
         'language': 'JavaScript'},
        {'firstName': 'Shufen', 'lastName': 'L.', 'country': 'Taiwan', 'continent': 'Asia', 'age': 35,
         'language': 'HTML'},
        {'firstName': 'Sumayah', 'lastName': 'M.', 'country': 'Tajikistan', 'continent': 'Asia', 'age': 30,
         'language': 'CSS'},
        {'firstName': 'Maia', 'lastName': 'S.', 'country': 'Tahiti', 'continent': 'Oceania', 'age': 28,
         'language': 'JavaScript'},
    ]
    count_developers(lst)


main()

