from gradebook import Student, generate_report

students = [
    Student("Priya"),
    Student("Amrutha"),
    Student("Rahul")
]

print("Students:")
print(generate_report(students))


# Predict output question
s = Student("Priya")

print(s.name)
print(type(s).__name__)
print(isinstance(s, Student))