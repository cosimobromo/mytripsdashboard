"""_summary_
"""

import streamlit as st

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
else:
    st.info("You already loaded data for your session. Navingate the available pages!")
