from data_processor import DataProcessor

class MovieAnalyzer:
    def __init__(self):
        self.processor = DataProcessor()

    def get_top_movies(self, ratings_df, movies_df):
        merged = ratings_df.merge(movies_df, on="movieId")
        result = merged.groupby("title")["rating"].mean().sort_values(ascending=False).head(10)
        print("\nTop Rated Movies:\n", result)
        return result
