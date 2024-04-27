"""_summary_
"""

import streamlit as st
from input_data import load_uploaded_data, preprocess_data
from carplots import tripmap

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
    tripmap(df)
