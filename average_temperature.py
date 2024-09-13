# scripts/average_temperature.py
import pandas as pd

# Load the preprocessed dataset
df = pd.read_csv('/home/shivanesh/WeatherAnalytics/data/chennai_weather_preprocessed.csv')

# Calculate the average temperature
average_temp = df['temp'].mean()
print(f"Average Temperature: {average_temp:.2f}°C")
