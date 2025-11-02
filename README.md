# GIC Python Take-Home Assessment

This project analyses movie data using Python and pandas, following the MovieLens dataset format.
It focuses on data loading, cleaning, basic statistics, visualization, and a simple API built with FastAPI.

## Features

Load and clean movie and ratings data using pandas

Generate basic dataset summaries and insights

Find top-rated movies based on average ratings

Visualize rating distribution using matplotlib / seaborn

Expose a small FastAPI endpoint for quick demo access

## Folder Structure

gic-python-assessment/
│
├── data_processor.py
├── movie_analyzer.py
├── data_visualizer.py
├── app.py
├── requirements.txt
├── README.md
└── sample_data/
├── movies.csv
└── ratings.csv


---

## How to Run

1. **Create and activate a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate

2. **Install dependencies**
    ```
    pip install -r requirements.txt

3. **Run the analysis interactively**
   ```python
   from data_processor import DataProcessor
   from movie_analyzer import MovieAnalyzer
   from data_visualizer import plot_rating_distribution

   processor = DataProcessor()
   ratings = processor.load_data("sample_data/ratings.csv")
   movies = processor.load_data("sample_data/movies.csv")

   clean_ratings = processor.clean_data(ratings)
   processor.aggregate_statistics(clean_ratings)

   analyzer = MovieAnalyzer()
   analyzer.get_top_movies(clean_ratings, movies)
   plot_rating_distribution(clean_ratings)


4. **Start the FastAPI service**
   ```
   uvicorn app:app --reload

Then open http://127.0.0.1:8000 in your browser.

## API Endpoints

    Endpoint	Description
    /	         Welcome message

## Tools & Libraries

    Python 3.9+

    pandas, numpy

    matplotlib, seaborn

    fastapi, uvicorn

Development was done locally on Python 3.7, but the code targets Python 3.9+ as required.

## AI Usage and Documentation

    Tools Used

    ChatGPT – for code review and organizing ideas

    GitHub Copilot – for small function scaffolding

How I Used Them

    I used AI mainly to review structure and sanity-check ideas.
    All functions were written, tested, and adjusted by me.
    The AI suggestions were only used to refine clarity and code layout.

## Key Prompts

    Suggest a clean structure for a MovieLens data analysis project using pandas and FastAPI

    Review pandas merge logic and filtering by minimum ratings

    Show an example pytest case for a FastAPI health endpoint

Modifications and My Additions

    Grouped data by (movieId, title) instead of just title to prevent duplicates

    Simplified plots to plain matplotlib for consistency

    Wrote my own docstrings and inline comments

Verified logic manually and through small tests (tests may need Python 3.9+)

I understand all parts of this code and can walk through my design decisions and trade-offs during the discussion

## Tests

    Includes simple pytest cases (`tests/test_api.py`) that verify:
    - The FastAPI root endpoint (`/`) returns the expected welcome message
    - The health check endpoint (`/health`) responds with status 200 and `{"status": "ok"}`


## Visualization Output

    
    Running the analysis generates a sample plot file named `rating_distribution.png` in the project root, which shows the rating distribution from the dataset.

