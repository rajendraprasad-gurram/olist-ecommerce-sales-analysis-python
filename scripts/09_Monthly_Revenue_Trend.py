import pandas as pd
import matplotlib.pyplot as plt

# Load datasets
orders = pd.read_csv(
    r"C:\Users\gurra\OneDrive\Desktop\Python project file\data\olist_orders_dataset.csv"
)

order_items = pd.read_csv(
    r"C:\Users\gurra\OneDrive\Desktop\Python project file\data\olist_order_items_dataset.csv"
)

# Convert datetime
orders["order_purchase_timestamp"] = pd.to_datetime(
    orders["order_purchase_timestamp"]
)

# Merge
merged_orders = pd.merge(
    orders,
    order_items,
    on="order_id",
    how="left"
)

# Total revenue
merged_orders["total_value"] = (
    merged_orders["price"] +
    merged_orders["freight_value"]
)

# Create Year-Month column
merged_orders["purchase_year_month"] = (
    merged_orders["order_purchase_timestamp"]
    .dt.to_period("M")
    .astype(str)
)

# Monthly revenue trend
monthly_revenue = (
    merged_orders
    .groupby("purchase_year_month")["total_value"]
    .sum()
)

print(monthly_revenue)

# Plot
plt.figure(figsize=(13, 6))

plt.plot(
    monthly_revenue.index,
    monthly_revenue.values,
    marker="o",
    linewidth=2.5,
    markersize=6
)

plt.title(
    "Monthly Revenue Trend",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Year-Month", fontsize=12)
plt.ylabel("Revenue", fontsize=12)

plt.grid(axis="y", linestyle="--", alpha=0.4)

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    r"C:\Users\gurra\OneDrive\Desktop\Python project file\images\monthly_revenue_trend.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()