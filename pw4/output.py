def display_menu(stdscr):
    """Display the menu for the system."""
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

def display_all_students(stdscr, system):
    """Display all students and their marks."""
    stdscr.clear()
    if system.students:
        for student in system.students.values():
            student.display()
    else:
        stdscr.addstr("No students found.")
    stdscr.refresh()

def display_student_gpa(stdscr, student_id, system):
    """Display the GPA of a student."""
    student = system.students.get(student_id)
    if student:
        gpa = student.calculate_gpa()
        stdscr.addstr(f"Student ID {student_id} ({student.name}) GPA: {gpa:.1f}")
    else:
        stdscr.addstr(f"Student with ID {student_id} not found.")
    stdscr.refresh()

def display_sorted_by_gpa(stdscr, system):
    """Display all students sorted by GPA."""
    sorted_students = sorted(system.students.values(), key=lambda s: s.calculate_gpa(), reverse=True)
    stdscr.clear()
    for student in sorted_students:
        student.display()
        stdscr.addstr(f"GPA: {student.calculate_gpa():.1f}\n")
    stdscr.refresh()

def show_message(stdscr, message):
    """Show a message and wait for user to press a key."""
    stdscr.addstr(message + "\nPress any key to continue...")
    stdscr.refresh()
    stdscr.getch()