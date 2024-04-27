import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import pandas as pd
import numpy as np
import zipfile

infinity_symbol = "∞"

GPSCols = [" Longitude", " Latitude", " Altitude", "GPS Speed (Meters/second)", "GPS Accuracy(m)", "GPS Bearing(°)", "GPS Satellites", " Horizontal Dilution of Precision", 
           " Bearing", " G(x)", " G(y)", " G(z)", " G(calibrated)"]
ConsumptionCols = ["Trip average Litres/100 KM(l/100km)", "Fuel Level (From Engine ECU)(%)"]
EngineCols = ["Engine RPM(rpm)", "Throttle Position(Manifold)(%)", "Intake Manifold Pressure(psi)", "Turbo Boost & Vacuum Gauge(psi)", "Intake Air Temperature(°C)", "Engine Coolant Temperature(°C)"]
KinCols = ["Acceleration Sensor(X axis)(g)", "Acceleration Sensor(Y axis)(g)", "Acceleration Sensor(Z axis)(g)", "Acceleration Sensor(Total)(g)", "Speed (OBD)(km/h)"]
DistCols = ["Trip Distance(km)", "Trip distance (stored in vehicle profile)(km)"]
TimeCols = ["GPS Time", " Device Time"]
VarCols = ["Barometric pressure (from vehicle)(psi)"]

cols = TimeCols+VarCols+DistCols+KinCols+EngineCols+ConsumptionCols+GPSCols


@st.cache_data
def preprocess_df(df: pd.DataFrame): 
    df = df.replace(infinity_symbol, np.inf)
    df = df[df["GPS Time"] != "GPS Time"]
    df["GPS Time"] = pd.to_datetime(df["GPS Time"], format="%a %b %d %H:%M:%S GMT%z %Y")
    df[" Device Time"] = pd.to_datetime(df[" Device Time"], format="%d-%b-%Y %H:%M:%S.%f")
    df = df.dropna()

    df[GPSCols] = df[GPSCols].astype(float)
    df[ConsumptionCols] = df[ConsumptionCols].astype(float)
    df[EngineCols] = df[EngineCols].astype(float)
    df[KinCols] = df[KinCols].astype(float)
    df[DistCols] = df[DistCols].astype(float)
    df[VarCols] = df[VarCols].astype(float)
    df.fillna(0)
    return df

#@st.cache_data
def map(df): 
    min_vel = 0
    max_vel = df["Speed (OBD)(km/h)"].max() 

    norm_vel = ((df["Speed (OBD)(km/h)"]-min_vel)/(max_vel-min_vel))
    cmap = plt.get_cmap("YlOrRd") 

    df["colors"] = cmap(norm_vel).tolist()

    df = df.rename(columns = {" Latitude": "lat", " Longitude": "lon"})
    st.map(df,
        latitude=' Latitude',
        longitude=' Longitude',
        size = 1, 
        color = "colors")
    
    return df 

# File Upload 
uploaded_file = st.file_uploader("Upload your log data", 
                                 type = ["zip", "csv"], 
                                 help = "Please upload the recorded data. You can either upload the zipped or unzipped content")

if uploaded_file is not None:
    st.write(uploaded_file)
    if uploaded_file.type == "application/zip" or uploaded_file.type == 'application/x-zip-compressed':
        with zipfile.ZipFile(uploaded_file, "r") as z:
            datafile = [file for file in z.namelist() if file.endswith(".csv")][0]
            with z.open(datafile, "r") as csvfile:
                df = pd.read_csv(csvfile, usecols = cols, na_values="-", low_memory=False)
    elif uploaded_file.type == "text/csv":
        df = pd.read_csv(uploaded_file, usecols = cols, na_values = "-", low_memory=False)
    
    df = preprocess_df(df) 
    _ = map(df)