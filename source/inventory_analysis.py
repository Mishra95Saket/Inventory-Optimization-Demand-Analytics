import pandas as pd

df = pd.read_csv("data/processed/inventory_features.csv")

df["annual_demand"] = df["avg_daily_demand"] * 365
df["inventory_value"] = df["avg_inventory"] * 1000

df = df.sort_values("inventory_value", ascending=False)
df["cum_pct"] = df["inventory_value"].cumsum() / df["inventory_value"].sum()

df["abc_class"] = df["cum_pct"].apply(
    lambda x: "A" if x <= 0.8 else "B" if x <= 0.95 else "C"
)

df.to_csv("outputs/abc_analysis.csv", index=False)
