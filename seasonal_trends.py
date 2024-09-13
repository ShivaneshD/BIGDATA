import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('/home/shivanesh/WeatherAnalytics/data/chennai_weather_preprocessed.csv')

# Convert datetime to extract month
df['month'] = pd.to_datetime(df['datetime'], dayfirst=True).dt.month

# Calculate average temperature and rainfall by month
monthly_avg = df.groupby('month').agg({
    'temp': 'mean',  # Average temperature
    'precip': 'mean'  # Average rainfall
}).reset_index()

# Plot seasonal trends
plt.figure(figsize=(10, 5))

# Plot average temperature
plt.plot(monthly_avg['month'], monthly_avg['temp'], label='Average Temperature (°C)', color='r', marker='o')

# Plot average rainfall
plt.plot(monthly_avg['month'], monthly_avg['precip'], label='Average Rainfall (mm)', color='b', marker='o')

plt.xlabel('Month')
plt.title('Seasonal Trends in Chennai')
plt.xticks(monthly_avg['month'], ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.legend()
plt.grid(True)
plt.show()
