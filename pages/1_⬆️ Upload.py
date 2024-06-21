"""_summary_
"""

import streamlit as st
from input_data import load_uploaded_data, preprocess_data, analyze_data

load_uploaded_data = st.cache_data(load_uploaded_data)
preprocess_data = st.cache_data(preprocess_data)

st.markdown("# Upload Data ⬆️")
st.markdown("Drag and drop you _.zip_ or _.csv_ file containing your data (that shall be collected using [Torque Pro application](https://play.google.com/store/apps/details?id=org.prowl.torque&pcampaignid=web_share)). \
            If you want to upload another dataset, please re-apply the same procedure. ")

# File Upload
uploaded_file = st.file_uploader(
    "Upload your log data",
    type=["zip", "csv"],
    help="Please upload the recorded data. You can either upload the zipped or unzipped content",
)

if uploaded_file is not None:
    df = load_uploaded_data(uploaded_file=uploaded_file)
    df = preprocess_data(df)
    df = analyze_data(df)
    st.session_state["data"] = df
    st.page_link("pages/2_📋 Summary.py", label="Look into trip highlights", icon="📋")
    st.page_link("pages/3_🌍 Map Trip.py", label="See my trip map", icon="🌍")
    st.page_link(
        "pages/4_⚙️ Usage Condition.py", label="Engine usage condition", icon="⚙️"
    )
    st.page_link("pages/5_📈 Plots.py", label="Plots", icon="📈")
