import pandas as pd
import numpy as np
from scipy.stats import norm
import yaml

with open("config.yaml") as f:
    config = yaml.safe_load(f)

z = norm.ppf(config["service_level"])

df = pd.read_csv("data/processed/inventory_features.csv")

df["safety_stock"] = z * df["demand_std"] * np.sqrt(df["lead_time"])
df["reorder_point"] = (df["avg_daily_demand"] * df["lead_time"]) + df["safety_stock"]

df.to_csv("outputs/warehouse_kpis.csv", index=False)
