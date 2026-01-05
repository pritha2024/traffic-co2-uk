import pandas as pd

def clean_traffic_data(df):
    """
    Standardizes column names and handles missing values.
    """
    # 1. Standardize column names (lowercase with underscores)
    df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]
    
    # 2. Handle missing values
    # In environmental data, we often use forward fill for time-series or median
    df = df.fillna(df.median(numeric_only=True))
    
    print("Cleaning complete: Column names standardized and missing values handled.")
    return df