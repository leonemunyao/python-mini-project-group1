import pandas as pd
import numpy as np
from typing import List, Dict, Tuple

def analyze_yearly_trends(df: pd.DataFrame, metric: str) -> Dict[int, float]:
    """Calculate yearly averages for temperature"""
    return df.groupby(df['year'], observed=False)[metric].mean().to_dict()

def compare_seasons(df: pd.DataFrame, metric: str) -> Dict[str, Dict[str, float]]:
    """Compare seasonal statitistics for rainfall across seasons"""
    return df.groupby('season', observed=False)[metric].agg(['mean', 'min', 'max']).to_dict('index')

def predict_future_trend(df: pd.DataFrame, metric: str, periods: int = 1) -> Tuple[list, list]:
    """Linear regression to predict future values of a metric"""
    yearly_average = df.groupby('year', observed=False)[metric].mean()
    x = np.arange(len(yearly_average))
    y = yearly_average.values

    # Fit a linear regression model
    z = np.polyfit(x, y, 1)
    p = np.poly1d(z)

    # Predict future values
    future_years = np.arange(len(yearly_average), len(yearly_average) + periods)
    prediction = [p(x) for x in future_years]

    # Ensure both arrays are of the same length
    years = yearly_average.index.tolist()
    values = list(yearly_average.values)

    # Add future years and predictions to the lists
    future_to_years = [int(years[-1]) + i for i in range(periods)]
    years.extend(future_to_years)
    values.extend(prediction)

    # Return the years and predicted values
    return years, values



# Functionality Testing.

if __name__ == "__main__":
    # Test the analysis functions
    try:
        # Load test data
        test_file = "/home/leone/Coding/python-mini-project-group1/data/raw/historical_weather.csv"
        df = pd.read_csv(test_file)
        print("\n=== Weather Analysis Test ===\n")

        # Test 1: Yearly Trends
        print("Testing yearly trends for temperature:")
        yearly_temp = analyze_yearly_trends(df, "temperature")
        print("Yearly temperature averages:", yearly_temp)

        # Test 2: Seasonal Comparison
        print("\nTesting seasonal comparison for rainfall:")
        seasonal_rain = compare_seasons(df, "rainfall")
        print("Seasonal rainfall statistics:", seasonal_rain)

        # Test 3: Future Predictions
        print("\nTesting future temperature predictions:")
        future_years, predictions = predict_future_trend(df, "temperature", periods=2)
        print(f"Predicted temperatures for next 2 years:")
        for year, pred in zip(future_years[-2:], predictions[-2:]):
            print(f"Year {year}: {pred:.2f}°C")

    except Exception as e:
        print(f"Error during testing: {e}")
