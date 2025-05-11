import csv

name = input("What's your name? ")
home = input("What's your home? ")

with open("C:\PROJECTS\PYTHON\CX50P\students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})






#
# import csv
#
# name = input("What's your name? ")
# home = input("Where's your home? ")
#
# with open("C:\PROJECTS\PYTHON\CX50P\students.csv", "a") as file:
#     writer = csv.writer(file)
#     writer.writerow([name, home])
#
