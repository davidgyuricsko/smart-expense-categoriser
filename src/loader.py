import pandas as pd


def load_transactions(csv_path: str) -> pd.DataFrame:
    """
    Load transactions from a CSV file and return a DataFrame.
    """
    return pd.read_csv(csv_path)
