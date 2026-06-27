import pandas as pd
import matplotlib.pyplot as plt

# Load datasets
orders = pd.read_csv(
    r"C:\Users\gurra\OneDrive\Desktop\Python project file\data\olist_orders_dataset.csv"
)

order_items = pd.read_csv(
    r"C:\Users\gurra\OneDrive\Desktop\Python project file\data\olist_order_items_dataset.csv"
)

# Merge tables
merged_orders = pd.merge(
    orders,
    order_items,
    on="order_id",
    how="left"
)

# Create total value
merged_orders["total_value"] = (
    merged_orders["price"] +
    merged_orders["freight_value"]
)

# Customer Spending
customer_spending = (
    merged_orders
    .groupby("customer_id")["total_value"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(customer_spending)

# Plot
plt.figure(figsize=(12,6))

plt.barh(
    customer_spending.index,
    customer_spending.values
)

plt.title("Top 10 Customers by Spending")
plt.xlabel("Total Spending")
plt.ylabel("Customer ID")

plt.gca().invert_yaxis()

plt.tight_layout()

plt.show()