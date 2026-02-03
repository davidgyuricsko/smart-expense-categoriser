import pandas as pd

from categoriser import categorise_description


def add_categories(df: pd.DataFrame) -> pd.DataFrame:
    """
    Return a copy of df with a new 'category' column.
    Expects columns: 'description', 'amount'
    """
    out = df.copy()
    out["category"] = out["description"].apply(categorise_description)
    return out
