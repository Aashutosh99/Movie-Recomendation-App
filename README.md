# Movie Recommendation App

This is a simple Python application that recommends movies based on your chosen genre and release year using the TMDB API.

## Features
- Choose a movie genre from a list.
- Input a movie release year.
- Get a random movie recommendation with details like title, overview, ratings, and language.

## Requirements
- Python 3.x
- `requests` library

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Aashutosh99/Movie-Recomendation-App.git
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your API key:**
   - Create a `.env` file (optional) or set the API key directly in the code.
   - Add your TMDB API key:
     ```
     API_KEY=your_tmdb_api_key_here
     ```

## How to Run

1. Run the application:
   ```bash
   python main.py
   ```

2. Follow the prompts to choose a genre and enter a release year.

## Example

```
What type of movie do you want to watch?
"Action", "Comedy", "Drama", "Horror", "Romance"
Action
Enter the movie release year: 2010

--- Recommended Movie ---
Title: Inception
Overview: A thief who steals corporate secrets through dream-sharing technology is given the inverse task of planting an idea.
Ratings: 8.8
Original Language: English

Enter 'Y' to recommend another movie or any other key to exit: 
```

## License
This project is open-source and available under the [MIT License](LICENSE).
