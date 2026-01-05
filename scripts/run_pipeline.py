import sys
import os

# Fix path so script can see the src folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.traffic_co2.io import load_traffic_data, save_processed_data
from src.traffic_co2.cleaning import clean_traffic_data
from src.traffic_co2.features import engineer_features
from src.traffic_co2.modeling import train_co2_model
from src.traffic_co2.viz import save_emissions_plot

def main():
    try:
        # 1. Load & Clean
        df = load_traffic_data("Traffic_local.csv")
        df = clean_traffic_data(df)
        
        # 2. Feature Engineering
        df = engineer_features(df)
        
        # 3. Visualization
        # Using 'all_motor_vehicles' and 'link_length_km' from your dataset
        save_emissions_plot(df, x_col='all_motor_vehicles', y_col='link_length_km')
        
        # 4. Modeling
        # Predicting link_length_km as a proxy for now
        model = train_co2_model(df, target_col='link_length_km')
        
        # 5. Save Results
        save_processed_data(df, "Final_Research_Data.csv")
        
        print("\n🏆 FULL RESEARCH PIPELINE COMPLETE!")
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()


# ... after save_emissions_plot(df, ...) ...
save_correlation_heatmap(df)