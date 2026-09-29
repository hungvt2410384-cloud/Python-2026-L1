from input import input_students, input_courses, input_marks
from output import list_courses, list_students, show_sorted_students, curses_ui_display
import curses

def main():
    students = []
    courses = []
    marks_storage = {}

    students = input_students()
    courses = input_courses()

    while True:
        print("\n--- MENU ---")
        print("1. List courses")
        print("2. List students")
        print("3. Input marks for a course")
        print("4. Calculate GPAs and sort students descending")
        print("5. Show UI with Curses module")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            list_courses(courses)
        elif choice == "2":
            list_students(students)
        elif choice == "3":
            if not courses or not students:
                print("Please ensure students and courses are added first!")
            else:
                c_id, course_marks = input_marks(students, courses)
                marks_storage[c_id] = course_marks
                print("Marks saved successfully!")
        elif choice == "4":
            for s in students:
                s.calculate_gpa(courses)
            students.sort(key=lambda x: x.get_gpa(), reverse=True)
            print("\nGPAs calculated and students sorted by GPA descending successfully!")
            show_sorted_students(students)
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