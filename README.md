# 📘🌍 Traffic, Transport & CO₂: A Data-Driven Analysis of UK Local Authorities


---

## 📖 Project Overview
This project investigates the relationship between **Road Traffic Volume** and **Transport-related Greenhouse Gas (GHG) Emissions** across United Kingdom Local Authorities. 

Using data from 2005 to 2023, the analysis explores:
1.  **Correlation:** Is traffic volume the sole driver of emissions, or does population density play a role?
2.  **Inequality:** Which regions are "Hotspots" for high per-capita emissions?
3.  **Trends:** Has the UK successfully "decoupled" economic activity (driving) from carbon output over the last 18 years?

## 📂 Dataset Information
The analysis integrates two official UK government datasets:

1.  **Road Traffic Statistics (TRA8901)** * *Source:* Department for Transport (DfT)  
    * *Description:* Annual vehicle miles broken down by Local Authority and vehicle type.  
    * *Link:* [data.gov.uk - Road Traffic Statistics](https://www.data.gov.uk/dataset/208c0e7b-353f-4e2d-8b7a-1a7118467acc/gb-road-traffic-counts)

2.  **UK Local Authority Greenhouse Gas Emissions** * *Source:* Department for Energy Security and Net Zero (DESNZ)  
    * *Description:* Annual CO₂ emissions estimates (kt) broken down by sector (Transport, Industry, etc.).  
    * *Link:* [data.gov.uk - UK Local Authority GHG Emissions](https://www.data.gov.uk/dataset/723c243d-2f1a-4d27-8b61-cdb93e5b10ff/local_authority_carbon_dioxide_emissions)

> **Note:** For the cross-sectional analysis (Correlation/Hotspots), the data was filtered to the most recent common year (2023) to ensure statistical validity.

## 🛠️ Methodology & Tools
The project is implemented in **Python 3** using a Jupyter Notebook (`Pritha_Assignment.ipynb`).

**Key Libraries Used:**
* **Pandas:** For data cleaning, merging, and transformation.
* **NumPy:** For numerical operations.
* **Seaborn & Matplotlib:** For statistical visualization (Heatmaps, Regressions, Time-series).

**Analytical Steps:**
1.  **Data Wrangling:** Cleaning headers, handling missing values, and merging datasets on `Local Authority` + `Year`.
2.  **Feature Engineering:** Creating metrics like `vehicles_per_capita` and `vehicle_density` (vehicles/km²).
3.  **Outlier Detection:** Using IQR (Interquartile Range) to identify major transport hubs (e.g., Leeds, Hampshire).
4.  **Statistical Modelling:** Pearson Correlation Matrix and Linear Regression ($R^2$ analysis).

## 💡 Key Findings

### 1. The "Urban Efficiency" Paradox
While total traffic strongly correlates with total emissions ($r \approx 0.9$), **population density** is negatively correlated with **per-capita emissions**. Residents in dense urban areas (like London) have significantly lower carbon footprints due to public transport availability, despite high congestion.

### 2. Rural Hotspots
The analysis identified a specific cluster of "High-Traffic, High-Emission" hotspots. These are predominantly rural authorities in **Scotland** and the **South West** (e.g., Highland, Rutland). In these areas, car dependency is structural, not optional.


## 🚀 How to Run the Code
1.  Ensure you have Python installed with the following libraries:
    ```bash
    pip install pandas numpy matplotlib seaborn
    ```
2.  Place the dataset CSV files in the same directory as the notebook (or update the file paths in **Section 2.1**).
3.  Open `Pritha_Assignment.ipynb` in Jupyter Lab or Notebook.
4.  Run all cells sequentially.

---
