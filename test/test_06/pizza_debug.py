import csv

price_list = []

with open("C:\PROJECTS\PYTHON\CX50P\/regular.csv") as file:
    reader = csv.reader(file)
    for pizza, small, large in reader:
        price_list.append({"pizza": pizza, "small": small, "large": large})


for pizza in price_list:
    print(f"{pizza['pizza']} ")
