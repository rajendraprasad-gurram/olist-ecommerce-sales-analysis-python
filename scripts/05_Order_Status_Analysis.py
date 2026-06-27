import pandas as pd
import matplotlib.pyplot as plt

orders = pd.read_csv(
    r"C:\Users\gurra\OneDrive\Desktop\Python project file\data\olist_orders_dataset.csv"
)

order_status = orders["order_status"].value_counts()

print(order_status)

plt.figure(figsize=(10,5))

plt.barh(
    order_status.index,
    order_status.values
)

plt.title("Order Status Distribution")
plt.xlabel("Number of Orders")
plt.ylabel("Order Status")

plt.tight_layout()

plt.savefig(
    r"C:\Users\gurra\OneDrive\Desktop\Python project file\images\order_status_distribution.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()
