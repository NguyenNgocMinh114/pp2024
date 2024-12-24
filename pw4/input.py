import math

def get_student_id(stdscr):
    """Get student ID from the user."""
    stdscr.addstr("Enter student ID: ")
    stdscr.refresh()
    student_id = int(stdscr.getstr().decode("utf-8"))
    return student_id

def get_student_name(stdscr):
    """Get student name from the user."""
    stdscr.addstr("Enter student name: ")
    stdscr.refresh()
    student_name = stdscr.getstr().decode("utf-8")
    return student_name

def get_marks_and_credits(stdscr):
    """Get marks and credits for a student."""
    stdscr.addstr("Enter marks for the student (comma separated): ")
    stdscr.refresh()
    marks = list(map(lambda x: math.floor(float(x) * 10) / 10, stdscr.getstr().decode("utf-8").split(',')))  # Round down marks

    stdscr.addstr("Enter credits for the student (comma separated): ")
    stdscr.refresh()
    credits = list(map(int, stdscr.getstr().decode("utf-8").split(',')))

    return marks, credits

def get_subject_index(stdscr):
    """Get subject index from the user to update marks."""
    stdscr.addstr("Enter subject index to update (0 for first subject): ")
    stdscr.refresh()
    return int(stdscr.getstr().decode("utf-8"))

def get_new_mark(stdscr):
    """Get new mark to update for a subject."""
    stdscr.addstr("Enter new mark: ")
    stdscr.refresh()
    new_mark = float(stdscr.getstr().decode("utf-8"))
    return math.floor(new_mark * 10) / 10  # Round down
