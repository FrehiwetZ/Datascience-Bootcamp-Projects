import json
import os

from src.stat_engine import StatEngine
from src.monte_carlo import run_simulations

# Load the user created JSON data 
with open("./data/sample_salaries.json","r") as f:
    data = json.load(f)

engine = StatEngine(data)

print("Mean:", engine.get_mean())
print("Median:", engine.get_median())
print("Mode:", engine.get_mode())
print("Variance:", engine.get_variance())
print("Std Dev:", engine.get_standard_deviation())
print("Outliers:", engine.get_outliers())

# Run simulation
run_simulations()