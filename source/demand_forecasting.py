import pandas as pd

df = pd.read_csv("data/processed/inventory_features.csv")

df["forecast_30d_demand"] = df["avg_daily_demand"] * 30

df.to_csv("outputs/stockout_risk.csv", index=False)
