import streamlit as st
from carplots import density_plot, gear_plot

# Set Page Configuration
st.set_page_config(page_title="Usage condition", page_icon="🏎️")

# Plot Map with Speed/Consumption information
if st.session_state["data"] is not None:
    df = st.session_state["data"]
    density_plot(df=df)
    if "GEAR" in df.columns:
        gear_plot(df=df)

        st.markdown(f"# Found {len(df['GEAR'].unique())} gear ratios")
        st.table(
            df.groupby(by="GEAR").aggregate(
                {"RATIO": "mean", "AVGCOMP": "mean", "OBDSPEED": ["min", "mean", "max"]}
            )
        )
else:
    st.warning("No data has been uploaded. Go to upload page")
    st.page_link("pages/1_⬆️ Upload.py", label="Upload your data: ", icon="⬆️")
