students = []

with open("C:\PROJECTS\PYTHON\CX50P\students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)


def get_name(student):
    return student["name"]


def get_house(student):
    return student['house']


for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")

for student in sorted(students, key=get_house, reverse=True):
    print(f"{student['name']} is in {student['house']}")
