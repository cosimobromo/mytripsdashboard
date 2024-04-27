"""_summary_
"""

import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd


def tripmap(df: pd.DataFrame):
    """_summary_

    Args:
        df (pd.DataFrame): _description_
    """
    min_vel = 0
    max_vel = df["OBDSPEED"].max()

    norm_vel = (df["OBDSPEED"] - min_vel) / (max_vel - min_vel)
    cmap = plt.get_cmap("YlOrRd")

    df["colors"] = cmap(norm_vel).tolist()

    st.map(df, size=2, color="colors")
