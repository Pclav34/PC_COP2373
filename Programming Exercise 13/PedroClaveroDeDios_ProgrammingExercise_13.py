# PedroClaveroDeDios_ProgrammingExercise_13.py
# This program creates a population database for 10 Florida cities,
# simulates 20 years of population growth and decline, and displays
# a matplotlib chart for a city selected by the user.

import sqlite3
import matplotlib.pyplot as plt


def create_population_database(database_name):
    """
    Creates the population database and population table.

    Parameters:
        database_name (str): The name of the SQLite database file.

    Variables:
        connection (sqlite3.Connection): The connection to the database.
        cursor (sqlite3.Cursor): The cursor used to execute SQL statements.

    Logic:
        1. Connect to the SQLite database file.
        2. Drop the population table if it already exists.
        3. Create a new population table with city, year, and population fields.
        4. Commit the changes.
        5. Return the database connection.

    Return:
        sqlite3.Connection: The open connection to the database.
    """

    # Connect to the SQLite database file
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()

    # Drop the table so the program starts with fresh data each time
    cursor.execute("DROP TABLE IF EXISTS population")

    # Create the population table
    cursor.execute(
        """
        CREATE TABLE population (
            city TEXT NOT NULL,
            year INTEGER NOT NULL,
            population INTEGER NOT NULL
        )
        """
    )

    # Save the table creation
    connection.commit()

    return connection


def insert_initial_population_data(connection):
    """
    Inserts the starting 2025 population data for 10 Florida cities.

    Parameters:
        connection (sqlite3.Connection): The connection to the database.

    Variables:
        cursor (sqlite3.Cursor): The cursor used to execute SQL statements.
        city_data (list): A list of tuples containing city names and 2025 populations.

    Logic:
        1. Define 10 Florida cities and their 2025 populations.
        2. Insert each city into the population table with the year 2025.
        3. Commit the changes to the database.
        4. Return the list of city data.

    Return:
        list: A list of tuples containing each city and its starting population.
    """

    # Create a cursor for database work
    cursor = connection.cursor()

    # Define the initial city data for 2025
    city_data = [
        ("Jacksonville", 1000000),
        ("Miami", 460000),
        ("Tampa", 410000),
        ("Orlando", 325000),
        ("St. Petersburg", 268000),
        ("Hialeah", 221000),
        ("Tallahassee", 204000),
        ("Fort Lauderdale", 185000),
        ("Port St. Lucie", 243000),
        ("Cape Coral", 236000)
    ]

    # Insert the starting data into the population table
    for city, population in city_data:
        cursor.execute(
            "INSERT INTO population (city, year, population) VALUES (?, ?, ?)",
            (city, 2025, population)
        )

    # Save the inserted data
    connection.commit()

    return city_data


def simulate_population_changes(connection, city_data, start_year=2025):
    """
    Simulates 20 years of population growth and decline for each city.

    Parameters:
        connection (sqlite3.Connection): The connection to the database.
        city_data (list): A list of tuples containing city names and starting populations.
        start_year (int): The starting year for the original population data.

    Variables:
        cursor (sqlite3.Cursor): The cursor used to execute SQL statements.
        annual_rates (list): A list of growth and decline rates for the 20 years.
        city (str): The current city being processed.
        starting_population (int): The 2025 population for the city.
        current_population (int): The running population total for the city.
        year_offset (int): The number of years after the start year.
        rate (float): The growth or decline rate for the current year.
        projected_population (int): The simulated population for the new year.

    Logic:
        1. Create a list of 20 annual rates that includes both growth and decline.
        2. Loop through each city and starting population.
        3. Apply each annual rate to the most recent population.
        4. Insert each projected year and population into the database.
        5. Commit the completed simulation data.

    Return:
        None
    """

    # Create a cursor for database work
    cursor = connection.cursor()

    # Define annual growth and decline rates for the next 20 years
    annual_rates = [
        0.018, 0.012, -0.004, 0.021, 0.009,
        -0.007, 0.015, 0.011, -0.003, 0.019,
        0.008, -0.006, 0.014, 0.010, -0.002,
        0.017, 0.007, -0.005, 0.013, 0.006
    ]

    # Process each city one at a time
    for city, starting_population in city_data:

        # Begin the simulation with the 2025 population
        current_population = starting_population

        # Apply each year's rate and store the result
        for year_offset, rate in enumerate(annual_rates, start=1):

            # Calculate the next year's population
            projected_population = round(current_population * (1 + rate))

            # Insert the projected population for the year
            cursor.execute(
                "INSERT INTO population (city, year, population) VALUES (?, ?, ?)",
                (city, start_year + year_offset, projected_population)
            )

            # Update the running population for the next loop
            current_population = projected_population

    # Save all projected population data
    connection.commit()


def get_city_selection(cities):
    """
    Prompts the user to choose one of the available cities.

    Parameters:
        cities (list): A list of city names available in the database.

    Variables:
        index (int): The display number for each city.
        choice (str): The raw input entered by the user.
        choice_number (int): The validated numeric choice entered by the user.

    Logic:
        1. Display each city as a numbered option.
        2. Prompt the user to enter a city number.
        3. Validate that the input is numeric and within range.
        4. Return the selected city name.

    Return:
        str: The city chosen by the user.
    """

    # Display the available city options
    print("\n=== Available Florida Cities ===\n")
    for index, city in enumerate(cities, start=1):
        print(f"  {index}. {city}")

    # Continue prompting until the user enters a valid selection
    while True:

        # Get the user's city choice
        choice = input("\nEnter the number of the city you would like to view: ").strip()

        # Validate that the input is numeric
        if not choice.isdigit():
            print("Invalid input. Please enter a number from the list.")
            continue

        choice_number = int(choice)

        # Validate that the number is within the list range
        if choice_number < 1 or choice_number > len(cities):
            print("Invalid city number. Please choose a number from the list.")
            continue

        return cities[choice_number - 1]


def plot_city_population(connection, city_name):
    """
    Retrieves population data for a city and creates a matplotlib chart.

    Parameters:
        connection (sqlite3.Connection): The connection to the database.
        city_name (str): The city chosen by the user.

    Variables:
        cursor (sqlite3.Cursor): The cursor used to execute SQL statements.
        rows (list): The list of database rows for the selected city.
        years (list): The list of years for the selected city.
        populations (list): The list of populations for the selected city.

    Logic:
        1. Query the population table for the selected city.
        2. Separate the years and populations into lists.
        3. Create a line chart using matplotlib.
        4. Display the chart to the user.

    Return:
        None
    """

    # Create a cursor for database work
    cursor = connection.cursor()

    # Retrieve the city's population history
    cursor.execute(
        "SELECT year, population FROM population WHERE city = ? ORDER BY year",
        (city_name,)
    )
    rows = cursor.fetchall()

    # Separate the query results into x and y values
    years = [row[0] for row in rows]
    populations = [row[1] for row in rows]

    # Create the population chart
    plt.figure(figsize=(10, 6))
    plt.plot(years, populations, marker="o", linewidth=2, color="green")
    plt.title(f"Population Growth and Decline for {city_name}")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.grid(True)
    plt.tight_layout()

    # Display the chart to the user
    plt.show()


def main():
    """
    Main function that runs the population database and chart program.

    Parameters:
        None

    Variables:
        database_name (str): The name of the database file.
        connection (sqlite3.Connection): The connection to the database.
        city_data (list): The list of starting city population data.
        cities (list): The list of city names available to the user.
        selected_city (str): The city chosen by the user.

    Logic:
        1. Display a welcome message.
        2. Create the population database and table.
        3. Insert the starting 2025 population data for 10 Florida cities.
        4. Simulate 20 years of population growth and decline.
        5. Display the list of cities and get the user's choice.
        6. Display a population chart for the selected city.
        7. Close the database connection.

    Return:
        None
    """

    # Display welcome message
    print("Welcome to the Florida Population Growth and Decline Program!")
    print("This program creates a population database and charts one selected city.\n")

    # Define the database filename using the student's initials
    database_name = "population_PCD.db"

    # Create the database and population table
    connection = create_population_database(database_name)

    # Insert the initial 2025 city population data
    city_data = insert_initial_population_data(connection)

    # Simulate the next 20 years of population changes
    simulate_population_changes(connection, city_data, start_year=2025)

    # Confirm that the database is ready
    print(f"Database '{database_name}' created successfully.")
    print("Population data for 2025 through 2045 has been stored in the population table.")

    # Build a list of city names for the menu
    cities = [city for city, population in city_data]

    # Let the user choose a city to graph
    selected_city = get_city_selection(cities)

    # Display the population chart for the selected city
    print(f"\nDisplaying the population chart for {selected_city}...")
    plot_city_population(connection, selected_city)

    # Close the database connection
    connection.close()

    # Display completion message
    print("\nThank you for using the Florida Population Program. Goodbye!")


# Program entry point
if __name__ == "__main__":
    main()
