from data_loader import load_weather_data
from analysis import analyze_yearly_trends, compare_seasons, predict_future_trend
from visualization import plot_yearly_trends, plot_seasonal_comparison, plot_future_trend
from utils import validate_metric, validate_years, formal_results
import sys
import pandas as pd
import os
from datetime import datetime


def export_results(results: dict, metric: str):
    """
    Export analysis results to CSV file
    
    Args:
        results (dict): Analysis results dictionary
        metric (str): Analyzed metric name
    """
    output_dir = '/home/leone/Coding/python-mini-project-group1/data/processed'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    # Prepare data for export
    export_data = {
        'analysis_date': datetime.now().strftime('%Y-%m-%d'),
        'metric': metric,
        'analysis_type': [],
        'category': [],
        'value': []
    }
    
    # Format the nested dictionary into flat structure
    for analysis_type, data in results.items():
        if isinstance(data, dict):
            for category, value in data.items():
                export_data['analysis_type'].append(analysis_type)
                export_data['category'].append(category)
                export_data['value'].append(value)
        else:
            export_data['analysis_type'].append(analysis_type)
            export_data['category'].append('value')
            export_data['value'].append(data)
    
    # Create DataFrame and export
    df = pd.DataFrame(export_data)
    filepath = os.path.join(output_dir, 'analysis_results.csv')
    
    # Append to existing file if it exists, otherwise create new
    mode = 'a' if os.path.exists(filepath) else 'w'
    header = not os.path.exists(filepath)
    
    df.to_csv(filepath, mode=mode, header=header, index=False)
    print(f"\nResults exported to: {filepath}")


def main(metric='temperature', test_mode=False):
    """
    Main function to run weather analysis
    
    Args:
        metric (str): Metric to analyze ('temperature', 'rainfall', 'humidity')
        test_mode (bool): If True, runs in test mode with minimal output
    """
    try:
        # Load the weather data
        file_path = '/home/leone/Coding/python-mini-project-group1/data/raw/historical_weather.csv'
        df = load_weather_data(file_path)

        if df.empty:
            print("No data loaded. Exiting.")
            return False

        # Analyze yearly trends
        yearly_trends = analyze_yearly_trends(df, metric)
        if not test_mode:
            print(f"\nYearly {metric} Trends:")
            print(yearly_trends)

        # Compare seasons
        seasonal_comparison = compare_seasons(df, metric)
        if not test_mode:
            print(f"\nSeasonal {metric} Comparison:")
            print(seasonal_comparison)

        # Predict future trends
        future_years, future_values = predict_future_trend(df, metric, periods=2)
        
        # Validate the data
        if not validate_metric(future_values) or not validate_years(future_years):
            print("Invalid data for plotting.")
            return False
        
        all_years = list(yearly_trends.keys()) + future_years[-2:]
        all_values = list(yearly_trends.values()) + future_values[-2:]

        # Plot results if not in test mode
        if not test_mode:
            plot_yearly_trends(all_years, all_values, metric)
                             
            plot_seasonal_comparison(seasonal_comparison, metric)

            plot_future_trend(future_years, future_values, metric)

        # Format and display results
        results = {
            'Yearly Trends': {str(year): float(value) for year, value in yearly_trends.items()},
            'Seasonal Comparison': {
                season: {k: float(v) for k, v in stats.items()}
                for season, stats in seasonal_comparison.items()
            },
            'Future Predictions': {
                str(year): float(value) 
                for year, value in zip(future_years[-2:], future_values[-2:])
            }
        }
        
        if not test_mode:
            formatted_results = formal_results(results)
            print("\nFormatted Results:")
            print(formatted_results)
            # Export results to CSV
            export_results(results, metric)
            

        return True

    except Exception as e:
        print(f"Error in main: {str(e)}")
        return False


def run_tests():
    """Run systematic tests of the main functionality"""
    print("\n=== Running Main Program Tests ===\n")
    
    test_cases = [
        ('temperature', "Testing temperature analysis"),
        ('rainfall', "Testing rainfall analysis"),
        ('humidity', "Testing humidity analysis")
    ]
    
    passed = 0
    total = len(test_cases)
    
    for metric, description in test_cases:
        print(f"\nTest: {description}")
        try:
            result = main(metric=metric, test_mode=True)
            if result:
                print(f"✓ {metric} analysis completed successfully")
                passed += 1
            else:
                print(f"✗ {metric} analysis failed")
        except Exception as e:
            print(f"✗ {metric} analysis error: {str(e)}")
    
    print(f"\nTest Summary: {passed}/{total} tests passed")
    return passed == total

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        success = run_tests()
        sys.exit(0 if success else 1)
    else:
        main()

# This script serves as the main entry point for the weather analysis application.
# It loads the weather data, performs analysis, and visualizes the results.
# The use of functions from different modules promotes code reusability and clarity.

