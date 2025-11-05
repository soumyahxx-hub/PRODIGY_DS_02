import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load datasets
bank = pd.read_csv("bank_marketing_data/bank_data/bank.csv", sep=';')
bank_additional = pd.read_csv("bank_marketing_data/bank_additional_data/bank-additional/bank-additional-full.csv", sep=';')

# ---------- INSIGHT 1: Age distribution ----------
plt.figure(figsize=(10, 6))
sns.histplot(bank_additional['age'], bins=30, kde=True, color='skyblue')
plt.title("Age Distribution of Bank Clients")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

# ---------- INSIGHT 2: Job type vs Subscription ----------
plt.figure(figsize=(12, 6))
sns.countplot(data=bank_additional, x='job', hue='y', order=bank_additional['job'].value_counts().index)
plt.title("Subscription by Job Type")
plt.xlabel("Job")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()

# ---------- INSIGHT 3: Education level vs Subscription ----------
plt.figure(figsize=(10, 6))
sns.countplot(data=bank_additional, x='education', hue='y', order=bank_additional['education'].value_counts().index)
plt.title("Subscription by Education Level")
plt.xlabel("Education")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()

# ---------- INSIGHT 4: Correlation heatmap ----------
plt.figure(figsize=(10, 8))
sns.heatmap(bank_additional.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap (Numeric Features)")
plt.show()
