# PedroClaveroDeDios_ProgrammingExercise_12.py
# This program uses numpy to analyze student grades stored in a CSV file.
# It loads the data, prints the first few rows, and calculates per-exam
# and overall statistics, including pass/fail counts and percentages.

import numpy as np
import os


def load_grades(filename):
    """
    Loads student exam grades from a CSV file into a numpy array.

    Parameters:
        filename (str): The path to the CSV file containing grade data.

    Variables:
        grades (np.ndarray): The numpy array of exam grades.

    Logic:
        1. Check if the CSV file exists.
        2. Use numpy genfromtxt to load only the exam columns (columns 2-4).
        3. Skip the header row.
        4. Return the loaded numpy array.

    Return:
        np.ndarray: A 2D numpy array where each row represents a student's exam grades.
    """

    # Check if the file exists
    if not os.path.exists(filename):
        print(f"Error: {filename} not found.")
        return None

    # Load only the numeric exam columns (skip name columns)
    grades = np.genfromtxt(
        filename,
        delimiter=",",
        skip_header=1,
        usecols=(2, 3, 4)
    )

    return grades


def display_first_rows(grades, num_rows=5):
    """
    Displays the first few rows of the grades dataset.

    Parameters:
        grades (np.ndarray): The numpy array of exam grades.
        num_rows (int): The number of rows to display.

    Variables:
        None

    Logic:
        1. Print a header showing the exam columns.
        2. Loop through the first num_rows of the array.
        3. Print each row in a formatted manner.

    Return:
        None
    """

    # Print header
    print(f"\n=== First {num_rows} Rows of Dataset ===\n")
    print(f"{'Student':<10}{'Exam 1':<10}{'Exam 2':<10}{'Exam 3':<10}")
    print("-" * 40)

    # Display each row with its index
    for i in range(min(num_rows, len(grades))):
        row = grades[i]
        print(f"{i + 1:<10}{row[0]:<10.1f}{row[1]:<10.1f}{row[2]:<10.1f}")


def calculate_exam_statistics(grades):
    """
    Calculates and prints mean, median, standard deviation, min, and max
    for each exam (column) in the grades array.

    Parameters:
        grades (np.ndarray): The numpy array of exam grades.

    Variables:
        num_exams (int): The number of exam columns.
        exam_column (np.ndarray): The column of grades for a specific exam.
        mean (float): The mean of the exam column.
        median (float): The median of the exam column.
        std_dev (float): The standard deviation of the exam column.
        minimum (float): The minimum value in the exam column.
        maximum (float): The maximum value in the exam column.

    Logic:
        1. Determine the number of exam columns.
        2. Loop through each exam column.
        3. Calculate mean, median, standard deviation, min, and max using numpy.
        4. Print the statistics for each exam.

    Return:
        None
    """

    print("\n=== Per-Exam Statistics ===\n")

    # Determine the number of exams from the number of columns
    num_exams = grades.shape[1]

    # Calculate and display statistics for each exam
    for i in range(num_exams):

        # Extract the current exam column
        exam_column = grades[:, i]

        # Calculate statistics using numpy
        mean = np.mean(exam_column)
        median = np.median(exam_column)
        std_dev = np.std(exam_column)
        minimum = np.min(exam_column)
        maximum = np.max(exam_column)

        # Display statistics for the current exam
        print(f"--- Exam {i + 1} ---")
        print(f"  Mean:               {mean:.2f}")
        print(f"  Median:             {median:.2f}")
        print(f"  Standard Deviation: {std_dev:.2f}")
        print(f"  Minimum:            {minimum:.2f}")
        print(f"  Maximum:            {maximum:.2f}")
        print()


def calculate_overall_statistics(grades):
    """
    Calculates and prints overall statistics across all exams combined.

    Parameters:
        grades (np.ndarray): The numpy array of exam grades.

    Variables:
        mean (float): The overall mean grade.
        median (float): The overall median grade.
        std_dev (float): The overall standard deviation.
        minimum (float): The overall minimum grade.
        maximum (float): The overall maximum grade.

    Logic:
        1. Calculate statistics over the entire numpy array (all exams combined).
        2. Print each overall statistic.

    Return:
        None
    """

    print("=== Overall Statistics (All Exams Combined) ===\n")

    # Calculate statistics across the entire dataset
    mean = np.mean(grades)
    median = np.median(grades)
    std_dev = np.std(grades)
    minimum = np.min(grades)
    maximum = np.max(grades)

    # Display the overall statistics
    print(f"  Overall Mean:               {mean:.2f}")
    print(f"  Overall Median:             {median:.2f}")
    print(f"  Overall Standard Deviation: {std_dev:.2f}")
    print(f"  Overall Minimum:            {minimum:.2f}")
    print(f"  Overall Maximum:            {maximum:.2f}")
    print()


def calculate_pass_fail(grades, passing_grade=60):
    """
    Determines and prints the number of students who passed and failed
    each exam, and the overall pass percentage across all exams.

    Parameters:
        grades (np.ndarray): The numpy array of exam grades.
        passing_grade (int): The minimum grade required to pass.

    Variables:
        num_exams (int): The number of exam columns.
        exam_column (np.ndarray): The column of grades for a specific exam.
        passed (int): The number of students who passed the exam.
        failed (int): The number of students who failed the exam.
        total_passed (int): The total number of passing grades across all exams.
        total_grades (int): The total number of grades in the dataset.
        pass_percentage (float): The overall pass percentage.

    Logic:
        1. Determine the number of exam columns.
        2. Loop through each exam column.
        3. Count the number of grades at or above the passing grade.
        4. Count the number of grades below the passing grade.
        5. Print pass/fail counts for each exam.
        6. Calculate the overall pass percentage across all exams.
        7. Print the overall pass percentage.

    Return:
        None
    """

    print(f"=== Pass/Fail Analysis (Passing Grade = {passing_grade}) ===\n")

    # Determine the number of exams
    num_exams = grades.shape[1]

    # Calculate pass/fail counts for each exam
    for i in range(num_exams):

        # Extract the current exam column
        exam_column = grades[:, i]

        # Count passed and failed students
        passed = np.sum(exam_column >= passing_grade)
        failed = np.sum(exam_column < passing_grade)

        # Display the results for the current exam
        print(f"--- Exam {i + 1} ---")
        print(f"  Passed: {passed}")
        print(f"  Failed: {failed}")
        print()

    # Calculate overall pass percentage across all exams
    total_passed = np.sum(grades >= passing_grade)
    total_grades = grades.size
    pass_percentage = (total_passed / total_grades) * 100

    # Display the overall pass percentage
    print("=== Overall Pass Percentage ===\n")
    print(f"  Total grades:        {total_grades}")
    print(f"  Total passing:       {total_passed}")
    print(f"  Overall pass rate:   {pass_percentage:.2f}%")
    print()


def main():
    """
    Main function that runs the grade analysis program.

    Parameters:
        None

    Variables:
        filename (str): The name of the CSV file to load.
        grades (np.ndarray): The numpy array of loaded grades.

    Logic:
        1. Display a welcome message.
        2. Load the grades from the CSV file.
        3. Check that the data was loaded successfully.
        4. Display the first few rows of the dataset.
        5. Calculate and display per-exam statistics.
        6. Calculate and display overall statistics.
        7. Calculate and display pass/fail counts and overall pass percentage.

    Return:
        None
    """

    # Display welcome message
    print("Welcome to the Student Grade Analyzer!")
    print("This program uses numpy to analyze exam grades from a CSV file.")

    # Define the CSV filename
    filename = "grades.csv"

    # Load the grades from the CSV file
    grades = load_grades(filename)

    # Check that grades were loaded successfully
    if grades is None:
        print("Unable to continue without data. Exiting.")
        return

    # Display the first few rows
    display_first_rows(grades, num_rows=5)

    # Calculate and display per-exam statistics
    calculate_exam_statistics(grades)

    # Calculate and display overall statistics
    calculate_overall_statistics(grades)

    # Calculate and display pass/fail analysis
    calculate_pass_fail(grades, passing_grade=60)

    # Display completion message
    print("Analysis complete. Thank you for using the Grade Analyzer!")


# Program entry point
if __name__ == "__main__":
    main()
