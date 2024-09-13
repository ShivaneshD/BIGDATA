# scripts/seasonal_trends.py
import pandas as pd

# Load the preprocessed dataset
df = pd.read_csv('/home/shivanesh/WeatherAnalytics/data/chennai_weather_preprocessed.csv')

# Convert datetime to extract month
df['month'] = pd.to_datetime(df['datetime'], dayfirst=True).dt.month

# Calculate average temperature and rainfall by month
monthly_avg = df.groupby('month').agg({
    'temp': 'mean',  # Average temperature
    'precip': 'mean'  # Average rainfall
}).reset_index()

# Print monthly averages
print(monthly_avg)
