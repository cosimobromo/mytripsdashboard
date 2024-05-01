"""_summary_
"""

import streamlit as st
from input_data import (
    load_uploaded_data,
    preprocess_data,
    columns_to_desc,
    desc_to_columns,
)
from carplots import tripmap, line_plot, density_plot

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

    # Plot Map with Speed/Consumption information
    tripmap(df)

    with st.form("Line Plot"):
        x_axis = st.selectbox(
            "Select variable for x axis: ", options=columns_to_desc.values()
        )
        y_axis = st.selectbox(
            "Select variable for y axis: ", options=columns_to_desc.values()
        )
        color = st.selectbox(
            "Select variable for color: ", options=columns_to_desc.values()
        )
        ready_to_plot = st.form_submit_button("Plot")
        if ready_to_plot:
            line_plot(
                df=df,
                x=desc_to_columns[x_axis],
                y=desc_to_columns[y_axis],
                color=desc_to_columns[color],
            )

    density_plot(df)
