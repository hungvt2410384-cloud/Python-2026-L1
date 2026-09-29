import math
import numpy as np
import curses

class Student:
    def __init__(self, student_id, name, dob):
        self.__id = student_id
        self.__name = name
        self.__dob = dob
        self.__marks = {}  # {course_id: mark}
        self.__gpa = 0.0

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_dob(self):
        return self.__dob

    def add_mark(self, course_id, mark):
        # Use math.floor to round down student marks to 1-digit decimal
        rounded_mark = math.floor(mark * 10) / 10.0
        self.__marks[course_id] = rounded_mark

    def calculate_gpa(self, courses):
        """
        Calculate average GPA for a given student using numpy array.
        Weighted sum of credits and marks.
        """
        if not self.__marks:
            self.__gpa = 0.0
            return self.__gpa

        marks_list = []
        credits_list = []

        for course in courses:
            c_id = course.get_id()
            if c_id in self.__marks:
                marks_list.append(self.__marks[c_id])
                credits_list.append(course.get_credits())

        if not marks_list:
            self.__gpa = 0.0
            return self.__gpa

        # Convert to numpy arrays for calculation
        marks_arr = np.array(marks_list)
        credits_arr = np.array(credits_list)

        # Weighted sum of credits and marks
        weighted_sum = np.sum(marks_arr * credits_arr)
        total_credits = np.sum(credits_arr)

        if total_credits == 0:
            self.__gpa = 0.0
        else:
            self.__gpa = round(weighted_sum / total_credits, 2)

        return self.__gpa

    def get_gpa(self):
        return self.__gpa


class Course:
    def __init__(self, course_id, name, credits):
        self.__id = course_id
        self.__name = name
        self.__credits = credits  # Credit weight for GPA calculation

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_credits(self):
        return self.__credits


def curses_ui_display(stdscr, students):
    """Decorate UI with curses module showing students and their GPAs"""
    stdscr.clear()
    stdscr.addstr(0, 0, "=== STUDENT MARK MANAGEMENT - CURSES UI ===", curses.A_BOLD)
    stdscr.addstr(2, 0, "ID          Name                GPA")
    stdscr.addstr(3, 0, "-" * 40)

    row = 4
    for student in students:
        info = f"{student.get_id():<11} {student.get_name():<19} {student.get_gpa():<5}"
        stdscr.addstr(row, 0, info)
        row += 1

    stdscr.addstr(row + 2, 0, "Press any key to return to main menu...")
    stdscr.refresh()
    stdscr.getch()


def main():
    students = []
    courses = []
    marks_storage = {}  # {course_id: {student_id: mark}}

    # 1. Input number and info of students
    num_students = int(input("Enter number of students: "))
    for i in range(num_students):
        print(f"\nEnter info for student {i+1}:")
        s_id = input("Student ID: ")
        name = input("Student Name: ")
        dob = input("Date of Birth: ")
        students.append(Student(s_id, name, dob))

    # 2. Input number and info of courses (including credits)
    num_courses = int(input("\nEnter number of courses: "))
    for i in range(num_courses):
        print(f"\nEnter info for course {i+1}:")
        c_id = input("Course ID: ")
        name = input("Course Name: ")
        credits = int(input("Course Credits (Weight): "))
        courses.append(Course(c_id, name, credits))

    while True:
        print("\n--- MENU ---")
        print("1. List courses")
        print("2. List students")
        print("3. Input marks for a course (math.floor applied)")
        print("4. Calculate GPAs and sort students descending")
        print("5. Show UI with Curses module")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            print("\n--- List of Courses ---")
            for c in courses:
                print(f"ID: {c.get_id()} | Name: {c.get_name()} | Credits: {c.get_credits()}")

        elif choice == "2":
            print("\n--- List of Students ---")
            for s in students:
                print(f"ID: {s.get_id()} | Name: {s.get_name()} | DoB: {s.get_dob()}")

        elif choice == "3":
            print("\n--- Select a course to input marks ---")
            for idx, c in enumerate(courses):
                print(f"{idx}. {c.get_name()} (ID: {c.get_id()})")
            c_index = int(input("Enter course number: "))
            selected_course = courses[c_index]
            c_id = selected_course.get_id()

            course_marks = {}
            print(f"Inputting marks for: {selected_course.get_name()} (math.floor will be used)")
            for s in students:
                raw_mark = float(input(f"Enter mark for {s.get_name()}: "))
                s.add_mark(c_id, raw_mark)
                course_marks[s.get_id()] = s._Student__marks[c_id]

            marks_storage[c_id] = course_marks
            print("Marks saved successfully!")

        elif choice == "4":
            # Calculate GPA for each student and sort descending
            for s in students:
                s.calculate_gpa(courses)
            
            # Sort student list by GPA descending
            students.sort(key=lambda x: x.get_gpa(), reverse=True)
            print("\nGPAs calculated and students sorted by GPA descending successfully!")
            
            print("\n--- Sorted Students by GPA ---")
            for s in students:
                print(f"ID: {s.get_id()} | Name: {s.get_name()} | GPA: {s.get_gpa()}")

        elif choice == "5":
            for s in students:
                s.calculate_gpa(courses)
            curses.wrapper(curses_ui_display, students)

        elif choice == "6":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()