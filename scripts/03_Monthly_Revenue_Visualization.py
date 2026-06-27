import pandas as pd
import matplotlib.pyplot as plt

orders = pd.read_csv(
    r"C:\Users\gurra\OneDrive\Desktop\Python project file\data\olist_orders_dataset.csv"
)

order_items = pd.read_csv(
    r"C:\Users\gurra\OneDrive\Desktop\Python project file\data\olist_order_items_dataset.csv"
)

date_columns = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date"
]

for column in date_columns:
    orders[column] = pd.to_datetime(orders[column])

merged_orders = pd.merge(
    orders,
    order_items,
    on="order_id",
    how="left"
)

merged_orders["total_value"] = merged_orders["price"] + merged_orders["freight_value"]
merged_orders["purchase_month"] = merged_orders["order_purchase_timestamp"].dt.month

revenue_by_month = merged_orders.groupby("purchase_month")["total_value"].sum()

print(revenue_by_month)

plt.figure(figsize=(10, 5))
plt.bar(revenue_by_month.index, revenue_by_month.values)
plt.title("Revenue by Month")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.tight_layout()
plt.show()
