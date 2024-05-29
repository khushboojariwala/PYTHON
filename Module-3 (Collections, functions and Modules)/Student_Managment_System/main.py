from authentication import counselor_management,faculty_management,student
# Import modules for counselor, faculty, and student managemen

# Function to display the main menu and call to different management systems
def main():
    while True:
        print("\nMain Menu:")
        print("Press 1 for Counselor")
        print("Press 2 for Faculty")
        print("Press 3 for Student")
        choice = input("Enter your choice: ")

        if choice == '1':
            counselor_management.student_menu()
        elif choice == '2':
            faculty_management.faculty_menu()
        elif choice == '3':
            student.get_student_by_id()
            break
        else:
            print("Invalid choice. Please select a valid option.")

main()  #call main function