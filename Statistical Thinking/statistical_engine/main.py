import json
import os
from src.stat_engine import StatEngine

file_path = os.path.join(os.path.dirname(__file__), "data", "sample_salaries.json")

# Load the user given JSON data
with open(file_path, "r") as f:
    data = json.load(f)

engine = StatEngine(data)


print("Mean:", engine.get_mean())
print("Median:", engine.get_median())
print("Mode:", engine.get_mode())
print("Population Standard Deviation:", engine.get_standard_deviation())
print("Sample Standard Deviation:", engine.get_standard_deviation(is_sample=True))
print("Outliers:", engine.get_outliers())