from .models import Student

def print_report(students: list[Student]):
    for student in students:
        print(f"{student.name}: {student.average:.2f}")