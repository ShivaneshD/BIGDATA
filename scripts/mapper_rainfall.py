# hadoop/mapper_rainfall.py
import sys

# Mapper function to extract rainfall data
for line in sys.stdin:
    data = line.strip().split(',')
    if len(data) > 2:
        rainfall = data[2]  # Assuming rainfall is the third column
        print(f"{rainfall}\t1")
