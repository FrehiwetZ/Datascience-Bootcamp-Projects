import pandas as pd

df = pd.read_csv("titanic.csv")

#Exploration of the dataset

print("First 5 rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())