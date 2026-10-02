import os
import zipfile
import curses
from input import input_students, input_courses, input_marks, load_data, save_students, save_courses, save_marks
from output import list_courses, list_students, show_sorted_students, curses_ui_display

DAT_FILE = "students.dat"

def compress_data():
    with zipfile.ZipFile(DAT_FILE, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file in ["students.txt", "courses.txt", "marks.txt"]:
            if os.path.exists(file):
                zipf.write(file)
    print("Data compressed successfully into", DAT_FILE)

def decompress_data():
    if os.path.exists(DAT_FILE):
        with zipfile.ZipFile(DAT_FILE, 'r') as zipf:
            zipf.extractall(".")
        print("Data decompressed successfully from", DAT_FILE)

def main():
    if os.path.exists(DAT_FILE):
        decompress_data()
        students, courses, marks_storage = load_data()
        print("Loaded existing data from file successfully!")
    else:
        print("No existing data found. Please input new data.")
        students = input_students()
        courses = input_courses()
        marks_storage = {}

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
                c_id, marks_storage = input_marks(students, courses, marks_storage)
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
            save_students(students)
            save_courses(courses)
            save_marks(marks_storage)
            compress_data()
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()