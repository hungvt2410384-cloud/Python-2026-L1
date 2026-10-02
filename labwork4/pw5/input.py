import os
from domains.student import Student
from domains.course import Course

def save_students(students):
    with open("students.txt", "w") as f:
        for s in students:
            f.write(f"{s.get_id()},{s.get_name()},{s.get_dob()}\n")

def save_courses(courses):
    with open("courses.txt", "w") as f:
        for c in courses:
            f.write(f"{c.get_id()},{c.get_name()},{c.get_credits()}\n")

def save_marks(marks_storage):
    with open("marks.txt", "w") as f:
        for c_id, marks in marks_storage.items():
            for s_id, mark in marks.items():
                f.write(f"{c_id},{s_id},{mark}\n")

def input_students():
    num_students = int(input("Enter number of students: "))
    students = []
    for i in range(num_students):
        print(f"\nEnter info for student {i+1}:")
        s_id = input("Student ID: ")
        name = input("Student Name: ")
        dob = input("Date of Birth: ")
        students.append(Student(s_id, name, dob))
    save_students(students)
    return students

def input_courses():
    num_courses = int(input("\nEnter number of courses: "))
    courses = []
    for i in range(num_courses):
        print(f"\nEnter info for course {i+1}:")
        c_id = input("Course ID: ")
        name = input("Course Name: ")
        credits = int(input("Course Credits (Weight): "))
        courses.append(Course(c_id, name, credits))
    save_courses(courses)
    return courses

def input_marks(students, courses, marks_storage):
    print("\n--- Select a course to input marks ---")
    for idx, course in enumerate(courses):
        print(f"{idx}. {course.get_name()} (ID: {course.get_id()})")
    
    c_index = int(input("Enter course number: "))
    selected_course = courses[c_index]
    c_id = selected_course.get_id()

    if c_id not in marks_storage:
        marks_storage[c_id] = {}

    print(f"Inputting marks for: {selected_course.get_name()} (math.floor applied)")
    for student in students:
        raw_mark = float(input(f"Enter mark for {student.get_name()}: "))
        student.add_mark(c_id, raw_mark)
        marks_storage[c_id][student.get_id()] = student.get_marks()[c_id]

    save_marks(marks_storage)
    return c_id, marks_storage

def load_data():
    students = []
    courses = []
    marks_storage = {}

    if os.path.exists("students.txt"):
        with open("students.txt", "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    students.append(Student(parts[0], parts[1], parts[2]))

    if os.path.exists("courses.txt"):
        with open("courses.txt", "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    courses.append(Course(parts[0], parts[1], int(parts[2])))

    if os.path.exists("marks.txt"):
        with open("marks.txt", "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    c_id, s_id, mark = parts[0], parts[1], float(parts[2])
                    if c_id not in marks_storage:
                        marks_storage[c_id] = {}
                    marks_storage[c_id][s_id] = mark
                    for s in students:
                        if s.get_id() == s_id:
                            s.add_mark(c_id, mark)

    return students, courses, marks_storage