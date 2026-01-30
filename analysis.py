import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file
df = pd.read_csv("students.csv")

print("First 5 rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

# Analysis
average_marks = df["Marks"].mean()
highest_marks = df["Marks"].max()
lowest_marks = df["Marks"].min()

print("\nAverage Marks:", average_marks)
print("Highest Marks:", highest_marks)
print("Lowest Marks:", lowest_marks)

# Gender-wise average
gender_avg = df.groupby("Gender")["Marks"].mean()
print("\nGender-wise Average Marks:")
print(gender_avg)

# Visualization
plt.bar(df["Name"], df["Marks"])
plt.title("Student Marks Analysis")
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
