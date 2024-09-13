# scripts/total_rainfall.py
import pandas as pd

# Load the preprocessed dataset
df = pd.read_csv('/home/shivanesh/WeatherAnalytics/data/chennai_weather_preprocessed.csv')

# Calculate the total rainfall
total_rainfall = df['precip'].sum()  # Assuming 'precip' is the column for rainfall
print(f"Total Rainfall: {total_rainfall:.2f} mm")
