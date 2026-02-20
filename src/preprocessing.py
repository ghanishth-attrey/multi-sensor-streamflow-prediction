import pandas as pd
from pathlib import Path

def load_datasets(base_path):
    base = Path(base_path)
    
    sat = pd.read_csv(base / "satellite.csv", parse_dates=["date"])
    ground = pd.read_csv(base / "ground.csv", parse_dates=["date"])
    flow = pd.read_csv(base / "streamflow.csv", parse_dates=["date"])

    return sat, ground, flow


def merge_datasets(sat, ground, flow):
    df = sat.merge(ground, on="date", suffixes=("_sat", "_ground"))
    df = df.merge(flow, on="date")
    df = df.sort_values("date")
    return df
