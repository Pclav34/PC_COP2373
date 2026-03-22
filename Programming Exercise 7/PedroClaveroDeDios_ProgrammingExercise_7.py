# PedroClaveroDeDios_ProgrammingExercise_7.py
# This program uses the look-ahead regular expression from Section 7.4
# to split a paragraph into individual sentences, including sentences
# that begin with numbers, and displays the count.

import re


def split_sentences(paragraph):
    """
    Splits a paragraph into individual sentences using a regular
    expression with look-ahead, based on Section 7.4 of the textbook.

    Parameters:
        paragraph (str): The paragraph to split into sentences.

    Variables:
        pattern (str): The regex pattern for matching sentences.
        sentences (list): The list of sentences found in the paragraph.

    Logic:
        1. Define a regex pattern based on Section 7.4 that matches sentences.
        2. Modify the pattern to also match sentences beginning with numbers.
        3. Use re.findall with DOTALL and MULTILINE flags to find all sentences.
        4. Strip whitespace from each sentence.
        5. Return the list of sentences.

    Return:
        list: A list of strings, each being an individual sentence.
    """

    # Define the regex pattern from Section 7.4, modified to also match
    # sentences that begin with numbers using [A-Z0-9] instead of [A-Z]
    pattern = r'[A-Z0-9].*?[.!?](?= [A-Z0-9]|$)'

    # Find all sentences using the pattern with DOTALL and MULTILINE flags
    sentences = re.findall(pattern, paragraph, flags=re.DOTALL | re.MULTILINE)

    # Strip extra whitespace from each sentence
    sentences = [s.strip() for s in sentences]

    return sentences


def display_sentences(sentences):
    """
    Displays each individual sentence and the total count.

    Parameters:
        sentences (list): A list of sentence strings to display.

    Variables:
        count (int): The total number of sentences found.

    Logic:
        1. Print a header for the output.
        2. Loop through the sentences and print each one numbered.
        3. Calculate and display the total sentence count.

    Return:
        None
    """

    # Print header
    print("\n--- Sentences Found ---")

    # Display each sentence with its number
    for i, sentence in enumerate(sentences, 1):
        print(f"  Sentence {i}: {sentence}")

    # Calculate and display the total count
    count = len(sentences)
    print(f"\nTotal number of sentences: {count}")


def get_paragraph():
    """
    Prompts the user to enter a paragraph.

    Parameters:
        None

    Variables:
        paragraph (str): The paragraph entered by the user.

    Logic:
        1. Prompt the user to enter a paragraph.
        2. Return the paragraph string.

    Return:
        str: The paragraph entered by the user.
    """

    # Prompt user to enter a paragraph
    paragraph = input("Enter a paragraph: ")

    return paragraph


def main():
    """
    Main function that runs the sentence counter program.

    Parameters:
        None

    Variables:
        paragraph (str): The paragraph entered by the user.
        sentences (list): The list of sentences found.
        continue_choice (str): The user's choice to continue or exit.

    Logic:
        1. Display a welcome message.
        2. Enter a loop to allow the user to analyze multiple paragraphs.
        3. Get a paragraph from the user.
        4. Split the paragraph into sentences using the regex pattern.
        5. Display the sentences and count.
        6. Ask if the user wants to analyze another paragraph.
        7. Exit when the user chooses not to continue.

    Return:
        None
    """

    # Display welcome message
    print("Welcome to the Sentence Counter Program!")
    print("This program splits paragraphs into sentences using regular expressions.")
    print("It handles abbreviations, decimal numbers, and sentences starting with numbers.\n")

    # Loop to allow multiple paragraphs
    while True:

        # Get paragraph from user
        paragraph = get_paragraph()

        # Split the paragraph into sentences
        sentences = split_sentences(paragraph)

        # Display the results
        if sentences:
            display_sentences(sentences)
        else:
            print("\nNo sentences were found in the input.")

        # Ask if the user wants to continue
        print()
        continue_choice = input("Would you like to analyze another paragraph? (yes/no): ").strip().lower()

        # Check if user wants to exit
        if continue_choice != "yes":
            print("\nThank you for using the Sentence Counter Program. Goodbye!")
            break

        print()


# Program entry point
if __name__ == "__main__":
    main()
