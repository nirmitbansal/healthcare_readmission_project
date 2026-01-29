import streamlit as st
import pandas as pd

df = pd.read_csv("data/engineered_healthcare_data.csv")

st.title("⚠️ Patient Risk & Readmission Analysis")

high_risk = df[(df["readmitted_flag"] == 1) | (df["high_utilization"] == True)]

st.metric("High Risk Patients", len(high_risk))

st.subheader("🚨 High-Risk Patient Records")
st.dataframe(high_risk.head(200))

st.subheader("📈 Medication Burden Distribution")
st.bar_chart(df["num_medications"].value_counts())
