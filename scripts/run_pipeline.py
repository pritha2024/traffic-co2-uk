import sys
import os

# Fix path so script can see the src folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.traffic_co2.io import load_traffic_data, save_processed_data
from src.traffic_co2.cleaning import clean_traffic_data
from src.traffic_co2.features import engineer_features
from src.traffic_co2.modeling import train_co2_model
# Added all three visualization functions to the import list
from src.traffic_co2.viz import save_emissions_plot, save_correlation_heatmap, save_traffic_distribution

def main():
    try:
        # 1. Load & Clean
        df = load_traffic_data("Traffic_local.csv")
        df = clean_traffic_data(df)
        
        # 2. Feature Engineering
        df = engineer_features(df)
        
        # 3. Visualization
        print("\n🎨 Generating Research Visualizations...")
        save_emissions_plot(df, x_col='all_motor_vehicles', y_col='link_length_km')
        save_correlation_heatmap(df)
        save_traffic_distribution(df)
        
        # 4. Modeling
        # Predicting link_length_km as a proxy for infrastructure capacity
        model = train_co2_model(df, target_col='link_length_km')
        
        # 5. Save Results
        save_processed_data(df, "Final_Research_Data.csv")
        
        print("\n🏆 FULL RESEARCH PIPELINE COMPLETE!")
        print("Check 'reports/figures/' for your three new plots.")
        
    except Exception as e:
        print(f"❌ Error during pipeline: {e}")

if __name__ == "__main__":
    main()