# PedroClaveroDeDios_ProgrammingExercise_CSV.py
# This program allows an instructor to input student names and exam grades,
# writes them to a grades.csv file, and can read and display the data
# in tabular format.

import csv
import os


def get_student_data():
    """
    Prompts the instructor to enter student names and three exam grades.

    Parameters:
        None

    Variables:
        num_students (int): The number of students to enter.
        students (list): A list of lists containing each student's data.
        first_name (str): The student's first name.
        last_name (str): The student's last name.
        exam1 (int): The student's first exam grade.
        exam2 (int): The student's second exam grade.
        exam3 (int): The student's third exam grade.

    Logic:
        1. Ask the instructor how many students they want to enter.
        2. Loop through the number of students.
        3. For each student, prompt for first name, last name, and three exam grades.
        4. Append each student's data as a list to the students list.
        5. Return the list of student data.

    Return:
        list: A list of lists, each containing first name, last name, and three exam grades.
    """

    # Ask for the number of students
    num_students = int(input("How many students would you like to enter? "))

    # Initialize list to hold all student data
    students = []

    # Loop through each student
    for i in range(num_students):

        print(f"\n--- Student {i + 1} ---")

        # Get student name
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")

        # Get three exam grades
        exam1 = int(input("Enter Exam 1 grade: "))
        exam2 = int(input("Enter Exam 2 grade: "))
        exam3 = int(input("Enter Exam 3 grade: "))

        # Add student data to the list
        students.append([first_name, last_name, exam1, exam2, exam3])

    return students


def write_grades_csv(students):
    """
    Writes student data to a grades.csv file using the csv module.

    Parameters:
        students (list): A list of lists containing each student's data.

    Variables:
        header (list): The header row for the CSV file.
        csv_file (file): The file object for grades.csv.
        writer (csv.writer): The CSV writer object.

    Logic:
        1. Define the header row with column names.
        2. Open grades.csv for writing using the with keyword.
        3. Create a csv.writer object.
        4. Write the header row.
        5. Write each student's data as a row.
        6. Display a confirmation message.

    Return:
        None
    """

    # Define the header row
    header = ["First Name", "Last Name", "Exam 1", "Exam 2", "Exam 3"]

    # Open the file and write data using with keyword
    with open("grades.csv", "w", newline="") as csv_file:

        # Create csv writer object
        writer = csv.writer(csv_file)

        # Write the header row
        writer.writerow(header)

        # Write each student record
        for student in students:
            writer.writerow(student)

    print("\nStudent data has been written to grades.csv successfully.")


def read_grades_csv():
    """
    Reads the grades.csv file and displays data in tabular format.

    Parameters:
        None

    Variables:
        csv_file (file): The file object for grades.csv.
        reader (csv.reader): The CSV reader object.
        header (list): The header row from the CSV file.
        row (list): A row of student data from the CSV file.

    Logic:
        1. Check if grades.csv exists.
        2. Open grades.csv for reading using the with keyword.
        3. Create a csv.reader object.
        4. Read the header row and display it formatted.
        5. Print a separator line.
        6. Read and display each student record in tabular format.

    Return:
        None
    """

    # Check if the file exists
    if not os.path.exists("grades.csv"):
        print("Error: grades.csv not found. Please create the file first.")
        return

    # Open the file for reading using with keyword
    with open("grades.csv", "r") as csv_file:

        # Create csv reader object
        reader = csv.reader(csv_file)

        # Read and display the header row
        header = next(reader)
        print(f"\n{'First Name':<15}{'Last Name':<15}{'Exam 1':<10}{'Exam 2':<10}{'Exam 3':<10}")

        # Print separator line
        print("-" * 60)

        # Read and display each student record
        for row in reader:
            print(f"{row[0]:<15}{row[1]:<15}{row[2]:<10}{row[3]:<10}{row[4]:<10}")


def main():
    """
    Main function that runs the grade management program.

    Parameters:
        None

    Variables:
        choice (str): The user's menu selection.
        students (list): The list of student data entered by the instructor.

    Logic:
        1. Display a welcome message.
        2. Enter a loop to present a menu to the user.
        3. Option 1: Get student data and write to grades.csv.
        4. Option 2: Read grades.csv and display in tabular format.
        5. Option 3: Exit the program.
        6. Repeat until the user chooses to exit.

    Return:
        None
    """

    # Display welcome message
    print("Welcome to the Student Grade Manager!")
    print("This program writes and reads student grades using a CSV file.\n")

    # Loop for menu
    while True:

        # Display menu options
        print("Menu:")
        print("  1. Enter student grades and save to grades.csv")
        print("  2. Display grades from grades.csv")
        print("  3. Exit")

        # Get user choice
        choice = input("\nEnter your choice (1, 2, or 3): ").strip()

        # Process user choice
        if choice == "1":

            # Get student data from instructor
            students = get_student_data()

            # Write data to CSV file
            write_grades_csv(students)
            print()

        elif choice == "2":

            # Read and display CSV data
            read_grades_csv()
            print()

        elif choice == "3":

            # Exit the program
            print("\nThank you for using the Student Grade Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.\n")


# Program entry point
if __name__ == "__main__":
    main()
