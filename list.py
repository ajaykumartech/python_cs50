# students.py
students = [
    {"name": "Alice", "grade": "A"},
    {"name": "Bob", "grade": "B"},
    {"name": "Charlie", "grade": "C"}
]

for student in students:
    print(f"{student['name']} got grade {student['grade']}")