import re

class Student:
    def __init__(self, student_id, name, dob):
        self.__id = student_id
        self.__name = name
        self.__dob = dob

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_dob(self):
        return self.__dob

    def describe(self):
        print(f"Student ID: {self.__id} | Name: {self.__name} | DoB: {self.__dob}")


class Course:
    def __init__(self, course_id, name):
        self.__id = course_id
        self.__name = name

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def describe(self):
        print(f"Course ID: {self.__id} | Course Name: {self.__name}")


class StudentMarkManagement:
    def __init__(self):
        self.__students = []
        self.__courses = []
        self.__marks = {}  # Format: {course_id: {student_id: mark}}

    # Helper method to validate DD/MM/YYYY date format
    def __validate_date(self, date_str):
        pattern = r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$"
        return bool(re.match(pattern, date_str))

    # Helper method to validate student ID (exactly 6 digits)
    def __validate_student_id(self, id_str):
        pattern = r"^\d{6}$"
        return bool(re.match(pattern, id_str))

    # Input functions
    def input_students(self):
        num = int(input("Enter the number of students in the class: "))
        for i in range(num):
            print(f"\n--- Enter details for student {i+1} ---")
            
            # Loop until a valid 6-digit Student ID is entered
            while True:
                sid = input("Enter student ID (exactly 6 digits): ")
                if self.__validate_student_id(sid):
                    break
                print("❌ Invalid ID! Student ID must consist of exactly 6 digits (e.g., 123456).")

            name = input("Enter student name: ")
            
            # Loop until a valid DoB format (DD/MM/YYYY) is entered
            while True:
                dob = input("Enter date of birth (DD/MM/YYYY): ")
                if self.__validate_date(dob):
                    break
                print("❌ Invalid format! Please enter DoB strictly in DD/MM/YYYY format (e.g., 05/12/2006).")

            self.__students.append(Student(sid, name, dob))
        print("\n Student list successfully recorded!")

    def input_courses(self):
        num = int(input("Enter the number of courses: "))
        for i in range(num):
            print(f"\n--- Enter details for course {i+1} ---")
            cid = input("Enter course ID: ")
            name = input("Enter course name: ")
            self.__courses.append(Course(cid, name))
        print("\n Course list successfully recorded!")

    def input_marks(self):
        if not self.__courses:
            print("\n The course list is empty! Please add courses first (Option 2).")
            return
        if not self.__students:
            print("\n The student list is empty! Please add students first (Option 1).")
            return

        print("\nAvailable courses:")
        for course in self.__courses:
            course.describe()
        
        selected_course_id = input("\nEnter the course ID to input marks for: ")
        
        # Verify if course exists
        course_exists = any(c.get_id() == selected_course_id for c in self.__courses)
        if not course_exists:
            print("\n Course ID does not exist!")
            return

        if selected_course_id not in self.__marks:
            self.__marks[selected_course_id] = {}

        print(f"\n--- Entering marks for course: {selected_course_id} ---")
        for student in self.__students:
            mark = float(input(f"Enter mark for student {student.get_name()} (ID: {student.get_id()}): "))
            self.__marks[selected_course_id][student.get_id()] = mark
        print("\n Marks successfully recorded!")

    # Listing functions
    def list_courses(self):
        if not self.__courses:
            print("\n No courses available.")
            return
        print("\n=== COURSE LIST ===")
        for course in self.__courses:
            course.describe()

    def list_students(self):
        if not self.__students:
            print("\n No students available.")
            return
        print("\n=== STUDENT LIST ===")
        for student in self.__students:
            student.describe()

    def show_student_marks(self):
        if not self.__marks:
            print("\n No marks data available.")
            return
        
        print("\nCourses with recorded marks:")
        for cid in self.__marks.keys():
            print(f"- Course ID: {cid}")

        selected_course_id = input("\nEnter the course ID to view marks: ")
        if selected_course_id not in self.__marks:
            print("\n Marks data not found for this course.")
            return

        print(f"\n=== MARKS SHEET FOR COURSE: {selected_course_id} ===")
        print(f"{'Student ID':<12} | {'Name':<20} | {'DoB':<12} | {'Mark':<5}")
        print("-" * 57)
        for student in self.__students:
            sid = student.get_id()
            name = student.get_name()
            dob = student.get_dob()
            score = self.__marks[selected_course_id].get(sid, "N/A")
            print(f"{sid:<12} | {name:<20} | {dob:<12} | {str(score):<5}")

    # Main menu controller
    def run(self):
        while True:
            print("\n================ STUDENT MARK MANAGEMENT ================")
            print("1. Input student information")
            print("2. Input course information")
            print("3. Input marks for students in a course")
            print("4. List courses")
            print("5. List students")
            print("6. Show student marks for a given course")
            print("0. Exit program")
            print("=========================================================")
            
            choice = input("Enter your choice (0-6): ")
            
            if choice == '1':
                self.input_students()
            elif choice == '2':
                self.input_courses()
            elif choice == '3':
                self.input_marks()
            elif choice == '4':
                self.list_courses()
            elif choice == '5':
                self.list_students()
            elif choice == '6':
                self.show_student_marks()
            elif choice == '0':
                print("\n Thank you for using the program. Goodbye!")
                break
            else:
                print("\n Invalid choice. Please enter a number between 0 and 6!")

if __name__ == "__main__":
    app = StudentMarkManagement()
    app.run()