students = ["Harry", "Hermione", "Ron"]
# Reverse the list using slicing
reversed_students = students[::-1]
print(reversed_students)
""""
If you want to return
return students[::-1]  # ✅ Returns a reversed copy
"""


students = ["Harry", "Hermione", "Ron"]
# Reverse using reversed()
# Python’s built-in reversed() function returns an iterator, which can be converted into a list.
reversed_students = list(reversed(students))
print(reversed_students)
""""
If you want to return
return list(reversed(students))  # ✅ Returns a new reversed list
"""


students = ["Harry", "Hermione", "Ron"]
# Reverse in place
# Unlike slicing and reversed(), .reverse() modifies the original list.
students.reverse()
print(students)
"""
If you want to return: 
students.reverse()
return students  # ✅ Works because you've already modified it
"""


