### @author - Saket Mishra

# RaaS Inventory Optimization & Analytics

## Overview
This project simulates an end-to-end inventory management analytics platform for a
Robotics-as-a-Service (RaaS) company managing robots, spare parts, and consumables
across multiple warehouses.

The solution covers:
- Synthetic data generation
- Inventory health analysis
- Stockout risk detection
- Safety stock optimization
- Warehouse performance benchmarking

---

## Business Questions Answered

1. Which SKUs are most likely to stock out in the next 30 days?
2. Where is inventory capital inefficiently deployed?
3. How much safety stock is required to meet SLA targets?
4. Which warehouses underperform operationally?

---

## Dataset

### Synthetic Dataset (Primary)
Generated using realistic supply chain assumptions:
- Daily demand variability
- Lead time uncertainty
- Multi-warehouse operations
- SKU criticality tiers

### Public Reference Dataset
UCI Online Retail Dataset  
https://archive.ics.uci.edu/ml/datasets/online+retail

Used only as a modeling reference.

---

## Key Metrics
- Inventory Turnover
- Days Inventory Outstanding (DIO)
- Fill Rate
- Stockout Probability
- Safety Stock
- ABC Classification

---

## How to Run

```bash
pip install -r requirements.txt
python src/data_generator.py
python src/data_cleaning.py
python src/feature_engineering.py
python src/inventory_analysis.py
python src/demand_forecasting.py
python src/safety_stock.py

