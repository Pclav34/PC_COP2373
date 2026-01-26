def sell_tickets(tickets_remaining):
    """
    Prompts the user to purchase tickets and validates the purchase.

    Parameters:
        tickets_remaining (int): The number of tickets still available for sale.

    Variables:
        tickets_requested (int): The number of tickets the user wants to purchase.

    Logic:
        1. Prompt the user for the number of tickets they want to buy.
        2. Convert the input to an integer.
        3. Validate that the requested tickets are between 1 and 4.
        4. Validate that enough tickets remain for the purchase.
        5. Return the number of tickets purchased if valid, or 0 if invalid.

    Return:
        int: The number of tickets successfully purchased (0 if invalid).
    """
    # Prompt user for number of tickets
    tickets_requested = int(input("How many tickets would you like to purchase? "))

    # Check if request is within allowed range (1-4 tickets)
    if tickets_requested < 1 or tickets_requested > 4:
        print("Error: You can only purchase between 1 and 4 tickets.")
        return 0

    # Check if enough tickets remain
    if tickets_requested > tickets_remaining:
        print(f"Error: Only {tickets_remaining} ticket(s) remaining. Please request fewer tickets.")
        return 0

    # Valid purchase
    return tickets_requested


def main():
    """
    Main function to manage the cinema ticket pre-sale process.

    Parameters:
        None

    Variables:
        TOTAL_TICKETS (int): Constant representing the total tickets available.
        tickets_remaining (int): Accumulator tracking remaining tickets.
        total_buyers (int): Accumulator tracking the total number of buyers.
        tickets_sold (int): Number of tickets sold in current transaction.

    Logic:
        1. Initialize total tickets to 20 and total buyers to 0.
        2. Display welcome message.
        3. Loop while tickets remain available.
        4. Call sell_tickets function to process a purchase.
        5. If purchase is valid, update remaining tickets and buyer count.
        6. Display remaining tickets after each purchase.
        7. When all tickets are sold, display total number of buyers.

    Return:
        None
    """
    # Initialize constants and accumulators
    TOTAL_TICKETS = 20
    tickets_remaining = TOTAL_TICKETS
    total_buyers = 0

    # Display welcome message
    print("Welcome to the Cinema Ticket Pre-Sale!")
    print(f"We have {TOTAL_TICKETS} tickets available.")
    print("Each buyer can purchase up to 4 tickets.\n")

    # Loop until all tickets are sold
    while tickets_remaining > 0:
        # Attempt to sell tickets
        tickets_sold = sell_tickets(tickets_remaining)

        # Check if the sale was successful
        if tickets_sold > 0:
            # Update remaining tickets
            tickets_remaining -= tickets_sold

            # Increment buyer count
            total_buyers += 1

            # Display remaining tickets
            print(f"Purchase successful! {tickets_remaining} ticket(s) remaining.\n")

    # Display final message when all tickets are sold
    print("All tickets have been sold!")
    print(f"Total number of buyers: {total_buyers}")


# Program entry point
if __name__ == "__main__":
    main()
