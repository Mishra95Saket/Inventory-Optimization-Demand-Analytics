import pandas as pd
import numpy as np

np.random.seed(42)

def generate_inventory_data():
    skus = [f"SKU_{i}" for i in range(1, 51)]
    warehouses = ["TX", "CA", "NJ"]
    days = pd.date_range("2023-01-01", "2024-12-31")

    records = []

    for sku in skus:
        for wh in warehouses:
            base_demand = np.random.randint(3, 30)
            lead_time = np.random.randint(5, 30)

            inventory = np.random.randint(200, 600)

            for day in days:
                demand = max(0, int(np.random.normal(base_demand, base_demand * 0.3)))
                inventory -= demand

                if inventory < 100:
                    inventory += np.random.randint(300, 600)

                records.append([
                    day, sku, wh, demand, inventory, lead_time
                ])

    df = pd.DataFrame(records, columns=[
        "date", "sku", "warehouse", "daily_demand", "on_hand_inventory", "lead_time_days"
    ])

    df.to_csv("data/raw/inventory_transactions.csv", index=False)

if __name__ == "__main__":
    generate_inventory_data()
