import datetime as datetime
from movie_finder import MovieFinder
from movie_data import genres


# Function to display all available genres to the user
def display_available_genres():
    print("Available genres:")
    for genre in genres.values():
        print(genre, end=", ")
    print("\n")


# Function to get the genre ID based on user input
def get_genre_id():
    # Show the available genres before taking input
    display_available_genres()
    while True:
        # Ask the user to input a genre type
        movie_genre = input("What type of movie do you want to watch?\n").strip().lower()
        # Check if the input matches any genre in the dictionary (case-insensitive)
        genre = next((key for key, val in genres.items() if movie_genre == val.lower()), None)
        # If a valid genre is found, return its ID
        if genre:
            return genre
        else:
            print("Invalid genre. Please choose from the available genres.")


# Function to get a valid movie release year from the user
def get_movie_release_year():
    current_year = datetime.datetime.today().year  # Get the current year
    while True:
        try:
            # Ask the user to input a release year
            release_year = int(input("Enter the movie release year: "))
            # Check if the input year is within a valid range
            if 1900 <= release_year <= current_year:
                return release_year
            else:
                print(f"Please input a valid year from 1900 to {current_year}.")
        except ValueError:
            print("Please enter a numeric year value.")


# Main function to handle the program logic
def main():
    print("Welcome to the Movie Recommendation App!")  # Greet the user
    genre_id = get_genre_id()  # Get genre ID from user input
    movie_release_year = get_movie_release_year()  # Get release year from user input

    while True:
        # Call the FindMovies class to recommend a movie
        MovieFinder(genre_id, movie_release_year)
        # Ask the user if they want another recommendation
        ask_user = input("Enter 'Y' to recommend another movie or any other key to exit the program: ").lower()
        if ask_user != 'y':
            print("Thank you for using the Movie Recommendation App!")  # Exit message
            break


# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()
