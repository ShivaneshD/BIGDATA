#!/usr/bin/env python3
# # hadoop/reducer_temp.py
import sys

# Reducer function to calculate the average temperature
total_temp = 0
total_count = 0

for line in sys.stdin:
    temp, count = line.strip().split('\t')
    total_temp += float(temp)
    total_count += int(count)

average_temp = total_temp / total_count if total_count != 0 else 0
print(f"Average Temperature: {average_temp:.2f}")
