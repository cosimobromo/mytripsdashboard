import streamlit as st
from carplots import tripmap

# Set Page Configuration
st.set_page_config(page_title="Map Trip", page_icon="🌍")

# Plot Map with Speed/Consumption information
if st.session_state["data"] is not None:
    df = st.session_state["data"]
    tripmap(df)
else:
    st.warning("No data has been uploaded. Go to upload page")
    st.page_link("pages/1_⬆️ Upload.py", label="Upload your data: ", icon="⬆️")
