import math
import numpy as np
import curses

class Student:
    def __init__(self, student_id, name, marks=None, credits=None):
        """Initialize the student object with ID, name, marks, and credits."""
        self.student_id = student_id
        self.name = name
        self.marks = np.array(marks) if marks else np.array([])  # Using numpy array for marks
        self.credits = np.array(credits) if credits else np.array([])  # Using numpy array for credits

    def assign_marks(self, marks, credits):
        """Assign marks and credits to the student."""
        self.marks = np.array(marks)
        self.credits = np.array(credits)
        print(f"Marks and credits updated for student {self.name} (ID: {self.student_id}).")

    def update_marks(self, subject_index, new_mark):
        """Update the marks for a specific subject."""
        if 0 <= subject_index < len(self.marks):
            self.marks[subject_index] = new_mark
            print(f"Marks updated for student {self.name} (ID: {self.student_id}), Subject {subject_index + 1}.")
        else:
            print(f"Invalid subject index for student {self.name} (ID: {self.student_id}).")

    def display(self):
        """Display student information along with their marks and credits."""
        print(f"Student ID: {self.student_id}, Name: {self.name}, Marks: {self.marks}, Credits: {self.credits}")

    def calculate_gpa(self):
        """Calculate and return the GPA (weighted average of marks)."""
        if len(self.marks) > 0 and len(self.credits) > 0:
            weighted_sum = np.sum(self.marks * self.credits)
            total_credits = np.sum(self.credits)
            if total_credits > 0:
                gpa = weighted_sum / total_credits
                return round(gpa, 1)  # Round GPA to 1 decimal place
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

    def assign_marks(self, student_id, marks, credits):
        """Assign marks and credits to an existing student."""
        student = self.students.get(student_id)
        if student:
            student.assign_marks(marks, credits)
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

    def display_student_gpa(self, student_id):
        """Display the GPA of a student."""
        student = self.students.get(student_id)
        if student:
            gpa = student.calculate_gpa()
            print(f"Student ID {student_id} ({student.name}) GPA: {gpa:.1f}")
        else:
            print(f"Student with ID {student_id} not found.")

    def sort_students_by_gpa(self):
        """Sort students by GPA in descending order."""
        sorted_students = sorted(self.students.values(), key=lambda s: s.calculate_gpa(), reverse=True)
        print("\nSorted Students by GPA:")
        for student in sorted_students:
            student.display()
            print(f"GPA: {student.calculate_gpa():.1f}")

def main(stdscr):
    # Clear screen
    curses.curs_set(0)
    stdscr.clear()

    system = StudentManagementSystem()

    while True:
        stdscr.clear()
        stdscr.addstr("\n----- Student Mark Management System -----\n")
        stdscr.addstr("1. Display all students and their marks\n")
        stdscr.addstr("2. Add new student\n")
        stdscr.addstr("3. Assign marks to student\n")
        stdscr.addstr("4. Update marks for a student\n")
        stdscr.addstr("5. Display student GPA\n")
        stdscr.addstr("6. Sort students by GPA\n")
        stdscr.addstr("7. Exit\n")
        
        stdscr.addstr("Choose an option (1-7): ")
        stdscr.refresh()
        
        choice = stdscr.getstr().decode("utf-8")

        if choice == '1':
            system.display_all_students()
        elif choice == '2':
            stdscr.addstr("Enter student ID: ")
            stdscr.refresh()
            student_id = int(stdscr.getstr().decode("utf-8"))
            stdscr.addstr("Enter student name: ")
            stdscr.refresh()
            student_name = stdscr.getstr().decode("utf-8")
            system.add_student(student_id, student_name)
        elif choice == '3':
            stdscr.addstr("Enter student ID: ")
            stdscr.refresh()
            student_id = int(stdscr.getstr().decode("utf-8"))
            stdscr.addstr("Enter marks for the student (comma separated): ")
            stdscr.refresh()
            marks = list(map(lambda x: math.floor(float(x) * 10) / 10, stdscr.getstr().decode("utf-8").split(',')))  # Round down marks
            stdscr.addstr("Enter credits for the student (comma separated): ")
            stdscr.refresh()
            credits = list(map(int, stdscr.getstr().decode("utf-8").split(',')))
            system.assign_marks(student_id, marks, credits)
        elif choice == '4':
            stdscr.addstr("Enter student ID: ")
            stdscr.refresh()
            student_id = int(stdscr.getstr().decode("utf-8"))
            stdscr.addstr("Enter subject index to update (0 for first subject): ")
            stdscr.refresh()
            subject_index = int(stdscr.getstr().decode("utf-8"))
            stdscr.addstr("Enter new mark: ")
            stdscr.refresh()
            new_mark = float(stdscr.getstr().decode("utf-8"))
            new_mark = math.floor(new_mark * 10) / 10  # Round down
            system.update_marks(student_id, subject_index, new_mark)
        elif choice == '5':
            stdscr.addstr("Enter student ID: ")
            stdscr.refresh()
            student_id = int(stdscr.getstr().decode("utf-8"))
            system.display_student_gpa(student_id)
        elif choice == '6':
            system.sort_students_by_gpa()
        elif choice == '7':
            stdscr.addstr("Exiting the program. Goodbye!\n")
            stdscr.refresh()
            break
        else:
            stdscr.addstr("Invalid option! Please choose a valid option (1-7).\n")
            stdscr.refresh()

        stdscr.addstr("\nPress any key to continue...")
        stdscr.getch()

if __name__ == "__main__":
    curses.wrapper(main)