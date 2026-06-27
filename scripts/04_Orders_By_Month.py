import pandas as pd
import matplotlib.pyplot as plt

# Load datasets
orders = pd.read_csv(
    r"C:\Users\gurra\OneDrive\Desktop\Python project file\data\olist_orders_dataset.csv"
)

order_items = pd.read_csv(
    r"C:\Users\gurra\OneDrive\Desktop\Python project file\data\olist_order_items_dataset.csv"
)

# Convert date columns
date_columns = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date"
]

for column in date_columns:
    orders[column] = pd.to_datetime(orders[column])

# Merge tables
merged_orders = pd.merge(
    orders,
    order_items,
    on="order_id",
    how="left"
)

# Create purchase month
merged_orders["purchase_month"] = merged_orders["order_purchase_timestamp"].dt.month

# Count orders by month
orders_by_month = merged_orders.groupby("purchase_month")["order_id"].nunique()

print(orders_by_month)

# Plot
plt.figure(figsize=(10,5))
plt.bar(orders_by_month.index, orders_by_month.values)

plt.title("Orders by Month")
plt.xlabel("Month")
plt.ylabel("Number of Orders")

plt.tight_layout()
plt.show()
