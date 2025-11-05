import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# -------------------------------
# Load the data
# -------------------------------
BASE_DIR = Path("bank_marketing_data")
bank = pd.read_csv(BASE_DIR / "bank_data" / "bank.csv", sep=';')
bank_additional = pd.read_csv(BASE_DIR / "bank_additional_data" / "bank-additional" / "bank-additional-full.csv", sep=';')

# -------------------------------
# Basic Info
# -------------------------------
print("✅ Bank data shape:", bank.shape)
print("✅ Bank Additional data shape:", bank_additional.shape)

print("\n📋 Columns in Bank dataset:\n", bank.columns.tolist())
print("\n📋 Columns in Bank Additional dataset:\n", bank_additional.columns.tolist())

# -------------------------------
# Data Cleaning
# -------------------------------
# Drop duplicates
bank.drop_duplicates(inplace=True)
bank_additional.drop_duplicates(inplace=True)

# Handle missing values
print("\n🔍 Missing values in Bank dataset:\n", bank.isnull().sum())
print("\n🔍 Missing values in Bank Additional dataset:\n", bank_additional.isnull().sum())

# -------------------------------
# Data Summary
# -------------------------------
print("\n📊 Summary of Bank dataset:\n", bank.describe(include='all').T.head())
print("\n📊 Summary of Bank Additional dataset:\n", bank_additional.describe(include='all').T.head())

# -------------------------------
# Visualization
# -------------------------------
plt.figure(figsize=(10, 6))
sns.countplot(data=bank, x='y')
plt.title("Bank Term Deposit Subscription (Bank Data)")
plt.xlabel("Subscribed (y)")
plt.ylabel("Count")
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(data=bank_additional, x='y')
plt.title("Bank Term Deposit Subscription (Bank Additional Data)")
plt.xlabel("Subscribed (y)")
plt.ylabel("Count")
plt.show()

# -------------------------------
# Correlation heatmap for numeric features
# -------------------------------
plt.figure(figsize=(12, 8))
sns.heatmap(bank_additional.corr(numeric_only=True), cmap='coolwarm', annot=False)
plt.title("Correlation Heatmap (Bank Additional Data)")
plt.show()
