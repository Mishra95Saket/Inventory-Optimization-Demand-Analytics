import pandas as pd

df = pd.read_csv("data/processed/inventory_clean.csv")

features = (
    df.groupby(["sku", "warehouse"])
      .agg(
          avg_daily_demand=("daily_demand", "mean"),
          demand_std=("daily_demand", "std"),
          avg_inventory=("on_hand_inventory", "mean"),
          lead_time=("lead_time_days", "mean")
      )
      .reset_index()
)

features.to_csv("data/processed/inventory_features.csv", index=False)
