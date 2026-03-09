import pandas as pd


def load_data(file_path: str):
    try:
        df = pd.read_csv(file_path)
        print("Dataset loaded successfully")
        return df
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"Error loading dataset: {e}")
