"""Streamlit dashboard template"""

import streamlit as st
import pandas as pd
from utils.reporting_template import get_high_sales

df = pd.read_csv("data/stores.csv")

st.title("Store Sales Dashboard")
threshold = st.slider("Sales Threshold", 1000, 3000, 1800)

high_sales = get_high_sales(df, threshold)

if high_sales.empty:
    st.warning("NONE had high sales")
else:
    st.success(f"{len(high_sales)} store(s) exceeded threshold")
    st.dataframe(high_sales)
    st.download_button(
        "Download Excel", high_sales.to_csv(index=False), "high_sales.csv"
    )
