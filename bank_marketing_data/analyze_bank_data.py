import pandas as pd
from pathlib import Path

# -------------------------------
# Define file paths
# -------------------------------
BASE_DIR = Path("bank_marketing_data")

# Paths to the two CSV files
BANK_FILE = BASE_DIR / "bank_data" / "bank.csv"
BANK_ADDITIONAL_FILE = BASE_DIR / "bank_additional_data" / "bank-additional" / "bank-additional-full.csv"

# -------------------------------
# Verify file existence
# -------------------------------
print("🔍 Checking file locations...")
print(f"Bank file: {BANK_FILE.exists()} -> {BANK_FILE}")
print(f"Bank additional file: {BANK_ADDITIONAL_FILE.exists()} -> {BANK_ADDITIONAL_FILE}")

# -------------------------------
# Load datasets
# -------------------------------
try:
    bank = pd.read_csv(BANK_FILE, sep=';')
    bank_additional = pd.read_csv(BANK_ADDITIONAL_FILE, sep=';')
    print("\n✅ Both datasets loaded successfully!\n")
except FileNotFoundError as e:
    print("❌ File not found! Please check the paths.")
    print(e)
    exit()

# -------------------------------
# Display basic info
# -------------------------------
print("📊 Bank Dataset Preview:")
print(bank.head(), "\n")

print("📊 Bank Additional Dataset Preview:")
print(bank_additional.head(), "\n")

print("✅ Shape of Bank Data:", bank.shape)
print("✅ Shape of Bank Additional Data:", bank_additional.shape)


