import pandas as pd

class DataProcessor:
    def load_data(self, file_path: str) -> pd.DataFrame:
        print(f"Loading data from {file_path}")
        df = pd.read_csv(file_path)
        return df

    def clean_data(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.drop_duplicates()
        df = df.dropna()
        return df

    def aggregate_statistics(self, df: pd.DataFrame):
        print("\nDataset Summary:")
        print(df.describe())
