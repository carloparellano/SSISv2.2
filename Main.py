import student
import course


def prompt_course():
    while True:
        print("Simple Course Information System")
        print("1. Add Course")
        print("2. View Course")
        print("3. Edit Course")
        print("4. Delete Course")
        print("5. Search Course")
        print("6. Back")
        choice2 = input("Enter your choice: ")
        print()
        if choice2 == '1':
            course.add_course()
        elif choice2 == '2':
            course.view_course()
        elif choice2 == '3':
            course.edit_course()
        elif choice2 == '4':
            course.delete_course()
        elif choice2 == '5':
            course.search_course()
        elif choice2 == '6':
            break  # exits the while loop, back to the main choices
        else:
            print("Invalid choice.\n")


def prompt_student():
    while True:
        print("Simple Student Information System")
        print("1. Add Students")
        print("2. View Student")
        print("3. Edit Student")
        print("4. Delete Student")
        print("5. Search Student")
        print("6. Back")
        choice2 = input("Enter your choice: ")
        print()
        if choice2 == '1':
            student.add_student()
        elif choice2 == '2':
            student.view_students()
        elif choice2 == '3':
            student.edit_student()
        elif choice2 == '4':
            student.delete_student()
        elif choice2 == '5':
            student.search_student()
        elif choice2 == '6':  # exits the while loop, back to the main choices
            break
        else:
            print("Invalid choice.\n")


if __name__ == "__main__":  # checks if the py file is the main py file, runs file if true
    while True:  # continues to execute the next lines until it is false
        print("1. CRUDL for Students\n2. CRUDL for Courses\n3. Exit")
        choice1 = input("Enter your choice: ")
        print()  # for spacing purposes
        if choice1 == '1':  
            prompt_student()
        elif choice1 == '2':  
            prompt_course()
        elif choice1 == '3':  
            break 
        else:
            print("Invalid choice.\n")