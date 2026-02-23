from functools import reduce


def get_expenses():
    """
    Asks the user for their monthly expenses.

    Parameters:
        None

    Variables:
        expenses (list): List of dictionaries with expense type and amount.
        expense_type (str): The type of expense entered by the user.
        amount (float): The amount of the expense.

    Logic:
        1. Initialize expenses as an empty list.
        2. Loop to ask user for expense type and amount.
        3. If user types 'done', stop collecting expenses.
        4. Convert amount to float and append to list.
        5. Return the list of expenses.

    Return:
        list: A list of dictionaries with 'type' and 'amount' keys.
    """
    expenses = []

    print("Enter your monthly expenses.")
    print("Type 'done' when you are finished.\n")

    while True:
        # Ask for the type of expense
        expense_type = input("Enter expense type (or 'done' to finish): ")

        if expense_type.lower() == "done":
            break

        # Ask for the amount of the expense
        try:
            amount = float(input(f"Enter amount for {expense_type}: $"))
        except ValueError:
            print("Invalid amount. Please enter a number.\n")
            continue

        # Add expense to the list
        expenses.append({"type": expense_type, "amount": amount})
        print()

    return expenses


def analyze_expenses(expenses):
    """
    Uses reduce to calculate total, highest, and lowest expenses.

    Parameters:
        expenses (list): List of expense dictionaries.

    Variables:
        total (float): The total of all expenses.
        highest (dict): The expense with the highest amount.
        lowest (dict): The expense with the lowest amount.

    Logic:
        1. Use reduce with a lambda to sum all expense amounts for total.
        2. Use reduce with a lambda to find the expense with the highest amount.
        3. Use reduce with a lambda to find the expense with the lowest amount.
        4. Return total, highest, and lowest.

    Return:
        tuple: The total expense, highest expense dict, and lowest expense dict.
    """
    # Calculate total expense using reduce
    total = reduce(lambda acc, exp: acc + exp["amount"], expenses, 0)

    # Find the highest expense using reduce
    highest = reduce(lambda a, b: a if a["amount"] >= b["amount"] else b, expenses)

    # Find the lowest expense using reduce
    lowest = reduce(lambda a, b: a if a["amount"] <= b["amount"] else b, expenses)

    return total, highest, lowest


def display_results(total, highest, lowest):
    """
    Displays the total, highest, and lowest expenses.

    Parameters:
        total (float): The total of all expenses.
        highest (dict): The expense with the highest amount.
        lowest (dict): The expense with the lowest amount.

    Variables:
        None

    Logic:
        1. Print the total expense amount.
        2. Print the highest expense type and amount.
        3. Print the lowest expense type and amount.

    Return:
        None
    """
    print("\n--- Expense Analysis ---")
    print(f"Total Expenses: ${total:.2f}")
    print(f"Highest Expense: {highest['type']} at ${highest['amount']:.2f}")
    print(f"Lowest Expense: {lowest['type']} at ${lowest['amount']:.2f}")


def main():
    """
    Main function to run the expense analyzer program.

    Parameters:
        None

    Variables:
        expenses (list): List of expense dictionaries from user.
        total (float): The total of all expenses.
        highest (dict): The highest expense.
        lowest (dict): The lowest expense.

    Logic:
        1. Get expenses from the user.
        2. Check if any expenses were entered.
        3. Analyze expenses using reduce.
        4. Display the results.

    Return:
        None
    """
    # Get expenses from the user
    expenses = get_expenses()

    # Check if user entered any expenses
    if not expenses:
        print("\nNo expenses were entered.")
        return

    # Analyze expenses using reduce
    total, highest, lowest = analyze_expenses(expenses)

    # Display the results
    display_results(total, highest, lowest)


# Program entry point
if __name__ == "__main__":
    main()
