import json
from .database import load_students

def main():
    try:
        students = load_students("student_tracker/students.json")

        for student in students:
            print(f"{student.name}: {student.average:.2f}")

    except FileNotFoundError:
        print("Error: Student file not found.")

    except (json.JSONDecodeError, KeyError, TypeError) as e:
        print(f"Error reading student data: {e}")

if __name__ == "__main__":
    main()