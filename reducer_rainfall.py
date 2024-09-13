
# hadoop/reducer_rainfall.py
import sys

# Reducer function to calculate the total rainfall
total_rainfall = 0

for line in sys.stdin:
    rainfall, count = line.strip().split('\t')
    total_rainfall += float(rainfall)

print(f"Total Rainfall: {total_rainfall:.2f} mm")
