import pandas as pd

df = pd.read_csv("titanic.csv")

#Exploration of the dataset

print("First 5 rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

#Data Cleaning

df["Age"].fillna(df["Age"].median(), inplace=True)

df["Embarked"].fillna(df["Embarked"].mode()[0], inplace=True)

df.drop(columns=["Cabin"], inplace=True)

df.drop_duplicates(inplace = True)


                          