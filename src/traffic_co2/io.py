import pandas as pd
import os

def load_traffic_data(filename):
    """Loads a CSV from the data/raw folder."""
    # This reaches out to find your project root
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    file_path = os.path.join(base_dir, "data", "raw", filename)
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found at: {file_path}")
    
    df = pd.read_csv(file_path)
    print(f"✅ Successfully loaded {filename}")
    return df

def save_processed_data(df, filename):
    """Saves a CSV to the data/processed folder."""
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    output_path = os.path.join(base_dir, "data", "processed", filename)
    df.to_csv(output_path, index=False)
    print(f"💾 Saved processed data to: {output_path}")