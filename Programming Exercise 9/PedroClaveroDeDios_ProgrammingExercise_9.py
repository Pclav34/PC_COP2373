# PedroClaveroDeDios_ProgrammingExercise_9.py
# This program creates a BankAcct class with methods for deposits,
# withdrawals, interest calculations, and balance display.


class BankAcct:
    """
    A class representing a bank account with name, account number,
    amount, and interest rate.

    Parameters:
        name (str): The account holder's name.
        account_number (str): The account number.
        amount (float): The initial balance.
        interest_rate (float): The annual interest rate as a percentage.

    Variables:
        self.name (str): The account holder's name.
        self.account_number (str): The account number.
        self.amount (float): The current balance.
        self.interest_rate (float): The annual interest rate as a percentage.

    Logic:
        1. Store the name, account number, amount, and interest rate.

    Return:
        None
    """

    def __init__(self, name, account_number, amount, interest_rate):
        """
        Initializes a new BankAcct object.

        Parameters:
            name (str): The account holder's name.
            account_number (str): The account number.
            amount (float): The initial balance.
            interest_rate (float): The annual interest rate as a percentage.

        Variables:
            None

        Logic:
            1. Set the account holder's name.
            2. Set the account number.
            3. Set the initial balance.
            4. Set the annual interest rate.

        Return:
            None
        """

        # Set account holder's name
        self.name = name

        # Set account number
        self.account_number = account_number

        # Set initial balance
        self.amount = amount

        # Set annual interest rate as a percentage
        self.interest_rate = interest_rate

    def adjust_interest_rate(self, new_rate):
        """
        Adjusts the interest rate on the account.

        Parameters:
            new_rate (float): The new annual interest rate as a percentage.

        Variables:
            old_rate (float): The previous interest rate for display.

        Logic:
            1. Store the old rate for display.
            2. Set the interest rate to the new value.
            3. Print confirmation of the change.

        Return:
            None
        """

        # Store old rate for confirmation message
        old_rate = self.interest_rate

        # Update interest rate
        self.interest_rate = new_rate

        # Display confirmation
        print(f"Interest rate adjusted from {old_rate:.2f}% to {self.interest_rate:.2f}%.")

    def deposit(self, deposit_amount):
        """
        Deposits money into the account.

        Parameters:
            deposit_amount (float): The amount to deposit.

        Variables:
            None

        Logic:
            1. Check if the deposit amount is positive.
            2. Add the deposit amount to the balance.
            3. Print confirmation of the deposit.

        Return:
            None
        """

        # Check for valid deposit amount
        if deposit_amount <= 0:
            print("Deposit amount must be positive.")
            return

        # Add deposit to balance
        self.amount += deposit_amount

        # Display confirmation
        print(f"Deposited ${deposit_amount:,.2f}. New balance: ${self.amount:,.2f}")

    def withdraw(self, withdraw_amount):
        """
        Withdraws money from the account.

        Parameters:
            withdraw_amount (float): The amount to withdraw.

        Variables:
            None

        Logic:
            1. Check if the withdrawal amount is positive.
            2. Check if there are sufficient funds.
            3. Subtract the withdrawal amount from the balance.
            4. Print confirmation of the withdrawal.

        Return:
            None
        """

        # Check for valid withdrawal amount
        if withdraw_amount <= 0:
            print("Withdrawal amount must be positive.")
            return

        # Check for sufficient funds
        if withdraw_amount > self.amount:
            print(f"Insufficient funds. Current balance: ${self.amount:,.2f}")
            return

        # Subtract withdrawal from balance
        self.amount -= withdraw_amount

        # Display confirmation
        print(f"Withdrew ${withdraw_amount:,.2f}. New balance: ${self.amount:,.2f}")

    def get_balance(self):
        """
        Returns the current account balance.

        Parameters:
            None

        Variables:
            None

        Logic:
            1. Return the current balance.

        Return:
            float: The current account balance.
        """

        return self.amount

    def calculate_interest(self, days):
        """
        Calculates interest earned based on the number of days.

        Parameters:
            days (int): The number of days to calculate interest for.

        Variables:
            daily_rate (float): The daily interest rate.
            interest (float): The calculated interest amount.

        Logic:
            1. Convert annual interest rate to a daily rate.
            2. Multiply the daily rate by the balance and the number of days.
            3. Print the interest earned.
            4. Return the interest amount.

        Return:
            float: The interest earned for the given number of days.
        """

        # Convert annual percentage rate to daily rate
        daily_rate = (self.interest_rate / 100) / 365

        # Calculate interest for the given number of days
        interest = self.amount * daily_rate * days

        # Display interest earned
        print(f"Interest earned over {days} days: ${interest:,.2f}")

        return interest

    def __str__(self):
        """
        Returns a string representation of the account with balance and interest info.

        Parameters:
            None

        Variables:
            None

        Logic:
            1. Format and return account details including name, account number,
               balance, and interest rate.

        Return:
            str: A formatted string displaying the account information.
        """

        return (
            f"Account Holder: {self.name}\n"
            f"Account Number: {self.account_number}\n"
            f"Balance: ${self.amount:,.2f}\n"
            f"Interest Rate: {self.interest_rate:.2f}%"
        )


def test_bank_acct():
    """
    Tests the BankAcct class methods with sample data.

    Parameters:
        None

    Variables:
        account (BankAcct): A test bank account object.
        balance (float): The current balance retrieved from the account.
        interest (float): The interest calculated for a period.

    Logic:
        1. Create a BankAcct object with test data.
        2. Display the initial account information.
        3. Test the deposit method.
        4. Test the withdraw method.
        5. Test withdrawing more than the balance.
        6. Test the get_balance method.
        7. Test the calculate_interest method.
        8. Test the adjust_interest_rate method.
        9. Test calculate_interest with the new rate.
        10. Display the final account information.

    Return:
        None
    """

    # Create a test account
    print("=== Creating Bank Account ===\n")
    account = BankAcct("John Smith", "1234567890", 1000.00, 3.5)

    # Display initial account info using __str__
    print(account)

    # Test deposit
    print("\n=== Testing Deposit ===\n")
    account.deposit(500.00)
    account.deposit(250.75)

    # Test withdraw
    print("\n=== Testing Withdrawal ===\n")
    account.withdraw(200.00)

    # Test withdrawal with insufficient funds
    print("\n=== Testing Insufficient Funds ===\n")
    account.withdraw(5000.00)

    # Test get_balance
    print("\n=== Testing Get Balance ===\n")
    balance = account.get_balance()
    print(f"Current balance: ${balance:,.2f}")

    # Test calculate_interest for 30 days
    print("\n=== Testing Interest Calculation (30 days) ===\n")
    interest = account.calculate_interest(30)

    # Test calculate_interest for 365 days
    print("\n=== Testing Interest Calculation (365 days) ===\n")
    interest = account.calculate_interest(365)

    # Test adjust_interest_rate
    print("\n=== Testing Interest Rate Adjustment ===\n")
    account.adjust_interest_rate(4.25)

    # Test calculate_interest with new rate for 90 days
    print("\n=== Testing Interest Calculation with New Rate (90 days) ===\n")
    interest = account.calculate_interest(90)

    # Display final account info using __str__
    print("\n=== Final Account Information ===\n")
    print(account)


# Program entry point
if __name__ == "__main__":
    test_bank_acct()
