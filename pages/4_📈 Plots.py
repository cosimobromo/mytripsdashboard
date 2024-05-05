"""_summary_
"""

import streamlit as st
from carplots import line_plot
from input_data import (
    columns_to_desc,
    desc_to_columns,
)

# Set Page Configuration
st.set_page_config(page_title="Plots", page_icon="📈")

# Plot Map with Speed/Consumption information
if st.session_state["data"] is not None:
    df = st.session_state["data"]
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

else:
    st.warning("No data has been uploaded. Go to upload page")
    st.page_link("pages/1_⬆️ Upload.py", label="Upload your data: ", icon="⬆️")
