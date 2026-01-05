import pandas as pd

def engineer_features(df):
    """Creates features based on UK traffic columns."""
    # Create a density feature (Vehicles per KM)
    if 'all_motor_vehicles' in df.columns and 'link_length_km' in df.columns:
        df['vehicle_density'] = df['all_motor_vehicles'] / (df['link_length_km'] + 0.1)
    
    print("🧪 Feature engineering complete: Density calculated.")
    return df