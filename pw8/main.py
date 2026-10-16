import sys
from output import load_data, save_data_async


class SchoolManagement:
    def __init__(self, filename="students.pkl.gz"):
        self.filename = filename
        self.last_save_thread = None

        loaded_data = load_data(self.filename)
        if loaded_data:
            self.students = loaded_data.get("students", [])
            self.courses = loaded_data.get("courses", [])
            self.marks = loaded_data.get("marks", {})
        else:
            self.students = []
            self.courses = []
            self.marks = {}

    def input_student(self):
        sid = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        dob = input("Enter Student DoB: ")
        self.students.append({"id": sid, "name": name, "dob": dob})
        print("Student added successfully.")

    def list_students(self):
        if not self.students:
            print("No students found.")
            return
        print("\n--- STUDENT LIST ---")
        for st in self.students:
            print(f"ID: {st['id']} | Name: {st['name']} | DoB: {st['dob']}")

    def save_data(self):
        data = {
            "students": self.students,
            "courses": self.courses,
            "marks": self.marks,
        }
        self.last_save_thread = save_data_async(data, self.filename)

    def run(self):
        while True:
            print("\n......................")
            print(" STUDENT MANAGEMENT SYSTEM ")
            print("......................")
            print("1. Add Student")
            print("2. List Students")
            print("3. Save Data (Background Thread)")
            print("4. Save & Exit")
            choice = input("Select an option (1-4): ")

            if choice == "1":
                self.input_student()
            elif choice == "2":
                self.list_students()
            elif choice == "3":
                self.save_data()
            elif choice == "4":
                print("Saving data before exiting...")
                self.save_data()
                if self.last_save_thread:
                    self.last_save_thread.join()
                print("Exiting application. Goodbye!")
                break
            else:
                print("Invalid choice, please try again.")


if __name__ == "__main__":
    app = SchoolManagement()
    app.run()