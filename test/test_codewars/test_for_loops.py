students = ["Harry Potter", "Hermione Granger", "Ron Weasley", "Draco Malfoy", "Luna Lovegood"]

# Using range(len()) to access index positions
for i in range(len(students)):
    print(f"Student {i + 1}: {students[i]}")

print(
"++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
)

students = ["Harry Potter", "Hermione Granger", "Ron Weasley", "Draco Malfoy", "Luna Lovegood"]

# Printing each student’s name directly
for student in students:
    print(f"Hogwarts Student: {student}")

print(
"========================================================================================================="
)

wizarding_skills = {"Potion-making", "Spell-casting", "Flying"}

for skill in wizarding_skills:
    print(f"Skill: {skill}")


print(
'----------------------------------------------------------------------------------------------------------'
)


students = ["Harry Potter", "Hermione Granger", "Ron Weasley", "Draco Malfoy", "Luna Lovegood"]

# Using range(len()) to access index positions
for i in range(len(students)):
    print(f"Student {i + 1}: {students[i]}")


print(
"************************************************************************************************************"
)

students = {"Harry": "Gryffindor", "Draco": "Slytherin", "Luna": "Ravenclaw"}

# Iterating over keys (student names)
for student in students:
    print(f"Student Name: {student}")

# Iterating over values (house names)
for house in students.values():
    print(f"Hogwarts House: {house}")

# Iterating over key-value pairs
for student, house in students.items():
    print(f"{student} belongs to {house}")


