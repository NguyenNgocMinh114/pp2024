import curses
from input import *
from output import *
from domains.system import StudentManagementSystem

def main(stdscr):
    # Initialize system
    system = StudentManagementSystem()

    while True:
        # Display the menu
        display_menu(stdscr)
        choice = stdscr.getstr().decode("utf-8")

        if choice == '1':
            display_all_students(stdscr, system)
        elif choice == '2':
            student_id = get_student_id(stdscr)
            student_name = get_student_name(stdscr)
            system.add_student(student_id, student_name)
        elif choice == '3':
            student_id = get_student_id(stdscr)
            marks, credits = get_marks_and_credits(stdscr)
            system.assign_marks(student_id, marks, credits)
        elif choice == '4':
            student_id = get_student_id(stdscr)
            subject_index = get_subject_index(stdscr)
            new_mark = get_new_mark(stdscr)
            system.update_marks(student_id, subject_index, new_mark)
        elif choice == '5':
            student_id = get_student_id(stdscr)
            display_student_gpa(stdscr, student_id, system)
        elif choice == '6':
            display_sorted_by_gpa(stdscr, system)
        elif choice == '7':
            show_message(stdscr, "Exiting the program. Goodbye!")
            break
        else:
            show_message(stdscr, "Invalid option! Please choose a valid option (1-7).")

if __name__ == "__main__":
    curses.wrapper(main)