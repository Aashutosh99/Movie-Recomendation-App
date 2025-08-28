import datetime as datetime
import requests
import random
import os
from movie_data import language_mapping

# Fetch API key from environment variable
API_KEY = os.environ.get("TMDB_API_KEY")
TMDB_URL = "https://api.themoviedb.org/3/discover/movie"


# Function to display movie details
def display_movie(movie):
    # Display the recommended movie in a formatted way
    print("\n--- Recommended Movie ---")
    print(f"Title: {movie['title']}")
    print(f"Overview: {movie['overview']}")
    print(f"Ratings: {movie['ratings']}")
    print(f"Original Language: {movie['original_language']}\n")


# Class to find and recommend movies
class MovieFinder:
    def __init__(self, genre, date=None):
        self.genre = genre

        # If date is not provided, use the current year
        if date is None:
            date = datetime.datetime.today().year
        self.date = datetime.datetime(year=date, month=1, day=1)
        self.release_date_from = f"{self.date.year}-01-01"
        self.release_date_to = f"{self.date.year}-12-31"
        self.movies_list = []

        # Start movie recommendation process
        self.display_random_movie()

    def fetch_movie_data(self):
        # Define the parameters for the API request
        parameters = {
            "api_key": API_KEY,
            "include_adult": "false",
            "include_video": "false",
            "language": "en-US",
            "page": 1,
            "primary_release_year": self.date.year,
            "primary_release_date.gte": self.release_date_from,
            "primary_release_date.lte": self.release_date_to,
            "sort_by": "vote_average.desc",
            "vote_count.gte": 100,
            "with_genres": self.genre
        }

        try:
            # Make a GET request to the TMDB API
            response = requests.get(url=TMDB_URL, params=parameters)
            response.raise_for_status()  # Raise HTTPError if the request fails
            movie_data = response.json()

            # Extract movie details and add them to the movies list
            for result in movie_data.get("results", []):
                title = result.get("title", "Unknown Title")
                overview = result.get("overview", "No overview available.")
                ratings = result.get("vote_average", "N/A")
                original_language = result.get("original_language", "en")
                language = language_mapping.get(original_language, "Unknown")

                self.movies_list.append({
                    "title": title,
                    "overview": overview,
                    "ratings": ratings,
                    "original_language": language
                })

        except requests.exceptions.RequestException as e:
            print(f"An error occurred while fetching movie data: {e}")

    def display_random_movie(self):
        # Fetch movie data if the list is empty
        if not self.movies_list:
            self.fetch_movie_data()

        # Display a random movie from the list if available
        if self.movies_list:
            recommended_movie = random.choice(self.movies_list)
            display_movie(recommended_movie)
        else:
            print("No movies to recommend. Please try a different genre or year.")
