import pandas as pd
import matplotlib.pyplot as plt

# Load Orders Dataset
orders = pd.read_csv(
    r"C:\Users\gurra\OneDrive\Desktop\Python project file\data\olist_orders_dataset.csv"
)

# Convert datetime columns
date_columns = [
    "order_purchase_timestamp",
    "order_delivered_customer_date"
]

for column in date_columns:
    orders[column] = pd.to_datetime(orders[column])

# Create Delivery Days
orders["delivery_days"] = (
    orders["order_delivered_customer_date"] -
    orders["order_purchase_timestamp"]
).dt.days

# Remove missing values
delivery = orders["delivery_days"].dropna()

print(delivery.describe())

# Histogram
plt.figure(figsize=(10,5))

plt.hist(
    delivery,
    bins=30
)

plt.title("Delivery Time Distribution")
plt.xlabel("Delivery Days")
plt.ylabel("Number of Orders")

plt.tight_layout()
plt.show()
