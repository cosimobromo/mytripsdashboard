"""_summary_
"""

import streamlit as st
from input_data import (
    load_uploaded_data,
    preprocess_data,
)

load_uploaded_data = st.cache_data(load_uploaded_data)
preprocess_data = st.cache_data(preprocess_data)

# File Upload
uploaded_file = st.file_uploader(
    "Upload your log data",
    type=["zip", "csv"],
    help="Please upload the recorded data. You can either upload the zipped or unzipped content",
)

if uploaded_file is not None:
    df = load_uploaded_data(uploaded_file=uploaded_file)
    df = preprocess_data(df)
    st.session_state["data"] = df

    st.page_link("pages/2_🌍 Map Trip.py", label="See my trip map", icon="🌍")
    st.page_link(
        "pages/3_⚙️ Usage Condition.py", label="Engine usage condition", icon="⚙️"
    )
    st.page_link("pages/4_📈 Plots.py", label="Plots", icon="📈")
