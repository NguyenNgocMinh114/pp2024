students = [
    (101, 'Alice'),
    (102, 'Bob'),
    (103, 'Charlie')
]

marks_dict = {
    101: [85, 90, 78],
    102: [92, 88, 79],
    103: [75, 80, 82]
}

def display_students():
    print("\nStudent List:")
    for student_id, student_name in students:
        marks = marks_dict.get(student_id, [])
        print(f"Student ID: {student_id}, Name: {student_name}, Marks: {marks}")

def add_student(student_id, student_name):
    students.append((student_id, student_name))
    marks_dict[student_id] = []  
    print(f"Student {student_name} added successfully.")

def assign_marks(student_id, marks):
    if student_id in marks_dict:
        marks_dict[student_id] = marks
        print(f"Marks updated for student ID {student_id}.")
    else:
        print(f"Student with ID {student_id} not found.")

def update_marks(student_id, subject_index, new_mark):
    if student_id in marks_dict and 0 <= subject_index < len(marks_dict[student_id]):
        marks_dict[student_id][subject_index] = new_mark
        print(f"Marks updated for student ID {student_id}, Subject {subject_index + 1}.")
    else:
        print(f"Invalid student ID or subject index.")

def display_average(student_id):
    if student_id in marks_dict:
        marks = marks_dict[student_id]
        average = sum(marks) / len(marks) if marks else 0
        print(f"Student ID {student_id} Average Marks: {average:.2f}")
    else:
        print(f"Student with ID {student_id} not found.")

def main():
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
            display_students()
        elif choice == '2':
            student_id = int(input("Enter student ID: "))
            student_name = input("Enter student name: ")
            add_student(student_id, student_name)
        elif choice == '3':
            student_id = int(input("Enter student ID: "))
            marks = list(map(int, input("Enter marks for the student (comma separated): ").split(',')))
            assign_marks(student_id, marks)
        elif choice == '4':
            student_id = int(input("Enter student ID: "))
            subject_index = int(input("Enter subject index to update (0 for first subject): "))
            new_mark = int(input("Enter new mark: "))
            update_marks(student_id, subject_index, new_mark)
        elif choice == '5':
            student_id = int(input("Enter student ID: "))
            display_average(student_id)
        elif choice == '6':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid option! Please choose a valid option (1-6).")

if __name__ == "__main__":
    main()
