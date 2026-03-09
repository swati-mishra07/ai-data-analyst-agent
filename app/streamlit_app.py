import sys
import os
import streamlit as st
import pandas as pd

# FIX: allow Streamlit to find src folder
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT_DIR)

from src.agent import generate_insights

st.title("AI Data Analyst Agent")

# OPTION 1: Upload CSV
uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

# OPTION 2: Use sample dataset

if st.button("Use Sample Dataset", key="sample_data"):
    df = pd.read_csv("data/adult.csv")
    st.success("Loaded sample dataset!")

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    st.subheader("Dataset Shape")
    st.write(df.shape)

    if st.button("Generate Insights", key="sample_insight"):
        summary = df.describe(include="all").to_string()
        insights = generate_insights(summary)
        st.subheader("AI Insights")
        st.write(insights)

# If user uploads file
if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    st.subheader("Dataset Shape")
    st.write(df.shape)

    if st.button("Generate Insights", key="upload_insight"):
        summary = df.describe(include="all").to_string()
        insights = generate_insights(summary)
        st.subheader("AI Insights")
        st.write(insights)
