import pandas as pd

orders = pd.read_csv(
    r"C:\Users\gurra\OneDrive\Desktop\Python project file\data\olist_orders_dataset.csv"
)

print("\nFirst 5 Rows")
print(orders.head())

print("\nDataset Shape")
print(orders.shape)

print("\nDataset Info")
print(orders.info())

print("\nMissing Values")
print(orders.isnull().sum())

print("\nDuplicate Rows")
print(orders.duplicated().sum())

print("\nOrder Status Values")
print(orders["order_status"].unique())

print("\nOrder Status Counts")
print(orders["order_status"].value_counts())

print("\nUnique Order IDs")
print(orders["order_id"].nunique())

date_columns = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date"
]

for column in date_columns:
    orders[column] = pd.to_datetime(orders[column])

orders["purchase_year"] = orders["order_purchase_timestamp"].dt.year
orders["purchase_month"] = orders["order_purchase_timestamp"].dt.month
orders["purchase_month_name"] = orders["order_purchase_timestamp"].dt.month_name()
orders["purchase_day_name"] = orders["order_purchase_timestamp"].dt.day_name()
orders["purchase_hour"] = orders["order_purchase_timestamp"].dt.hour

print("\nCreated Date Features")
print(orders[[
    "order_purchase_timestamp",
    "purchase_year",
    "purchase_month",
    "purchase_month_name",
    "purchase_day_name",
    "purchase_hour"
]].head())

print("\nOrders by Year")
print(orders["purchase_year"].value_counts().sort_index())

print("\nOrders by Month")
print(orders["purchase_month_name"].value_counts())

print("\nOrders by Day")
print(orders["purchase_day_name"].value_counts())

print("\nOrders by Hour")
print(orders["purchase_hour"].value_counts().sort_index())