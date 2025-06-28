### streamlit_app.py
import streamlit as st
import pandas as pd
import requests
from ui_components import array_ui_filter, safe_melt

st.set_page_config(page_title="RAFTworks POS Dashboard", layout="wide")
st.title("📊 POS Command Center")

# Load data from FastAPI
resp = requests.get("http://localhost:8000/sales")
df = pd.DataFrame(resp.json())

# Fast filtering listbox
st.write("### 🔍 Filter by Store or City")
filtered_df = array_ui_filter(df, filters=["store_no", "city"])

st.write("### 🧾 Filtered Sales Data")
st.dataframe(filtered_df)
