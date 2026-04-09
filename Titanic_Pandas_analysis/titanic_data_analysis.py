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
    labels=["Child", "Young", "Young Adult", "Adult", "Senior"])

survival_age_group = df.groupby("AgeGroup")["Survived"].mean()
print("\nSurvival Rate By Age Group:")
print(survival_age_group)

#filterring data for specific analysis

female_survivors =df[(df["Sex"]== "female") & (df["Survived"] == 1)]
print("\nFemale Passengers Who Survived:")
print(female_survivors)

children_survivors = df[(df["Age"] < 12) & (df["Survived"] == 1)]
print("\nChildren Who Survived:")
print(children_survivors)

first_class_survivors = df[(df["Pclass"] == 1) & (df["Survived"] == 1)]
print("\nFirst-Class Passengers Who Survived:")
print(first_class_survivors)

#Data Visualization

print("\n----- Insights -----")

print("1. Females were more likely to survive than males.")

print("2. Passenger class affected survival. 1st class passengers had the highest survival rate.")

print("3. Children had higher survival chances, indicating that children were prioritized.")

print("4. Female passengers in 1st class had the highest survival probability.")