#~~~~~~~~~~~~~~~~~~~~~~~~~~~A Simple Student Management System in Python :-~~~~~~~~~~~~~~~~~~~~~~~~~~~
# We can add students, show student details, and find the top student based on marks.
# It also stores student information in a dictionary for easy access and management.

student = {}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~functions to manage students~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ADD STUDENT: This function takes the student's name, age, grade, and marks as input and adds the student to the dictionary.
def add_student(name, age, grade, marks):
    student[name] = {
        "age": age,
        "grade": grade ,
        "marks": marks
        }
# SHOW STUDENT: This function takes the student's name as input and displays the student's details if found in the dictionary. If the student is not found, it prints a message indicating that the student was not found.    
def show_student(name):
    if name in student:
        print(f"Name: {name}, Age: {student[name]['age']}, Grade: {student[name]['grade']}, Marks: {student[name]['marks']}")
    else:
        print("Student not found.")  
# TOP STUDENT: This function calculates and displays the student with the highest marks. It uses the max function with a lambda function to find the student with the maximum marks in the dictionary. If there are no students, it prints a message indicating that no students are available.
def top_student():
    if student:
        top = max(student, key=lambda x: student[x]['marks'])
        print(f"Top student is {top} with marks {student[top]['marks']}")
    else:
        print("No students available.")
# DELETE STUDENT: This function takes the student's name as input and deletes the student from the dictionary if found. If the student is not found, it prints a message indicating that the student does not exist.
def delete_student(name):
    if name in student:
        del student[name]
        print(f"Student {name} deleted successfully.")
    else:        print("Student does not exist.")    
# UPDATE STUDENT: This function takes the student's name and optional parameters for age, grade, and marks. It updates the student's details in the dictionary if the student exists. If the student does not exist, it prints a message indicating that the student does not exist.
def update_student(name, age=None, grade=None, marks=None): 
    if name in student:
        if age is not None:
            student[name]['age'] = age
        if grade is not None:
            student[name]['grade'] = grade
        if marks is not None:
            student[name]['marks'] = marks
        print(f"Student {name} updated successfully.")
    else:
        print("Student does not exist.")
# SHOW ALL STUDENTS: This function displays the details of all students in the dictionary. If there are no students, it prints a message indicating that no students are available.
def show_all_students():
    if student:
        for name, data in student.items():
            print(f"{name} -> {data}")
    else:
        print("No students available")
# We also have two additional functions, save_data and load_data, to save the student information to a JSON file and load it back when the program starts. This allows us to persist the student data across sessions. The save_data function writes the student dictionary to a file named "students.json", while the load_data function reads from the same file and populates the student dictionary when the program starts. If the file does not exist or an error occurs during loading, it initializes an empty student dictionary.
import json
# SAVE DATA: This function saves the current state of the student dictionary to a JSON file named "students.json". It uses the json.dump method to write the dictionary to the file in JSON format. This allows us to persist the student data across sessions, so that when we run the program again, we can load the existing student data from the file.
def save_data():
    with open("students.json", "w") as f:
        json.dump(student, f)
# LOAD DATA: This function attempts to load student data from a JSON file named "students.json". If the file exists and is properly formatted, it populates the global student dictionary with the data from the file. If the file does not exist or an error occurs during loading (such as a JSON decoding error), it initializes the student dictionary as an empty dictionary. This allows the program to start with existing student data if available, or start fresh if no data is found.
def load_data():
    global student
    try:
        with open("students.json", "r") as f:
            student = json.load(f)
    except:
        student = {}

# Load existing student data when the program starts
load_data()

# Main loop to interact with the user
while True:
    print("Welcome to the Student Management System")
    print("\n1. Add Student")
    print("2. Show Student")
    print("3. Top Student")
    print("4. Delete Student")
    print("5. Update Student")
    print("6. Show All Students")
    print("7. Exit")

    choice = input("Enter your choice(1,2,3,4,5,6,7): ")
# Based on the user's choice, we call the appropriate function to manage students. The loop continues until the user chooses to exit.
    if choice == "1":
        try:
            name = input("Enter student's name: ").strip().title()
            age = int(input("Enter student's age: "))
            grade = input("Enter student's grade: ")
            marks = float(input("Enter student's marks: "))
            add_student(name, age, grade, marks)
            print(f"Student {name} added successfully!")
        except ValueError:
            print("Invalid input. Age must be an integer and marks must be a number.")
        except Exception as e:
            print(f"An error occurred: {e}")

# If the user chooses to show student details, we prompt them to enter the student's name and call the show_student function to display the details.
    elif choice == "2":
        name = input("Enter student's name to show details: ")
        print("Student details:")
        show_student(name)

# If the user chooses to find the top student, we call the top_student function which calculates and displays the student with the highest marks.
    elif choice == "3":
        print(f"The top student is:")
        top_student()
        
# If the user chooses to delete a student, we prompt them to enter the student's name and call the delete_student function.
    elif choice == "4":
        name = input("Enter student's name to delete: ")
        delete_student(name)
# If the user chooses to update a student's details, we prompt them to enter the student's name and the new details. We then call the update_student function with the provided information. The user can choose to update any of the details (age, grade, marks) or keep them unchanged by pressing Enter. 
    elif choice == "5":
        name = input("Enter student's name to update: ")
        print("Enter new details (press Enter to keep current value):")
        age = input("Enter new age: ")
        grade = input("Enter new grade: ")
        marks = input("Enter new marks: ")
        update_student(name, age=int(age) if age else None, grade=grade if grade else None, marks=float(marks) if marks else None)
# If the user chooses to show all students, we call the show_all_students function.
    elif choice == "6":
        show_all_students()
# If the user chooses to exit the system, we print a goodbye message and break the loop to end the program.
    elif choice == "7":
        print("Exiting the system. Goodbye!. if you want any help, just come again.")
        break

# If the user enters an invalid choice, we print an error message and prompt them to try again.
    else:
        print("Invalid choice. Please try again.")
