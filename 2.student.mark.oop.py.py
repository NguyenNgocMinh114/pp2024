class Student:
    def __init__(self, student_id, name, marks=None):
        """Initialize the student object with ID, name, and marks."""
        self.student_id = student_id
        self.name = name
        self.marks = marks if marks else []

    def assign_marks(self, marks):
        """Assign marks to the student."""
        self.marks = marks
        print(f"Marks updated for student {self.name} (ID: {self.student_id}).")

    def update_marks(self, subject_index, new_mark):
        """Update the marks for a specific subject."""
        if 0 <= subject_index < len(self.marks):
            self.marks[subject_index] = new_mark
            print(f"Marks updated for student {self.name} (ID: {self.student_id}), Subject {subject_index + 1}.")
        else:
            print(f"Invalid subject index for student {self.name} (ID: {self.student_id}).")

    def display(self):
        """Display student information along with their marks."""
        print(f"Student ID: {self.student_id}, Name: {self.name}, Marks: {self.marks}")

    def calculate_average(self):
        """Calculate and return the average of the marks."""
        if self.marks:
            return sum(self.marks) / len(self.marks)
        return 0


class StudentManagementSystem:
    def __init__(self):
        """Initialize the system to manage students."""
        self.students = {}

    def add_student(self, student_id, student_name):
        """Add a new student to the system."""
        if student_id not in self.students:
            student = Student(student_id, student_name)
            self.students[student_id] = student
            print(f"Student {student_name} (ID: {student_id}) added successfully.")
        else:
            print(f"Student with ID {student_id} already exists.")

    def assign_marks(self, student_id, marks):
        """Assign marks to an existing student."""
        student = self.students.get(student_id)
        if student:
            student.assign_marks(marks)
        else:
            print(f"Student with ID {student_id} not found.")

    def update_marks(self, student_id, subject_index, new_mark):
        """Update marks for a student and a specific subject."""
        student = self.students.get(student_id)
        if student:
            student.update_marks(subject_index, new_mark)
        else:
            print(f"Student with ID {student_id} not found.")

    def display_all_students(self):
        """Display all students and their marks."""
        print("\nStudent List:")
        if self.students:
            for student in self.students.values():
                student.display()
        else:
            print("No students found.")

    def display_student_average(self, student_id):
        """Display the average marks of a student."""
        student = self.students.get(student_id)
        if student:
            average = student.calculate_average()
            print(f"Student ID {student_id} ({student.name}) Average Marks: {average:.2f}")
        else:
            print(f"Student with ID {student_id} not found.")


def main():
    system = StudentManagementSystem()

    while True:
        print("\n----- Student Mark Management System -----")
        print("1. Display all students and their marks")
        print("2. Add new student")
        print("3. Assign marks to student")
        print("4. Update marks for a student")
        print("5. Display student average marks")
        print("6. Exit")
        
        choice = input("Choose an option (1-6): ")

        if choice == '1':
            system.display_all_students()
        elif choice == '2':
            student_id = int(input("Enter student ID: "))
            student_name = input("Enter student name: ")
            system.add_student(student_id, student_name)
        elif choice == '3':
            student_id = int(input("Enter student ID: "))
            marks = list(map(int, input("Enter marks for the student (comma separated): ").split(',')))
            system.assign_marks(student_id, marks)
        elif choice == '4':
            student_id = int(input("Enter student ID: "))
            subject_index = int(input("Enter subject index to update (0 for first subject): "))
            new_mark = int(input("Enter new mark: "))
            system.update_marks(student_id, subject_index, new_mark)
        elif choice == '5':
            student_id = int(input("Enter student ID: "))
            system.display_student_average(student_id)
        elif choice == '6':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid option! Please choose a valid option (1-6).")

if __name__ == "__main__":
    main()
