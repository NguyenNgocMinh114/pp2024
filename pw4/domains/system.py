from .student import Student

class StudentManagementSystem:
    def __init__(self):
        """Initialize the system to manage students."""
        self.students = {}

    def add_student(self, student_id, student_name):
        """Add a new student to the system."""
        if student_id not in self.students:
            student = Student(student_id, student_name)
            self.students[student_id] = student
        else:
            raise ValueError("Student ID already exists.")

    def assign_marks(self, student_id, marks, credits):
        """Assign marks and credits to an existing student."""
        student = self.students.get(student_id)
        if student:
            student.assign_marks(marks, credits)
        else:
            raise ValueError(f"Student with ID {student_id} not found.")

    def update_marks(self, student_id, subject_index, new_mark):
        """Update marks for a student and a specific subject."""
        student = self.students.get(student_id)
        if student:
            student.update_marks(subject_index, new_mark)
        else:
            raise ValueError(f"Student with ID {student_id} not found.")

    def display_all_students(self):
        """Display all students and their marks."""
        return self.students.values()

    def display_student_gpa(self, student_id):
        """Display the GPA of a student."""
        student = self.students.get(student_id)
        if student:
            return student.calculate_gpa()
        return 0

    def sort_students_by_gpa(self):
        """Sort students by GPA in descending order."""
        return sorted(self.students.values(), key=lambda s: s.calculate_gpa(), reverse=True)