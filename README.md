# GIC Python Take-Home Assessment

This project performs movie data analysis using Python and pandas, based on the MovieLens dataset format.  
It demonstrates skills in data cleaning, aggregation, visualization, and modular code organization.

## Features
- Load and clean datasets using **pandas**
- Generate dataset statistics and summary insights
- Identify top-rated movies by average score
- Visualize rating distribution using **matplotlib** and **seaborn**
- Simple FastAPI endpoint for demonstration

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


## How to Run

1. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate

2. Install dependencies:

pip install -r requirements.txt

3. Run the analysis interactively:

python

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

4. uvicorn app:app --reload

uvicorn app:app --reload

Open your browser at  http://127.0.0.1:8000/

Tools & Libraries

Python 3.9+

pandas, numpy, matplotlib, seaborn

fastapi, uvicorn

