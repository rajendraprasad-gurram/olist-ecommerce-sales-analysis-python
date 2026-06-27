import pandas as pd
import matplotlib.pyplot as plt

# Load datasets
orders = pd.read_csv(
    r"C:\Users\gurra\OneDrive\Desktop\Python project file\data\olist_orders_dataset.csv"
)

order_items = pd.read_csv(
    r"C:\Users\gurra\OneDrive\Desktop\Python project file\data\olist_order_items_dataset.csv"
)

products = pd.read_csv(
    r"C:\Users\gurra\OneDrive\Desktop\Python project file\data\olist_products_dataset.csv"
)

# Convert dates
orders["order_purchase_timestamp"] = pd.to_datetime(
    orders["order_purchase_timestamp"]
)

orders["order_delivered_customer_date"] = pd.to_datetime(
    orders["order_delivered_customer_date"]
)

# Merge tables
merged = pd.merge(
    orders,
    order_items,
    on="order_id",
    how="left"
)

merged = pd.merge(
    merged,
    products,
    on="product_id",
    how="left"
)

# Feature Engineering
merged["total_value"] = merged["price"] + merged["freight_value"]
merged["purchase_year"] = merged["order_purchase_timestamp"].dt.year
merged["purchase_month"] = merged["order_purchase_timestamp"].dt.month

orders["delivery_days"] = (
    orders["order_delivered_customer_date"] -
    orders["order_purchase_timestamp"]
).dt.days

# Analysis

revenue_year = (
    merged.groupby("purchase_year")["total_value"]
    .sum()
)

orders_month = (
    merged.groupby("purchase_month")["order_id"]
    .nunique()
)

top_categories = (
    merged.groupby("product_category_name")["total_value"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

delivery = orders["delivery_days"].dropna()

# Dashboard

fig, ax = plt.subplots(2, 2, figsize=(18, 12))

fig.suptitle(
    "Olist E-Commerce Sales Dashboard",
    fontsize=20,
    fontweight="bold"
)

# Revenue by Year
ax[0,0].bar(revenue_year.index, revenue_year.values)
ax[0,0].set_title("Revenue by Year")

ax[0,0].grid(axis="y", linestyle="--", alpha=0.4)

ax[0,1].grid(axis="y", linestyle="--", alpha=0.4)

ax[1,0].grid(axis="x", linestyle="--", alpha=0.4)

ax[1,1].grid(axis="y", linestyle="--", alpha=0.4)

ax[0,0].set_xlabel("Year")
ax[0,0].set_ylabel("Revenue")

# Orders by Month
ax[0,1].plot(
    orders_month.index,
    orders_month.values,
    marker="o"
)

ax[0,0].grid(axis="y", linestyle="--", alpha=0.4)

ax[0,1].grid(axis="y", linestyle="--", alpha=0.4)

ax[1,0].grid(axis="x", linestyle="--", alpha=0.4)

ax[1,1].grid(axis="y", linestyle="--", alpha=0.4)

ax[0,1].set_title("Orders by Month")

ax[0,1].set_xlabel("Month")
ax[0,1].set_ylabel("Orders")

# Top Categories
ax[1,0].barh(
    top_categories.index,
    top_categories.values
)
ax[1,0].invert_yaxis()
ax[1,0].set_title("Top Product Categories")

ax[0,0].grid(axis="y", linestyle="--", alpha=0.4)

ax[0,1].grid(axis="y", linestyle="--", alpha=0.4)

ax[1,0].grid(axis="x", linestyle="--", alpha=0.4)

ax[1,1].grid(axis="y", linestyle="--", alpha=0.4)

ax[1,0].set_xlabel("Revenue")
ax[1,0].set_ylabel("Category")

# Delivery Histogram
ax[1,1].hist(
    delivery,
    bins=30
)
ax[1,1].set_title("Delivery Time Distribution")

ax[0,0].grid(axis="y", linestyle="--", alpha=0.4)

ax[0,1].grid(axis="y", linestyle="--", alpha=0.4)

ax[1,0].grid(axis="x", linestyle="--", alpha=0.4)

ax[1,1].grid(axis="y", linestyle="--", alpha=0.4)

ax[1,1].set_xlabel("Delivery Days")
ax[1,1].set_ylabel("Orders")

plt.tight_layout(rect=[0, 0, 1, 0.96])

plt.savefig(
    r"C:\Users\gurra\OneDrive\Desktop\Python project file\images\dashboard.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()