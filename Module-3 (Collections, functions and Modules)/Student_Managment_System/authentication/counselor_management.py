students = {}
# Store student information in a dictionary
student_id=0   # Initialize student_id to 0

# Function to add a new student
def add_student():
    global student_id
    student_id += 1       # Increment student_id to generate a new unique roll ID
    roll_id=student_id

    #input student information
    while True:
        student_id = input("Enter Roll ID: ")
        if student_id in students:
            print("Student with this Roll ID already exists.")
        else:
            break

    while True:
        first_name = input("Enter First Name: ")
        if not is_valid_name(first_name):
            print("Invalid first name. Please enter a valid name.")
        else:
            break

    while True:
        last_name = input("Enter Last Name: ")
        if not is_valid_name(last_name):
            print("Invalid last name. Please enter a valid name.")
        else:
            break

    while True:
        contact_number = input("Enter Contact Number: ")
        if not is_valid_contact_number(contact_number):
            print("Invalid contact number. Please enter a 10-digit numeric value.")
        else:
            break

    subject_name = input("Enter Subject Name: ")
    marks = input("Enter Marks: ")
    fees = input("Enter Fees: ")

    # Add the student's information to the dictionary
    students[roll_id] = {
        'first_name': first_name,
        'last_name': last_name,
        'contact_number': contact_number,
        'subject_name': subject_name,
        'marks': marks,
        'fees': fees
    }
    print("Student added successfully.")

# Function to check if a contact number is valid
def is_valid_contact_number(contact_number):
    if contact_number.isdigit() and len(contact_number) == 10:
        return True
    else:
        return False

#Function to check if a name is valid
def is_valid_name(name):
    if name.isalpha():
        return True
    else:
        return False
    
# Function to remove a student
def remove_student():
    roll_id = input("Enter Roll ID to remove: ")
    if roll_id in students:
        del students[roll_id]
        print("Student removed successfully.")
    else:
        print("Student with this Roll ID not found.")

# Function to view information of a specific student
def view_specific_student():
    roll_id = input("Enter Roll ID of the student to view: ")
    student_info = students.get(roll_id)
    if student_info:
        print("\nStudent Details:")
        print(f"Roll ID: {roll_id}")
        print(f"First Name: {student_info['first_name']}")
        print(f"Contact Number: {student_info['contact_number']}")
        confirmation = input("Are you sure you want to delete this student (Y/N)? ").strip().lower()
        if confirmation == 'y':
            remove_student(roll_id)
        else:
            print("Deletion canceled.")
    else:
        print(f"Student with Roll ID {roll_id} not found.")

# Function to view information of all students
def view_all_students():
    if students:
        print("\nAll Students:")
        for roll_id, student_info in students.items():
            print(f"Roll ID: {roll_id}")
            print(f"First Name: {student_info['first_name']}")
            print(f"Contact Number: {student_info['contact_number']}")
            print("-" * 20)
    else:
        print("No students to display.")

# Function to display all student details
def display_students():
    if students:
        print("Student Details:")
        for roll_id, student_info in students.items():
            print(f"{roll_id}: {student_info}")
    else:
        print("No students to display.")

# Function to manage the student menu
def student_menu():
    while True:
        print("\nStudent Menu:")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. View Specific Student")
        print("4. View All Students")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            remove_student()
        elif choice == '3':
            view_specific_student()
        elif choice == '4':
            view_all_students()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please select a valid option.")

        more_operations = input("Do you want to perform more operations? (y/n) ").strip().lower()
        if more_operations != 'y':
            break