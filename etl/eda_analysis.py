import pandas as pd
import os

# Load engineered dataset
base_path = os.path.dirname(__file__)
file_path = os.path.join(base_path, "../data/engineered_healthcare_data.csv")

df = pd.read_csv(file_path)

print("\nDataset Shape:", df.shape)

# KPI 1 — Readmission Rate
readmission_rate = df["readmitted_flag"].mean() * 100
print("\n📊 Readmission Rate (%):", round(readmission_rate, 2))

# KPI 2 — Average Hospital Stay
avg_stay = df["time_in_hospital"].mean()
print("\n🏥 Average Hospital Stay (Days):", round(avg_stay, 2))

# KPI 3 — High Utilization Patients
high_util_pct = df["high_utilization"].mean() * 100
print("\n🚨 High Utilization Patients (%):", round(high_util_pct, 2))

# KPI 4 — Emergency Visit Rate
emergency_rate = df["emergency_risk"].mean() * 100
print("\n🚑 Emergency Visit Rate (%):", round(emergency_rate, 2))

# KPI 5 — Heavy Medication Burden Rate
heavy_med_pct = df["heavy_medication"].mean() * 100
print("\n💊 Heavy Medication Patients (%):", round(heavy_med_pct, 2))

# Top diagnoses distribution (if available)
if "diag_1" in df.columns:
    print("\n🦠 Top Diagnoses:")
    print(df["diag_1"].value_counts().head(10))

# Length of stay distribution summary
print("\n📈 Length of Stay Distribution:")
print(df["time_in_hospital"].describe())

# Procedure intensity summary
print("\n🧪 Procedure Intensity Summary:")
print(df["procedure_intensity"].describe())
