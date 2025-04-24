import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from typing import List, Tuple

def plot_yearly_trends(years: List[int], values: List[float], metric: str):
    """
    Plot yearly trends for a given metric.
    
    Args:
        years (List[int]): List of years.
        values (List[float]): List of values corresponding to the years.
        metric (str): The metric being plotted (e.g., 'temperature', 'rainfall').
    """
    plt.figure(figsize=(10, 5))
    plt.plot(years[:-1], values[:-1], 'b-', label='Historical')
    plt.plot(years[-2:], values[-2:], 'r--', label='Prediction')
    plt.title(f'Yearly {metric.capitalize()} Trends')
    plt.xlabel('Year')
    plt.ylabel(metric.capitalize())
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_seasonal_comparison(data: dict, metric: str):
    """
    Plot seasonal comparison for a given metric.
    
    Args:
        data (dict): Dictionary containing seasonal data.
        metric (str): The metric being plotted (e.g., 'temperature', 'rainfall').
    """
    seasons = list(data.keys())
    means = [data[season]['mean'] for season in seasons]
    mins = [data[season]['min'] for season in seasons]
    maxs = [data[season]['max'] for season in seasons]

    x = range(len(seasons))
    
    plt.figure(figsize=(10, 5))
    plt.bar(x, means, yerr=[mins, maxs], capsize=5)
    plt.xticks(x, seasons)
    plt.title(f'Seasonal Comparison of {metric.capitalize()}')
    plt.xlabel('Season')
    plt.ylabel(metric.capitalize())
    plt.grid(True)
    plt.show()

def plot_future_trend(years: List[int], values: List[float], metric: str):
    """
    Plot future trend for a given metric.
    
    Args:
        years (List[int]): List of years.
        values (List[float]): List of values corresponding to the years.
        metric (str): The metric being plotted (e.g., 'temperature', 'rainfall').
    """
    plt.figure(figsize=(10, 5))
    plt.plot(years, values, 'g-', label='Predicted')
    plt.title(f'Future Trend of {metric.capitalize()}')
    plt.xlabel('Year')
    plt.ylabel(metric.capitalize())
    plt.legend()
    plt.grid(True)
    plt.show()

# The above code defines functions to visualize weather data trends, including yearly trends, seasonal comparisons, and future predictions.
# The functions use matplotlib to create line plots and bar charts, making it easier to interpret the data visually.
# The code is modular, allowing for easy integration into a larger weather analysis pipeline.


# ...Testing Functionality...

if __name__ == "__main__":
    try:
        # Load sample data
        import pandas as pd
        test_file = "/home/leone/Coding/python-mini-project-group1/data/raw/historical_weather.csv"
        df = pd.read_csv(test_file)

        print("\n=== Testing Visualization Functions ===\n")

        # Test 1: Yearly Trends
        print("Testing yearly trends plot...")
        years = df['year'].unique().tolist()
        values = df.groupby('year')['temperature'].mean().tolist() + [25]
        plot_yearly_trends(years + [years[-1] + 1], values, "temperature")

        # Test 2: Seasonal Comparison
        print("\nTesting seasonal comparison plot...")
        seasonal_stats = df.groupby('season')['rainfall'].agg(['mean', 'min', 'max'])
        seasonal_data = {
            season: {
                'mean': stats['mean'],
                'min': stats['min'],
                'max': stats['max']
            }
            for season, stats in seasonal_stats.iterrows()
        }
        plot_seasonal_comparison(seasonal_data, "rainfall")

        # Test 3: Future Trend
        print("\nTesting future trend plot...")
        future_years = years + [years[-1] + 1] + [years[-1] + 2]
        future_values = values + [values[-1] + 0.5]
        plot_future_trend(future_years, future_values, "temperature")

        print("\nAll visualization tests completed successfully.")

    except Exception as e:
        print(f"Error during visualization testing: {e}")
        import traceback
        traceback.print_exc()

# This script serves as a testing module for the visualization functions.
# It loads sample data, tests the plotting functions, and handles any exceptions that may occur.
