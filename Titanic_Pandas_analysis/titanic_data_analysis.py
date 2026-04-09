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

#Data Analysis

survival_gender = df.groupby("Sex")["Survived"].mean()
print("\nSurvival Rate By Gender:")
print(survival_gender)

survival_class= df.groupby("Pclass")["Survived"].mean()
print("\nSurvival Rate By Passenger Class:")
print(survival_class)

survival_age = df.groupby("Pclass")["Age"].mean()
print("\nAverage Age By Passenger Class:")
print(survival_age)

df["AgeGroup"] = pd.cut(
    df["Age"],
    bins=[0 ,12, 18, 35, 60, 100], 
    labels=["Child", "Young", "Adult", "Senior"])

survival_age_group = df.groupby("AgeGroup")["Survived"].mean()
print("\nSurvival Rate By Age Group:")
print(survival_age_group)

