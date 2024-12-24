import numpy as np

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

    def update_marks(self, subject_index, new_mark):
        """Update the marks for a specific subject."""
        if 0 <= subject_index < len(self.marks):
            self.marks[subject_index] = new_mark
        else:
            raise ValueError("Invalid subject index.")

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