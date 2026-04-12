# PedroClaveroDeDios_ProgrammingExercise_11.py
# This program implements a 5-card draw Poker game using a Deck class
# based on Section 11.5. It deals a hand, allows the user to draw
# replacement cards, and displays the final hand.

import random


class Deck:
    """
    A class representing a standard 52-card deck of playing cards,
    based on Section 11.5 of the textbook.

    Parameters:
        None

    Variables:
        self.cards (list): A list of tuples representing the cards in the deck.
        self.ranks (list): The list of card rank names.
        self.suits (list): The list of card suit names.

    Logic:
        1. Define the ranks and suits for a standard deck.
        2. Build the deck as a list of (rank, suit) tuples.
        3. Shuffle the deck.

    Return:
        None
    """

    def __init__(self):
        """
        Initializes a new Deck object with 52 shuffled cards.

        Parameters:
            None

        Variables:
            self.ranks (list): The list of card rank names from 2 to Ace.
            self.suits (list): The list of four card suit names.
            self.cards (list): The full list of 52 (rank, suit) tuples.

        Logic:
            1. Define the 13 ranks from 2 through Ace.
            2. Define the 4 suits.
            3. Build the deck using a list comprehension.
            4. Shuffle the deck.

        Return:
            None
        """

        # Define the 13 ranks
        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9',
                      '10', 'Jack', 'Queen', 'King', 'Ace']

        # Define the 4 suits
        self.suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

        # Build the full deck of 52 cards as (rank, suit) tuples
        self.cards = [(rank, suit) for suit in self.suits
                      for rank in self.ranks]

        # Shuffle the deck
        random.shuffle(self.cards)

    def deal(self, num_cards):
        """
        Deals a specified number of cards from the top of the deck.

        Parameters:
            num_cards (int): The number of cards to deal.

        Variables:
            dealt (list): The list of cards dealt from the deck.

        Logic:
            1. Check if there are enough cards remaining in the deck.
            2. Take the specified number of cards from the top of the deck.
            3. Remove those cards from the deck.
            4. Return the dealt cards.

        Return:
            list: A list of (rank, suit) tuples representing the dealt cards.
        """

        # Check if enough cards remain
        if num_cards > len(self.cards):
            print("Not enough cards remaining in the deck.")
            return []

        # Take cards from the top of the deck
        dealt = self.cards[:num_cards]

        # Remove dealt cards from the deck
        self.cards = self.cards[num_cards:]

        return dealt

    def __len__(self):
        """
        Returns the number of cards remaining in the deck.

        Parameters:
            None

        Variables:
            None

        Logic:
            1. Return the length of the cards list.

        Return:
            int: The number of cards remaining in the deck.
        """

        return len(self.cards)


def format_card(card):
    """
    Formats a single card tuple into a readable string.

    Parameters:
        card (tuple): A (rank, suit) tuple representing a card.

    Variables:
        rank (str): The rank of the card.
        suit (str): The suit of the card.

    Logic:
        1. Unpack the rank and suit from the tuple.
        2. Return a formatted string showing the rank and suit.

    Return:
        str: A formatted string like "Ace of Spades".
    """

    # Unpack the card tuple
    rank, suit = card

    return f"{rank} of {suit}"


def display_hand(hand):
    """
    Displays the current hand of cards with numbered positions.

    Parameters:
        hand (list): A list of (rank, suit) tuples representing the hand.

    Variables:
        None

    Logic:
        1. Loop through the hand and print each card with its position number.

    Return:
        None
    """

    # Display each card with its position number
    for i, card in enumerate(hand, 1):
        print(f"  Card {i}: {format_card(card)}")


def get_cards_to_replace():
    """
    Prompts the user to enter which card positions to replace.

    Parameters:
        None

    Variables:
        user_input (str): The raw input string from the user.
        positions (list): The list of card position numbers to replace.

    Logic:
        1. Prompt the user to enter card numbers separated by commas.
        2. If the input is empty, return an empty list (keep all cards).
        3. Parse the input into a list of integers.
        4. Validate that each position is between 1 and 5.
        5. Return the list of valid positions.

    Return:
        list: A list of integers representing card positions to replace (1-5).
    """

    # Prompt the user for card positions to replace
    user_input = input("\nEnter card numbers to replace (e.g., 1, 3, 5) or press Enter to keep all: ")

    # If input is empty, keep all cards
    if user_input.strip() == "":
        return []

    # Parse the input into a list of integers
    try:
        positions = [int(x.strip()) for x in user_input.split(",")]
    except ValueError:
        print("Invalid input. Please enter numbers separated by commas.")
        return get_cards_to_replace()

    # Validate that each position is between 1 and 5
    for pos in positions:
        if pos < 1 or pos > 5:
            print(f"Invalid card number: {pos}. Must be between 1 and 5.")
            return get_cards_to_replace()

    return positions


def draw_replacement_cards(deck, hand, positions):
    """
    Replaces selected cards in the hand with new cards from the deck.

    Parameters:
        deck (Deck): The Deck object to draw replacement cards from.
        hand (list): The current hand of (rank, suit) tuples.
        positions (list): The list of card positions to replace (1-indexed).

    Variables:
        new_cards (list): The list of new cards drawn from the deck.

    Logic:
        1. Deal the same number of new cards as positions to replace.
        2. Replace each selected card in the hand with a new card.
        3. Return the updated hand.

    Return:
        list: The updated hand with replacement cards.
    """

    # Deal new cards from the deck
    new_cards = deck.deal(len(positions))

    # Replace each selected card with a new card
    for i, pos in enumerate(positions):
        hand[pos - 1] = new_cards[i]

    return hand


def play_poker_hand(deck):
    """
    Plays one round of 5-card draw poker.

    Parameters:
        deck (Deck): The Deck object to deal from.

    Variables:
        hand (list): The player's hand of 5 cards.
        positions (list): The card positions selected for replacement.

    Logic:
        1. Deal a hand of 5 cards from the deck.
        2. Display the initial hand to the player.
        3. Prompt the player to select cards to replace.
        4. If the player selected cards, draw replacements and show the new hand.
        5. If the player kept all cards, confirm the choice.

    Return:
        None
    """

    # Deal a hand of 5 cards
    print("\n=== Dealing Your Hand ===\n")
    hand = deck.deal(5)

    # Display the initial hand
    print("Your hand:")
    display_hand(hand)

    # Prompt the player for cards to replace
    print("\n=== Draw Phase ===")
    positions = get_cards_to_replace()

    # Check if the player wants to replace any cards
    if positions:

        # Show which cards are being replaced
        print(f"\nReplacing card(s): {', '.join(str(p) for p in positions)}")

        # Draw replacement cards
        hand = draw_replacement_cards(deck, hand, positions)

        # Display the updated hand
        print("\n=== Your New Hand ===\n")
        print("Your hand after drawing:")
        display_hand(hand)

    else:

        # Player chose to keep all cards
        print("\nYou chose to keep all your cards.")
        print("\n=== Your Final Hand ===\n")
        print("Your hand:")
        display_hand(hand)


def main():
    """
    Main function that runs the 5-card draw Poker program.

    Parameters:
        None

    Variables:
        deck (Deck): The Deck object used for the game.
        continue_choice (str): The user's choice to play again or exit.

    Logic:
        1. Display a welcome message.
        2. Enter a loop to allow the user to play multiple rounds.
        3. Create a new shuffled Deck for each round.
        4. Play a round of poker.
        5. Ask if the user wants to play again.
        6. Exit when the user chooses not to continue.

    Return:
        None
    """

    # Display welcome message
    print("Welcome to 5-Card Draw Poker!")
    print("You will be dealt 5 cards, then choose which to replace.")

    # Loop to allow multiple rounds
    while True:

        # Create a new shuffled deck for each round
        deck = Deck()

        # Play a round of poker
        play_poker_hand(deck)

        # Ask if the user wants to play again
        print()
        continue_choice = input("Would you like to play another hand? (yes/no): ").strip().lower()

        # Check if user wants to exit
        if continue_choice != "yes":
            print("\nThank you for playing 5-Card Draw Poker. Goodbye!")
            break

        print()


# Program entry point
if __name__ == "__main__":
    main()
