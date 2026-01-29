import pandas as pd
import os

# File path
base_path = os.path.dirname(__file__)
file_path = os.path.join(base_path, "../data/diabetic_data.csv")

# Load dataset
df = pd.read_csv(file_path)

print("\nOriginal Shape:", df.shape)

# Replace '?' with NaN (missing value marker in this dataset)
df.replace("?", pd.NA, inplace=True)

# Drop columns with too many missing values
threshold = len(df) * 0.5
df = df.dropna(axis=1, thresh=threshold)

# Drop duplicate rows if any
df = df.drop_duplicates()

print("\nShape After Cleaning:", df.shape)

# Save cleaned dataset
output_path = os.path.join(base_path, "../data/cleaned_diabetic_data.csv")
df.to_csv(output_path, index=False)

print("\n✅ Cleaned dataset saved to data/cleaned_diabetic_data.csv")
