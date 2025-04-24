import pandas as pd
import csv
from typing import List, Dict
import os

def load_weather_data(file_path: str) -> pd.DataFrame:
    """
    Load weather data from a CSV file.
    
    Args:
        file_path (str): Path to the CSV file containing weather data.
        
    Returns:
        pd.DataFrame: DataFrame containing the weather data.
    """
    #Check if the file exists
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return pd.DataFrame()
    
    try:
        # Read the CSV file
        df = pd.read_csv(file_path)

        # Valiidate required columns
        required_columns = ['date', 'temperature', 'rainfall', 'humidity', 'season', 'month', 'year']
        for column in required_columns:
            if column not in df.columns:
                raise ValueError(f"Missing required column: {column}")
            

        df = pd.read_csv(file_path)
        df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
        df['temperature'] = df['temperature'].astype(float)
        df['rainfall'] = df['rainfall'].astype(float)
        df['humidity'] = df['humidity'].astype(float)
        df['season'] = df['season'].astype('category')
        df['month'] = df['date'].dt.month.astype('category')
        df['year'] = df['date'].dt.year.astype('category')

        # Check for missing values and handle them
        if df.isnull().values.any():
            print("Warning: Missing values found in the datase.")
            df = df.dropna()
            print("Missing values have been dropped: {len(df)} rows remaining.")


        return df
    
    except Exception as e:
        print(f"Error loading weather data: {e}")
        return pd.DataFrame()


if __name__ == "__main__":
    # Test the data loader
    file_path = "/home/leone/Coding/python-mini-project-group1/data/raw/historical_weather.csv"
    df = load_weather_data(file_path)
    if not df.empty:
        print("\nData Loading Success!")
        print(f"Shape: {df.shape}")
        print("\nFirst few rows:")
        print(df.head())
        print("\nData Types:")
        print(df.dtypes)