import matplotlib.pyplot as plt
import seaborn as sns

def save_emissions_plot(df, x_col='all_motor_vehicles', y_col='link_length_km'):
    plt.figure(figsize=(10, 6))
    sns.set_style("whitegrid")
    
    sns.scatterplot(data=df, x=x_col, y=y_col, alpha=0.6)
    plt.title(f"UK Traffic Analysis: {x_col} vs {y_col}", fontsize=14)
    plt.xlabel("Total Motor Vehicles")
    plt.ylabel("Link Length (km)")
    
    output_path = "reports/figures/traffic_analysis_plot.png"
    plt.savefig(output_path, dpi=300)
    plt.close()
    print(f"🖼️ Figure saved to: {output_path}")


def save_correlation_heatmap(df):
    """
    Generates a heatmap to show relationships between all numeric variables.
    """
    plt.figure(figsize=(12, 8))
    # Select only numeric columns for correlation
    numeric_df = df.select_dtypes(include=['number'])
    sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
    
    plt.title("Correlation Matrix of UK Traffic & Infrastructure Features")
    
    output_path = "reports/figures/correlation_heatmap.png"
    plt.savefig(output_path, dpi=300)
    plt.close()
    print(f"📊 Correlation heatmap saved to: {output_path}")




import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def save_emissions_plot(df, x_col='all_motor_vehicles', y_col='link_length_km'):
    plt.figure(figsize=(10, 6))
    sns.set_style("whitegrid")
    sns.scatterplot(data=df, x=x_col, y=y_col, alpha=0.6, color='steelblue')
    plt.title(f"UK Traffic Analysis: {x_col} vs {y_col}", fontsize=14)
    plt.savefig("reports/figures/traffic_analysis_plot.png", dpi=300)
    plt.close()

def save_correlation_heatmap(df):
    """Generates a heatmap of all numeric variables."""
    plt.figure(figsize=(12, 8))
    numeric_df = df.select_dtypes(include=['number'])
    sns.heatmap(numeric_df.corr(), annot=True, cmap='RdYlGn', fmt=".2f")
    plt.title("Correlation Matrix of UK Traffic Metrics", fontsize=14)
    plt.savefig("reports/figures/correlation_heatmap.png", dpi=300)
    plt.close()
    print("📊 Correlation heatmap saved to reports/figures/")

def save_traffic_distribution(df):
    """Generates a distribution plot of motor vehicles."""
    plt.figure(figsize=(10, 6))
    sns.histplot(df['all_motor_vehicles'], kde=True, color='green')
    plt.title("Distribution of Total Motor Vehicles across UK Authorities", fontsize=14)
    plt.savefig("reports/figures/traffic_distribution.png", dpi=300)
    plt.close()
    print("📈 Distribution plot saved to reports/figures/")