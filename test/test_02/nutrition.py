x = input("Item: ")
x = x.strip().lower()

fruits_dic = {
    "apple": "130",
    "avocado": "50",
    "sweet cherries": "100",
    "kiwifruit": "90",
    "pear": "100"
}

if x in fruits_dic:
    print(fruits_dic[x])
else:
    pass
