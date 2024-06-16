import streamlit as st
from carplots import density_plot, gear_plot
from input_data import analyze_data, columns_to_desc, desc_to_columns
# Set Page Configuration
st.set_page_config(page_title="Usage condition", page_icon="🏎️")

# Plot Map with Speed/Consumption information
if st.session_state["data"] is not None:
    df = st.session_state["data"]
    st.markdown("# Engine Usage Conditions ⚙️")
    st.markdown("This page shows your engine usage conditions. Gear ratios are estimated using clustering techniques, please provide feedbacks if you see something weird. 🙂")
    if "GEAR" in df.columns:
        gear_plot(df=df)
        density_plot(df=df)
        st.markdown(f"## Gear ratios")
        st.markdown(f"{len(df.GEAR.unique())-1} _ratios_ have been found. \
                    Aggregated data by gear ratio is reported.")
        st.table(
            df.groupby(by="GEAR").aggregate(
                {"RATIO": "mean", "AVGCOMP": "mean", "OBDSPEED": ["min", "mean", "max"]}
            ).rename(columns = {"RATIO": "Transmission Ratio (km/h)/(rpm)", "AVGCOMP": columns_to_desc["AVGCOMP"], "OBDSPEED": columns_to_desc["OBDSPEED"]})
        )

    st.markdown("**Issues?** Try to run the analysis again...")
    if st.button("Reanalyze your data"): 
        df = analyze_data(df)
else:
    st.warning("No data has been uploaded. Go to upload page")
    st.page_link("pages/1_⬆️ Upload.py", label="Upload your data", icon="⬆️")
