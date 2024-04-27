"""_summary_

Returns:
    _type_: _description_
"""

from typing import List, Dict
import zipfile
import io
import os
import pandas as pd
import numpy as np
import yaml


def return_column_names(columns: List[Dict], names: bool = True) -> List[str]:
    """_summary_

    Args:
        columns (List[Dict]): _description_
        names (bool, optional): _description_. Defaults to True.

    Returns:
        List[str]: _description_
    """
    if names:
        return [list(column.values())[0] for column in columns]
    else:
        return [list(column.keys())[0] for column in columns]


with open(
    os.path.join(os.path.dirname(__file__), "input_data.yaml"), "r", encoding="utf-8"
) as input_data_file:
    input_data_conf = yaml.safe_load(input_data_file)

GPSCols = return_column_names(input_data_conf["GPSCols"])
ConsumptionCols = return_column_names(input_data_conf["ConsumptionCols"])
EngineCols = return_column_names(input_data_conf["EngineCols"])
KinCols = return_column_names(input_data_conf["KinCols"])
DistCols = return_column_names(input_data_conf["DistCols"])
TimeCols = return_column_names(input_data_conf["TimeCols"])
VarCols = return_column_names(input_data_conf["VarCols"])

input_cols = (
    TimeCols + VarCols + DistCols + KinCols + EngineCols + ConsumptionCols + GPSCols
)

# Update column names
GPS = return_column_names(input_data_conf["GPSCols"], names=False)
Consumption = return_column_names(input_data_conf["ConsumptionCols"], names=False)
Engine = return_column_names(input_data_conf["EngineCols"], names=False)
Kin = return_column_names(input_data_conf["KinCols"], names=False)
Dist = return_column_names(input_data_conf["DistCols"], names=False)
Time = return_column_names(input_data_conf["TimeCols"], names=False)
Var = return_column_names(input_data_conf["VarCols"], names=False)

infinity_symbol = input_data_conf["infinity_symbol"]


def load_uploaded_data(uploaded_file: io.BytesIO) -> pd.DataFrame:
    """_summary_

    Args:
        uploaded_file (io.BytesIO): _description_

    Returns:
        pd.DataFrame: _description_
    """
    if (
        uploaded_file.type == "application/zip"
        or uploaded_file.type == "application/x-zip-compressed"
    ):
        with zipfile.ZipFile(uploaded_file, "r") as z:
            datafile = [file for file in z.namelist() if file.endswith(".csv")][0]
            with z.open(datafile, "r") as csvfile:
                df = pd.read_csv(
                    csvfile, usecols=input_cols, na_values="-", low_memory=False
                )
    elif uploaded_file.type == "text/csv":
        df = pd.read_csv(
            uploaded_file, usecols=input_cols, na_values="-", low_memory=False
        )
    return df


def cast_rename_columns(df: pd.DataFrame) -> pd.DataFrame:
    """_summary_

    Args:
        df (pd.DataFrame): _description_

    Returns:
        pd.DataFrame: _description_
    """
    df["GPS Time"] = pd.to_datetime(df["GPS Time"], format="%a %b %d %H:%M:%S GMT%z %Y")
    df[" Device Time"] = pd.to_datetime(
        df[" Device Time"], format="%d-%b-%Y %H:%M:%S.%f"
    )
    # Rename columns
    df = df.rename(
        columns={input_name: final_name for input_name, final_name in zip(GPSCols, GPS)}
    )
    df = df.rename(
        columns={
            input_name: final_name
            for input_name, final_name in zip(ConsumptionCols, Consumption)
        }
    )
    df = df.rename(
        columns={
            input_name: final_name for input_name, final_name in zip(EngineCols, Engine)
        }
    )
    df = df.rename(
        columns={input_name: final_name for input_name, final_name in zip(KinCols, Kin)}
    )
    df = df.rename(
        columns={
            input_name: final_name for input_name, final_name in zip(DistCols, Dist)
        }
    )
    df = df.rename(
        columns={
            input_name: final_name for input_name, final_name in zip(TimeCols, Time)
        }
    )
    df = df.rename(
        columns={input_name: final_name for input_name, final_name in zip(VarCols, Var)}
    )
    # Cast columns to float
    df[GPS] = df[GPS].astype(float)
    df[Consumption] = df[Consumption].astype(float)
    df[Engine] = df[Engine].astype(float)
    df[Kin] = df[Kin].astype(float)
    df[Dist] = df[Dist].astype(float)
    df[Var] = df[Var].astype(float)
    return df


def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """_summary_

    Args:
        df (pd.DataFrame): _description_

    Returns:
        pd.DataFrame: _description_
    """
    df = df.replace(infinity_symbol, np.inf)
    # Remove multiple headers
    df = df[df["GPS Time"] != "GPS Time"]
    # Drop NaN rows
    df = df.dropna()

    df = cast_rename_columns(df)
    df.fillna(0)
    return df