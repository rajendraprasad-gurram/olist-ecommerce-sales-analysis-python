import pandas as pd
import matplotlib.pyplot as plt

orders = pd.read_csv(
    r"C:\Users\gurra\OneDrive\Desktop\Python project file\data\olist_orders_dataset.csv"
)

date_columns = [
    "order_delivered_customer_date",
    "order_estimated_delivery_date"
]

for column in date_columns:
    orders[column] = pd.to_datetime(orders[column])

orders["delay_days"] = (
    orders["order_delivered_customer_date"] -
    orders["order_estimated_delivery_date"]
).dt.days

delay_data = orders["delay_days"].dropna()

print(delay_data.describe())

plt.figure(figsize=(10, 5))
plt.hist(delay_data, bins=40)

plt.title("Delivery Delay Distribution")
plt.xlabel("Delay Days")
plt.ylabel("Number of Orders")

plt.tight_layout()
plt.show()