import json
import os
from src.stat_engine import StatEngine

# Path to JSON file relative to this script
file_path = os.path.join(os.path.dirname(__file__), "data", "sample_salaries.json")

# Load the JSON data
with open(file_path, "r") as f:
    data = json.load(f)

# Initialize StatEngine
engine = StatEngine(data)

# Print some statistics
print("Mean:", engine.get_mean())
print("Median:", engine.get_median())
print("Mode:", engine.get_mode())
print("Population Standard Deviation:", engine.get_standard_deviation())
print("Sample Standard Deviation:", engine.get_standard_deviation(is_sample=True))
print("Outliers:", engine.get_outliers())