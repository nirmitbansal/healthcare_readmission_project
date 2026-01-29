import pandas as pd
import os

# Get base directory path
base_path = os.path.dirname(__file__)

# Build dataset path
file_path = os.path.join(base_path, "../data/diabetic_data.csv")

# Load dataset
df = pd.read_csv(file_path)

# Dataset size
print("\n📦 Dataset Shape (Rows, Columns):")
print(df.shape)

# Column list
print("\n🧱 Column Names:")
print(df.columns.tolist())

# Sample rows
print("\n🔍 Sample Data Preview:")
print(df.head())

# Missing values summary
print("\n⚠️ Missing Values Per Column:")
print(df.isnull().sum())
