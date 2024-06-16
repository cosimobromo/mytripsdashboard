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
    
    st.header("Your customizable plots")
    st.markdown("You can select two variables to be plotted against, and another one to color your plot.")

    df = st.session_state["data"]
    
    x_axis = st.selectbox(
            "Select variable for x axis: ", options=columns_to_desc.values(), index = None
        )

    if x_axis is not None: 
        y_axis = st.selectbox(
            "Select variable for y axis: ", options=[col for col in columns_to_desc.values() if col != x_axis], index = None
        )

    if x_axis is not None and y_axis is not None: 
        color = st.selectbox(
            "Select variable for color: ", options=[col for col in columns_to_desc.values() if col not in [x_axis, y_axis]], index = None
        )
    ready_to_plot = True if (x_axis is not None and y_axis is not None and color is not None) else False
    if ready_to_plot:
        line_plot(
            df=df,
            x=desc_to_columns[x_axis],
            y=desc_to_columns[y_axis],
            color=desc_to_columns[color],
        )

else:
    st.warning("No data has been uploaded. Go to upload page")
    st.page_link("pages/1_⬆️ Upload.py", label="Upload your data", icon="⬆️")
