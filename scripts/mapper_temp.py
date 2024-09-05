# hadoop/mapper_temp.py
import sys

# Mapper function to extract temperature values
for line in sys.stdin:
    data = line.strip().split(',')
    if len(data) > 1:
        temp = data[1]  # Assuming temperature is the second column
        print(f"{temp}\t1")
