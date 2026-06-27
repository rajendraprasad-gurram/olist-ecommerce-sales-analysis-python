import pandas as pd

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

merged_orders["total_value"] = (
    merged_orders["price"] + merged_orders["freight_value"]
)

merged_orders["purchase_year"] = merged_orders["order_purchase_timestamp"].dt.year

print("\nMerged Dataset Shape")
print(merged_orders.shape)

print("\nMerged Dataset Columns")
print(merged_orders.columns)

print("\nSample Total Value")
print(merged_orders[["price", "freight_value", "total_value"]].head())

print("\nTotal Revenue")
print(merged_orders["total_value"].sum())

print("\nAverage Order Item Value")
print(merged_orders["total_value"].mean())

print("\nHighest Order Item Value")
print(merged_orders["total_value"].max())

print("\nLowest Order Item Value")
print(merged_orders["total_value"].min())

print("\nRevenue by Year")
print(merged_orders.groupby("purchase_year")["total_value"].sum())

print("\nAverage Revenue by Year")
print(merged_orders.groupby("purchase_year")["total_value"].mean())