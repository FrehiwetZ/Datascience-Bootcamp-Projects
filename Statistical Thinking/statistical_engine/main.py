import sys
import os
import json

sys.path.append(os.path.abspath("src"))

from stat_engine import StatEngine
from monte_carlo import run_simulations

# Load user JSON data
file_path = os.path.join("data", "sample_salaries.json")

with open(file_path) as f:
    data = json.load(f)
engine = StatEngine(data)

print("Mean:", engine.get_mean())
print("Median:", engine.get_median())
print("Mode:", engine.get_mode())
print("Variance:", engine.get_variance())
print("Std Dev:", engine.get_standard_deviation())
print("Outliers:", engine.get_outliers())

# Run the simulation
run_simulations()