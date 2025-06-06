import csv
from tabulate import tabulate

students = []

with open("/hlam/before.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        students.append({"name": row[0], "home": row[1]})

print(tabulate(students, headers="firstrow", tablefmt="grid"))
