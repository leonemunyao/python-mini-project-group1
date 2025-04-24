from data_loader import load_weather_data
from analysis import analyze_yearly_trends, compare_seasons, predict_future_trend
from visualization import plot_yearly_trends, plot_seasonal_comparison, plot_future_trend
from utilis import validate_metric, validate_years, formal_results

def main():
    # Load the weather data
    file_path = '/home/leone/Coding/python-mini-project-group1/data/raw/historical_weather.csv'
    df = load_weather_data(file_path)

    if df.empty:
        print("No data loaded. Exiting.")
        return

    # Analyze yearly trends
    metric = 'temperature'
    yearly_trends = analyze_yearly_trends(df, metric)
    print("Yearly Trends:")
    print(yearly_trends)

    # Compare seasons
    seasonal_comparison = compare_seasons(df, metric)
    print("Seasonal Comparison:")
    print(seasonal_comparison)

    # Predict future trends
    future_years, future_values = predict_future_trend(df, metric, periods=5)
    
    # Validate the data
    if not validate_metric(future_values) or not validate_years(future_years):
        print("Invalid data for plotting.")
        return

    # Plot the results
    plot_yearly_trends(yearly_trends.keys(), list(yearly_trends.values()), metric)
    plot_seasonal_comparison(seasonal_comparison, metric)
    plot_future_trend(future_years, future_values, metric)
    # Format and display results
    results = {
        'Yearly Trends': yearly_trends,
        'Seasonal Comparison': seasonal_comparison,
        'Future Predictions': dict(zip(future_years, future_values))
    }
    formatted_results = formal_results(results)
    print("Formatted Results:")
    print(formatted_results)

if __name__ == "__main__":
    main()
# This script serves as the main entry point for the weather analysis application.
# It loads the weather data, performs analysis, and visualizes the results.
# The script is structured to be modular, allowing for easy updates and maintenance.
# The use of functions from different modules promotes code reusability and clarity.