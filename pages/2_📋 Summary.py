import streamlit as st
from input_data import columns_to_desc, desc_to_columns
from carplots import dist_plot
# Set Page Configuration
st.set_page_config(page_title="Summary", page_icon="📋")

# Plot Map with Speed/Consumption information
if st.session_state["data"] is not None:
    df = st.session_state["data"]
    st.markdown("# Your trip summary 📋")
    st.markdown("This page shows your itinerary resume. Select all the variables of interest. ")
    
    vars = st.multiselect("Select what you are interested in: ", options = columns_to_desc.values())
    
    for var in vars: 
        st.subheader(var, divider = True) 
        if desc_to_columns[var] != "GPSTIME": 
            min_col, mean_col, max_col = st.columns(3) 
            min_col.metric("Minimum", round(df[desc_to_columns[var]].min(), 2))
            mean_col.metric("Average", round(df[desc_to_columns[var]].mean(), 2))
            max_col.metric("Maximum", round(df[desc_to_columns[var]].max(), 2))
            dist_plot(df=df, x = desc_to_columns[var])
        elif desc_to_columns[var] == "GPSTIME": 
            start_trip_col, end_trip_col = st.columns(2) 
            start_trip_col.metric("Start Trip Time", df[desc_to_columns[var]].min().strftime("%d/%m/%Y, %H:%M:%S"))
            end_trip_col.metric("End Trip Time", df[desc_to_columns[var]].max().strftime("%d/%m/%Y, %H:%M:%S"))
else:
    st.warning("No data has been uploaded. Go to upload page")
    st.page_link("pages/1_⬆️ Upload.py", label="Upload your data", icon="⬆️")
