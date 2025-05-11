import csv
import sys
from tabulate import tabulate

students = []

with open("C:\PROJECTS\PYTHON\CX50P\/before.csv") as file:
    student = csv.DictReader(file)
    students.append(student)

print(tabulate(students))
