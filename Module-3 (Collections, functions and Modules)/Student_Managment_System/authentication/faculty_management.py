# Function to check if a student belongs to a specific faculty
def is_faculty_student(faculty_id, roll_id):
    return True
 
# Function to add marks to a student
def add_marks(faculty_id,roll_id):
    roll_id = input("Enter Roll ID of the student: ")

    # Check if the student belongs to this faculty
    if is_faculty_student(faculty_id, roll_id):
        marks = float(input("Enter Marks: "))
        print("Marks added successfully.")
       
    else:
        print("This student doesn't belong to your faculty.")

# Function to view students belonging to a specific faculty
def view_own_students(faculty_id):
    print("Your students:")

# Function to manage the faculty menu
def faculty_menu():
    faculty_id = input("Enter Faculty ID: ")
    print("\nFaculty Menu:")
    while True:
        print("1. Add Mark to Student")
        print("2. View All Students")
        print("3.Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_marks(faculty_id)
        elif choice == '2':
            view_own_students(faculty_id)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please select a valid option.")



