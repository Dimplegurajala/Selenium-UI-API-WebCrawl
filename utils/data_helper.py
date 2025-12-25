import csv
import os

def get_csv_data(file_name):
    path = os.path.join(os.path.dirname(__file__), "..", "data", file_name)
    data = []
    with open(path, mode='r') as f:
        reader = csv.DictReader(f) # Use DictReader for clarity
        for row in reader:
            # Returns: (user, pwd, expected, test_id)
            data.append((row['user'], row['pwd'], row['expected'], row['test_id']))
    return data