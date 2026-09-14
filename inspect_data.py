import pandas as pd

# Load the Excel dataset
df = pd.read_excel("sample_-_superstore.xls")

# Display basic information
print("First 5 rows:")
print(df.head())

print("\nDataset shape:")
print(df.shape)

print("\nColumn names:")
print(df.columns.tolist())

print("\nMissing values:")
print(df.isnull().sum())

print("\nData types:")
print(df.dtypes)

print("Total Sales:", df["Sales"].sum())
print("Total Profit:", df["Profit"].sum())
print("Total Quantity Sold:", df["Quantity"].sum())
print("Average Discount:", df["Discount"].mean())

category_summary = df.groupby("Category").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum"),
    Total_Quantity=("Quantity", "sum")
).sort_values(by="Total_Profit", ascending=False)

print(category_summary)

subcategory_summary = df.groupby("Sub-Category").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum"),
    Total_Quantity=("Quantity", "sum")
).sort_values(by="Total_Profit")

print(subcategory_summary)

region_summary = df.groupby("Region").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum"),
    Total_Quantity=("Quantity", "sum")
).sort_values(by="Total_Profit", ascending=False)

print(region_summary)

discount_summary = df.groupby("Discount").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum"),
    Average_Profit=("Profit", "mean"),
    Orders=("Order ID", "count")
).sort_index()

print(discount_summary)

state_summary = df.groupby("State/Province").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum")
).sort_values(by="Total_Profit")

print(state_summary.head(10))

import matplotlib.pyplot as plt
import seaborn as sns

# Profit by category
category_summary["Total_Profit"].plot(
    kind="bar",
    color=["#2E86AB", "#3CAEA3", "#F6C85F"]
)
plt.title("Total Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit ($)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# Profit by region
region_summary["Total_Profit"].plot(
    kind="bar",
    color="#2E86AB"
)
plt.title("Total Profit by Region")
plt.xlabel("Region")
plt.ylabel("Profit ($)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# Profit by discount
discount_summary["Total_Profit"].plot(
    kind="line",
    marker="o",
    color="#E74C3C"
)
plt.title("Effect of Discount on Total Profit")
plt.xlabel("Discount Rate")
plt.ylabel("Profit ($)")
plt.axhline(0, color="black", linewidth=1)
plt.tight_layout()
plt.show()
