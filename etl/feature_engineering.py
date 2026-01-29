import pandas as pd
import os

# Load cleaned dataset
base_path = os.path.dirname(__file__)
file_path = os.path.join(base_path, "../data/cleaned_diabetic_data.csv")

df = pd.read_csv(file_path)

print("Initial Shape:", df.shape)

# Convert numeric columns safely
numeric_cols = [
    "time_in_hospital", "num_lab_procedures", "num_procedures",
    "num_medications", "number_outpatient", "number_emergency",
    "number_inpatient"
]

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Feature 1 — Total hospital visits
df["total_visits"] = (
    df["number_outpatient"] +
    df["number_emergency"] +
    df["number_inpatient"]
)

# Feature 2 — High utilization patient flag
df["high_utilization"] = df["total_visits"] > 3

# Feature 3 — Long hospital stay flag
df["long_stay"] = df["time_in_hospital"] > 7

# Feature 4 — Heavy medication burden
df["heavy_medication"] = df["num_medications"] > 10

# Feature 5 — Procedure intensity score
df["procedure_intensity"] = (
    df["num_lab_procedures"] +
    df["num_procedures"]
)

# Feature 6 — Emergency risk flag
df["emergency_risk"] = df["number_emergency"] > 0

# Feature 7 — Readmission target label
df["readmitted_flag"] = df["readmitted"].apply(
    lambda x: 1 if x == "<30" else 0
)

print("Shape After Feature Engineering:", df.shape)

# Save final engineered dataset
output_path = os.path.join(base_path, "../data/engineered_healthcare_data.csv")
df.to_csv(output_path, index=False)

print("✅ Feature-engineered dataset saved to data/engineered_healthcare_data.csv")
