import pandas as pd

df = pd.read_csv("data/raw/inventory_transactions.csv", parse_dates=["date"])

df = df[df["daily_demand"] >= 0]
df = df.drop_duplicates()

df.to_csv("data/processed/inventory_clean.csv", index=False)
