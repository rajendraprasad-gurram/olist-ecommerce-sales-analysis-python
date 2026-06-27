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
merged_orders["purchase_year"] = merged_orders["order_purchase_timestamp"].dt.year

revenue_by_year = merged_orders.groupby("purchase_year")["total_value"].sum()

print(revenue_by_year)

plt.figure(figsize=(8, 5))
plt.bar(revenue_by_year.index, revenue_by_year.values)
plt.title("Revenue by Year")
plt.xlabel("Year")
plt.ylabel("Revenue")

# Plot
plt.figure(figsize=(9, 6))

bars = plt.bar(
    revenue_by_year.index,
    revenue_by_year.values
)

plt.title(
    "Revenue by Year",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Year", fontsize=12)
plt.ylabel("Revenue", fontsize=12)

plt.grid(axis="y", linestyle="--", alpha=0.4)

# Add value labels
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:,.0f}",
        ha="center",
        va="bottom",
        fontsize=10
    )

plt.tight_layout()

plt.savefig(
    r"C:\Users\gurra\OneDrive\Desktop\Python project file\images\revenue_by_year.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.tight_layout()
plt.show()
