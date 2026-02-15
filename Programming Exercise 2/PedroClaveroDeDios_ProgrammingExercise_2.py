def check_spam(message):
    """
    Checks the message for spam keywords and calculates the score.

    Parameters:
        message (str): The email message to check.

    Variables:
        spam_score (int): Accumulator for the spam score.
        found_keywords (list): List to store keywords found in message.
        spam_keywords (list): List of 30 spam words and phrases.

    Logic:
        1. Initialize spam_score to 0 and found_keywords as empty list.
        2. Define list of 30 spam keywords.
        3. Loop through each spam keyword.
        4. Check if the keyword is in the message.
        5. If found, add to score and add keyword to list.
        6. Return the score and the list of found keywords.

    Return:
        tuple: The spam score and list of found keywords.
    """
    spam_score = 0
    found_keywords = []
    spam_keywords = [
        "free money",
        "act now",
        "limited time",
        "cash bonus",
        "make money fast",
        "earn extra cash",
        "get paid",
        "double your",
        "winner",
        "lottery",
        "prize",
        "wire transfer",
        "credit card offer",
        "don't miss out",
        "expires today",
        "once in a lifetime",
        "click here",
        "buy now",
        "order now",
        "call now",
        "sign up for free",
        "subscribe here",
        "apply online",
        "visit our website",
        "urgent",
        "risk-free",
        "guarantee",
        "no obligation",
        "exclusive deal",
        "you have been selected"
    ]

    # Make message lowercase for checking
    message_lower = message.lower()

    for keyword in spam_keywords:
        keyword_lower = keyword.lower()
        if keyword_lower in message_lower:
            spam_score = spam_score + message_lower.count(keyword_lower)
            found_keywords.append(keyword)

    return spam_score, found_keywords


def main():
    """
    Main function to run the spam detector program.

    Parameters:
        None

    Variables:
        email_message (str): The email message from user.
        spam_score (int): The spam score.
        found_keywords (list): List of spam keywords found.
        spam_level (str): The spam level description.

    Logic:
        1. Get email message from user.
        2. Calculate spam score.
        3. Determine spam level based on score.
        4. Display score, level, and found keywords.

    Return:
        None
    """
    # Get email message from user
    email_message = input("Enter your email message: ")

    # Calculate spam score
    spam_score, found_keywords = check_spam(email_message)

    # Determine spam level
    if spam_score <= 2:
        spam_level = "Low likelihood of spam"
    elif spam_score <= 5:
        spam_level = "Moderate likelihood of spam"
    elif spam_score <= 10:
        spam_level = "High likelihood of spam"
    else:
        spam_level = "Very high likelihood of spam"

    # Display results
    print(f"\nSpam Score: {spam_score}")
    print(f"Likelihood: {spam_level}")

    if found_keywords:
        print("\nSpam keywords/phrases found:")
        for keyword in found_keywords:
            print(f"  - {keyword}")
    else:
        print("\nNo spam keywords detected.")


# Program entry point
if __name__ == "__main__":
    main()
