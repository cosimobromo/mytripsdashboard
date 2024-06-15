"""_summary_
"""

from typing import List
import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st
import pandas as pd
from input_data import columns_to_desc, desc_to_columns


def tripmap(df: pd.DataFrame):
    """_summary_

    Args:
        df (pd.DataFrame): _description_
    """

    fig = px.scatter_mapbox(
        df,
        lat="LATITUDE",
        lon="LONGITUDE",
        color="OBDSPEED",
        color_continuous_scale=px.colors.cyclical.IceFire,
        zoom=10,
        mapbox_style="carto-positron",
        custom_data=["OBDSPEED", "AVGCOMP"],
    )
    fig.update_traces(
        hovertemplate="<b>Speed (km/h): </b>%{customdata[0]}</b><br>"
        + "<b>Consumption (l/100km): </b>%{customdata[1]:.2f}</b><br>"
        + "Latitude: %{lat:.5f}<br>"
        + "Longitude: %{lon:.5f}<br>"
        + "<extra></extra>",
        mode="markers",
        marker={"sizemode": "area", "sizeref": 10},
    )
    st.plotly_chart(fig, theme="streamlit")


def line_plot(
    df: pd.DataFrame,
    x: str,
    y: str,
    color: str | None = None,
    hover_data: List[str] | None = None,
):
    """_summary_

    Args:
        df (pd.DataFrame): _description_
        x (str): _description_
        y (str): _description_
        color (str | None, optional): _description_. Defaults to None.
        hover_data (List[str] | None, optional): _description_. Defaults to None.
    """
    fig = px.scatter(df, x=x, y=y, color=color, hover_data=hover_data)
    fig.update_layout(
        title=f"{columns_to_desc[y]} vs {columns_to_desc[x]}",
        xaxis_title=columns_to_desc[x],
        yaxis_title=columns_to_desc[y],
    )
    st.plotly_chart(fig, theme="streamlit")


def density_plot(df: pd.DataFrame):
    """_summary_

    Args:
        df (pd.DataFrame): _description_
    """
    fig = px.density_contour(
        df, x="ENGINERPM", y="OBDSPEED", nbinsx=50, nbinsy=50, color="GEAR"
    )
    fig.update_layout(
        title=f"{columns_to_desc['ENGINERPM']} vs {columns_to_desc['OBDSPEED']} density plot",
        xaxis_title=columns_to_desc["ENGINERPM"],
        yaxis_title=columns_to_desc["OBDSPEED"],
    )
    st.plotly_chart(fig)  # , theme="streamlit")


def gear_plot(df: pd.DataFrame) -> None:
    """_summary_

    Args:
        df (pd.DataFrame): _description_
    """
    fig = px.scatter(
        df,
        x="ENGINERPM",
        y="OBDSPEED",
        color="GEAR",
        marginal_x="box",
        marginal_y="box",
        title=f"{columns_to_desc['ENGINERPM']} vs {columns_to_desc['OBDSPEED']} - Gear Ratios",
    )
    fig.update_layout(
        xaxis_title=columns_to_desc["ENGINERPM"],
        yaxis_title=columns_to_desc["OBDSPEED"],
    )
    st.plotly_chart(fig, theme="streamlit")
