from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import joblib
import os

def train_co2_model(df, target_col='co2_emissions'):
    """
    Trains a model to predict CO2 levels based on traffic features.
    """
    # Select only numeric features for the baseline
    features = df.select_dtypes(include=['number']).drop(columns=[target_col])
    target = df[target_col]
    
    X_train, X_test, y_train, y_test = train_test_split(
        features, target, test_size=0.2, random_state=42
    )
    
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    predictions = model.predict(X_test)
    r2 = r2_score(y_test, predictions)
    
    print(f"📊 Model Trained. R² Score: {r2:.4f}")
    
    return model