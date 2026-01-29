import streamlit as st
import pandas as pd

df = pd.read_csv("data/engineered_healthcare_data.csv")

st.title("🦠 Disease & Diagnosis Trends")

if "diag_1" in df.columns:
    top_diag = df["diag_1"].value_counts().head(15)
    st.subheader("Most Common Diagnoses")
    st.bar_chart(top_diag)

st.subheader("📊 Procedure Intensity Distribution")
st.line_chart(df["procedure_intensity"])
