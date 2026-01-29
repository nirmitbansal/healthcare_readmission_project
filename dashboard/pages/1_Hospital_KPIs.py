import streamlit as st
import pandas as pd

df = pd.read_csv("data/engineered_healthcare_data.csv")

st.title("🏥 Hospital Performance KPIs")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Admissions", len(df))
col2.metric("Readmission Rate (%)", round(df["readmitted_flag"].mean() * 100, 2))
col3.metric("Avg Hospital Stay (Days)", round(df["time_in_hospital"].mean(), 2))
col4.metric("Emergency Visit Rate (%)", round(df["emergency_risk"].mean() * 100, 2))

st.subheader("📊 Admissions by Length of Stay")
st.bar_chart(df["time_in_hospital"].value_counts())
