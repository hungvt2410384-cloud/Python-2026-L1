from domains.student import Student
from domains.course import Course

def input_students():
    num_students = int(input("Enter number of students: "))
    students = []
    for i in range(num_students):
        print(f"\nEnter info for student {i+1}:")
        s_id = input("Student ID: ")
        name = input("Student Name: ")
        dob = input("Date of Birth: ")
        students.append(Student(s_id, name, dob))
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
    return courses

def input_marks(students, courses):
    print("\n--- Select a course to input marks ---")
    for idx, course in enumerate(courses):
        print(f"{idx}. {course.get_name()} (ID: {course.get_id()})")
    
    c_index = int(input("Enter course number: "))
    selected_course = courses[c_index]
    c_id = selected_course.get_id()

    course_marks = {}
    print(f"Inputting marks for: {selected_course.get_name()} (math.floor applied)")
    for student in students:
        raw_mark = float(input(f"Enter mark for {student.get_name()}: "))
        student.add_mark(c_id, raw_mark)
        course_marks[student.get_id()] = student.get_marks()[c_id]

    return c_id, course_marks