# PedroClaveroDeDios_ProgrammingExercise_6.py
# This program validates phone numbers, social security numbers,
# and zip codes using regular expressions.

import re


def validate_phone_number(phone):
    """
    Validates a phone number using a regular expression.

    Parameters:
        phone (str): The phone number string to validate.

    Variables:
        pattern (str): The regular expression pattern for valid phone numbers.
        match (re.Match or None): The result of matching the phone string against the pattern.

    Logic:
        1. Define a regex pattern that accepts common US phone number formats.
        2. Use re.fullmatch to check if the entire string matches the pattern.
        3. Return True if there is a match, False otherwise.

    Return:
        bool: True if the phone number is valid, False otherwise.
    """

    # Define pattern for US phone numbers
    # Accepts: (xxx) xxx-xxxx, xxx-xxx-xxxx, xxx.xxx.xxxx, xxx xxx xxxx, xxxxxxxxxx
    pattern = r'(\(\d{3}\)\s?|\d{3}[-.\s]?)\d{3}[-.\s]?\d{4}'

    # Check if the entire input matches the pattern
    match = re.fullmatch(pattern, phone)

    return match is not None


def validate_ssn(ssn):
    """
    Validates a social security number using a regular expression.

    Parameters:
        ssn (str): The social security number string to validate.

    Variables:
        pattern (str): The regular expression pattern for valid SSNs.
        match (re.Match or None): The result of matching the SSN string against the pattern.

    Logic:
        1. Define a regex pattern that matches the standard SSN format (xxx-xx-xxxx).
        2. Ensure the SSN does not start with 000, 666, or 900-999 per SSA rules.
        3. Use re.fullmatch to check if the entire string matches the pattern.
        4. Return True if there is a match, False otherwise.

    Return:
        bool: True if the SSN is valid, False otherwise.
    """

    # Define pattern for SSN in format xxx-xx-xxxx
    # First three digits cannot be 000, 666, or 900-999
    pattern = r'(?!000|666|9\d{2})\d{3}-(?!00)\d{2}-(?!0000)\d{4}'

    # Check if the entire input matches the pattern
    match = re.fullmatch(pattern, ssn)

    return match is not None


def validate_zip_code(zip_code):
    """
    Validates a zip code using a regular expression.

    Parameters:
        zip_code (str): The zip code string to validate.

    Variables:
        pattern (str): The regular expression pattern for valid zip codes.
        match (re.Match or None): The result of matching the zip code string against the pattern.

    Logic:
        1. Define a regex pattern that matches 5-digit or 9-digit (ZIP+4) zip codes.
        2. Use re.fullmatch to check if the entire string matches the pattern.
        3. Return True if there is a match, False otherwise.

    Return:
        bool: True if the zip code is valid, False otherwise.
    """

    # Define pattern for 5-digit zip code with optional 4-digit extension
    # Accepts: xxxxx or xxxxx-xxxx
    pattern = r'\d{5}(-\d{4})?'

    # Check if the entire input matches the pattern
    match = re.fullmatch(pattern, zip_code)

    return match is not None


def get_user_input():
    """
    Prompts the user to enter a phone number, SSN, and zip code.

    Parameters:
        None

    Variables:
        phone (str): The phone number entered by the user.
        ssn (str): The social security number entered by the user.
        zip_code (str): The zip code entered by the user.

    Logic:
        1. Prompt the user to enter a phone number.
        2. Prompt the user to enter a social security number.
        3. Prompt the user to enter a zip code.
        4. Return all three values as a tuple.

    Return:
        tuple: A tuple containing the phone number, SSN, and zip code strings.
    """

    # Prompt user for a phone number
    phone = input("Enter a phone number (e.g., (555) 123-4567): ")

    # Prompt user for a social security number
    ssn = input("Enter a social security number (e.g., 123-45-6789): ")

    # Prompt user for a zip code
    zip_code = input("Enter a zip code (e.g., 12345 or 12345-6789): ")

    return phone, ssn, zip_code


def display_results(phone, ssn, zip_code):
    """
    Validates and displays the results for each input.

    Parameters:
        phone (str): The phone number to validate and display.
        ssn (str): The social security number to validate and display.
        zip_code (str): The zip code to validate and display.

    Variables:
        phone_valid (bool): Whether the phone number is valid.
        ssn_valid (bool): Whether the SSN is valid.
        zip_valid (bool): Whether the zip code is valid.

    Logic:
        1. Validate the phone number using validate_phone_number.
        2. Validate the SSN using validate_ssn.
        3. Validate the zip code using validate_zip_code.
        4. Display the validation results for each input.

    Return:
        None
    """

    # Validate each input
    phone_valid = validate_phone_number(phone)
    ssn_valid = validate_ssn(ssn)
    zip_valid = validate_zip_code(zip_code)

    # Display the results
    print("\n--- Validation Results ---")

    # Show phone number result
    if phone_valid:
        print(f"Phone number '{phone}' is VALID.")
    else:
        print(f"Phone number '{phone}' is INVALID.")

    # Show SSN result
    if ssn_valid:
        print(f"Social security number '{ssn}' is VALID.")
    else:
        print(f"Social security number '{ssn}' is INVALID.")

    # Show zip code result
    if zip_valid:
        print(f"Zip code '{zip_code}' is VALID.")
    else:
        print(f"Zip code '{zip_code}' is INVALID.")


def test_validations():
    """
    Tests the validation functions with various valid and invalid inputs.

    Parameters:
        None

    Variables:
        phone_tests (list): A list of tuples containing phone numbers and expected results.
        ssn_tests (list): A list of tuples containing SSNs and expected results.
        zip_tests (list): A list of tuples containing zip codes and expected results.

    Logic:
        1. Define test cases for phone numbers with valid and invalid examples.
        2. Define test cases for SSNs with valid and invalid examples.
        3. Define test cases for zip codes with valid and invalid examples.
        4. Run each test and display the result compared to the expected value.

    Return:
        None
    """

    print("=== Testing Phone Number Validation ===\n")

    # Define phone number test cases with expected results
    phone_tests = [
        ("(555) 123-4567", True),
        ("(555)123-4567", True),
        ("555-123-4567", True),
        ("555.123.4567", True),
        ("555 123 4567", True),
        ("5551234567", True),
        ("555-1234", False),
        ("(555 123-4567", False),
        ("12345678901", False),
        ("abc-def-ghij", False),
    ]

    # Run each phone test
    for phone, expected in phone_tests:
        result = validate_phone_number(phone)
        status = "PASS" if result == expected else "FAIL"
        print(f"  [{status}] '{phone}' -> {result} (expected {expected})")

    print("\n=== Testing SSN Validation ===\n")

    # Define SSN test cases with expected results
    ssn_tests = [
        ("123-45-6789", True),
        ("001-01-0001", True),
        ("000-45-6789", False),
        ("666-45-6789", False),
        ("900-45-6789", False),
        ("123-00-6789", False),
        ("123-45-0000", False),
        ("1234-56-7890", False),
        ("123456789", False),
        ("abc-de-fghi", False),
    ]

    # Run each SSN test
    for ssn, expected in ssn_tests:
        result = validate_ssn(ssn)
        status = "PASS" if result == expected else "FAIL"
        print(f"  [{status}] '{ssn}' -> {result} (expected {expected})")

    print("\n=== Testing Zip Code Validation ===\n")

    # Define zip code test cases with expected results
    zip_tests = [
        ("12345", True),
        ("12345-6789", True),
        ("00501", True),
        ("99999-9999", True),
        ("1234", False),
        ("123456", False),
        ("12345-678", False),
        ("ABCDE", False),
        ("12345-", False),
    ]

    # Run each zip code test
    for zip_code, expected in zip_tests:
        result = validate_zip_code(zip_code)
        status = "PASS" if result == expected else "FAIL"
        print(f"  [{status}] '{zip_code}' -> {result} (expected {expected})")

    print()


def main():
    """
    Main function that runs the validation program.

    Parameters:
        None

    Variables:
        phone (str): The phone number entered by the user.
        ssn (str): The social security number entered by the user.
        zip_code (str): The zip code entered by the user.
        continue_choice (str): The user's choice to continue or exit.

    Logic:
        1. Display a welcome message.
        2. Run the test suite to demonstrate validation with various inputs.
        3. Enter a loop to allow the user to validate their own inputs.
        4. Get user input for phone number, SSN, and zip code.
        5. Display validation results.
        6. Ask if the user wants to validate more inputs.
        7. Exit when the user chooses not to continue.

    Return:
        None
    """

    # Display welcome message
    print("Welcome to the Input Validator Program!")
    print("This program validates phone numbers, social security numbers, and zip codes.\n")

    # Run test cases to show validation works correctly
    print("Running test cases first...\n")
    test_validations()

    # Loop to allow user to validate multiple inputs
    while True:

        # Get input from the user
        print("--- Enter Your Information ---")
        phone, ssn, zip_code = get_user_input()

        # Display validation results
        display_results(phone, ssn, zip_code)

        # Ask if the user wants to continue
        print()
        continue_choice = input("Would you like to validate more inputs? (yes/no): ").strip().lower()

        # Check if user wants to exit
        if continue_choice != "yes":
            print("\nThank you for using the Input Validator Program. Goodbye!")
            break

        print()


# Program entry point
if __name__ == "__main__":
    main()
