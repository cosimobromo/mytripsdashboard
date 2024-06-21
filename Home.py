"""_summary_
"""

import os
import pandas as pd
import streamlit as st
from input_data import input_cols, analyze_data, preprocess_data

# ---------- Set Page Configuration ----------
st.set_page_config(page_title="My Trips Dashboard", page_icon="🚗")

# Description Page
st.markdown("# Analyze your car trips! 🗺️")

st.markdown(
    "This tool allows you to easily review you car trip, by analying your _driving conditions_, _itinerary_ and _plot_ the recorded data. Data must be recorded connecting a WiFi/Bluetooth \
        **OBDII** Interface to your Smartphone using [Torque Pro application](https://play.google.com/store/apps/details?id=org.prowl.torque&pcampaignid=web_share). \
        "
)

# Inizialize data
if "data" not in st.session_state.keys():
    st.session_state["data"] = None

if st.session_state["data"] is None:
    st.subheader("Go to upload page to continue")
    st.page_link("pages/1_⬆️ Upload.py", label="Upload your data", icon="⬆️")

    sample_data = st.button(label = "Don't have any data? Play with a sample dataset ✨")

    if sample_data: 
        df = pd.read_csv(
            os.path.join(os.path.realpath(os.path.dirname(__file__)), "data", "data", "sample_data.csv"), usecols=input_cols, na_values="-", low_memory=False
        )
        df = preprocess_data(df)
        df = analyze_data(df)
        st.session_state["data"] = df
        st.page_link("pages/2_📋 Summary.py", label="Look into trip highlights", icon="📋")
        st.page_link("pages/3_🌍 Map Trip.py", label="See my trip map", icon="🌍")
        st.page_link(
            "pages/4_⚙️ Usage Condition.py", label="Engine usage condition", icon="⚙️"
        )
        st.page_link("pages/5_📈 Plots.py", label="Plots", icon="📈")
else:
    st.info("You already loaded data for your session. Navingate the available pages!")
