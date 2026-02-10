from student import Student
from storage import Storage


class StudentManagementSystem:
    def __init__(self):
        self.storage = Storage()
        self.students = self.storage.load()

    def add_student(self):
        try:
            roll = input("Enter roll number: ").strip()
            if any(s["roll"] == roll for s in self.students):
                print("❌ Roll number already exists.")
                return

            name = input("Enter name: ").strip()
            marks = int(input("Enter marks (0-100): "))

            if marks < 0 or marks > 100:
                raise ValueError

            student = Student(roll, name, marks)
            self.students.append(student.to_dict())
            self.storage.save(self.students)
            print("✅ Student added successfully.")

        except ValueError:
            print("❌ Invalid marks input.")

    def view_students(self):
        if not self.students:
            print("❌ No records found.")
            return

        print("\n--- Student Records ---")
        for s in self.students:
            print(
                f"Roll: {s['roll']} | Name: {s['name']} | Marks: {s['marks']} | Grade: {s['grade']}"
            )

    def search_student(self):
        roll = input("Enter roll number to search: ").strip()
        for s in self.students:
            if s["roll"] == roll:
                print("✅ Student Found:", s)
                return
        print("❌ Student not found.")

    def update_student(self):
        roll = input("Enter roll number to update: ").strip()
        for s in self.students:
            if s["roll"] == roll:
                try:
                    s["name"] = input("Enter new name: ").strip()
                    marks = int(input("Enter new marks: "))
                    if marks < 0 or marks > 100:
                        raise ValueError
                    s["marks"] = marks
                    s["grade"] = Student(roll, s["name"], marks).grade
                    self.storage.save(self.students)
                    print("✅ Student updated.")
                    return
                except ValueError:
                    print("❌ Invalid marks.")
                    return
        print("❌ Student not found.")

    def delete_student(self):
        roll = input("Enter roll number to delete: ").strip()
        for s in self.students:
            if s["roll"] == roll:
                self.students.remove(s)
                self.storage.save(self.students)
                print("✅ Student deleted.")
                return
        print("❌ Student not found.")

    def sort_students(self):
        self.students.sort(key=lambda x: x["marks"], reverse=True)
        print("✅ Students sorted by marks (high → low).")

    def export_to_csv(self):
        self.storage.export_csv(self.students)
        print("✅ Data exported to students.csv")

    def menu(self):
        while True:
            print("\n====== Student Management System ======")
            print("1. Add Student")
            print("2. View Students")
            print("3. Search Student")
            print("4. Update Student")
            print("5. Delete Student")
            print("6. Sort by Marks")
            print("7. Export to CSV")
            print("8. Exit")

            choice = input("Enter choice: ")

            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.view_students()
            elif choice == "3":
                self.search_student()
            elif choice == "4":
                self.update_student()
            elif choice == "5":
                self.delete_student()
            elif choice == "6":
                self.sort_students()
            elif choice == "7":
                self.export_to_csv()
            elif choice == "8":
                print("👋 Goodbye!")
                break
            else:
                print("❌ Invalid choice.")


if __name__ == "__main__":
    StudentManagementSystem().menu()
