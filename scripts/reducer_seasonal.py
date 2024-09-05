# hadoop/reducer_seasonal.py
import sys

# Reducer function to calculate monthly averages
monthly_data = {}

for line in sys.stdin:
    month, temp, rainfall = line.strip().split('\t')
    if month not in monthly_data:
        monthly_data[month] = {'temp_total': 0, 'rainfall_total': 0, 'count': 0}
    monthly_data[month]['temp_total'] += float(temp)
    monthly_data[month]['rainfall_total'] += float(rainfall)
    monthly_data[month]['count'] += 1

for month, data in monthly_data.items():
    avg_temp = data['temp_total'] / data['count']
    avg_rainfall = data['rainfall_total'] / data['count']
    print(f"Month: {month}, Avg Temp: {avg_temp:.2f}, Avg Rainfall: {avg_rainfall:.2f} mm")

