# hadoop/mapper_seasonal.py
import sys

# Mapper function to extract month and temperature/rainfall data
for line in sys.stdin:
    data = line.strip().split(',')
    if len(data) > 1:
        month = data[0].split('-')[1]  # Extract month from date
        temp = data[1]
        rainfall = data[2]
        print(f"{month}\t{temp}\t{rainfall}")
