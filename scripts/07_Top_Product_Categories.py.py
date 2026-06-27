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

# Convert date column
orders["order_purchase_timestamp"] = pd.to_datetime(
    orders["order_purchase_timestamp"]
)

# Merge orders with order items
merged_orders = pd.merge(
    orders,
    order_items,
    on="order_id",
    how="left"
)

# Merge with products
merged_products = pd.merge(
    merged_orders,
    products,
    on="product_id",
    how="left"
)

# Create total value
merged_products["total_value"] = (
    merged_products["price"] + merged_products["freight_value"]
)

# Revenue by product category
category_revenue = (
    merged_products
    .groupby("product_category_name")["total_value"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(category_revenue)

# Plot
plt.figure(figsize=(10, 6))
plt.barh(category_revenue.index, category_revenue.values)

plt.title("Top 10 Product Categories by Revenue")
plt.xlabel("Revenue")
plt.ylabel("Product Category")

# Polished Plot
plt.figure(figsize=(12, 7))

bars = plt.barh(
    category_revenue.index,
    category_revenue.values
)

plt.title(
    "Top 10 Product Categories by Revenue",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Revenue", fontsize=12)
plt.ylabel("Product Category", fontsize=12)

plt.gca().invert_yaxis()
plt.grid(axis="x", linestyle="--", alpha=0.4)

# Add value labels
for bar in bars:
    width = bar.get_width()
    plt.text(
        width,
        bar.get_y() + bar.get_height() / 2,
        f"{width:,.0f}",
        va="center",
        fontsize=10
    )

plt.tight_layout()

plt.savefig(
    r"C:\Users\gurra\OneDrive\Desktop\Python project file\images\top_product_categories.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()