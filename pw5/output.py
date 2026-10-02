import curses

def list_courses(courses):
    print("\n--- List of Courses ---")
    if not courses:
        print("No courses available.")
    for c in courses:
        print(f"ID: {c.get_id()} | Name: {c.get_name()} | Credits: {c.get_credits()}")

def list_students(students):
    print("\n--- List of Students ---")
    if not students:
        print("No students available.")
    for s in students:
        print(f"ID: {s.get_id()} | Name: {s.get_name()} | DoB: {s.get_dob()}")

def show_sorted_students(students):
    print("\n--- Sorted Students by GPA ---")
    for s in students:
        print(f"ID: {s.get_id()} | Name: {s.get_name()} | GPA: {s.get_gpa()}")

def curses_ui_display(stdscr, students):
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