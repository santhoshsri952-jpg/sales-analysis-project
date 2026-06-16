import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales.csv")

print(df)

print("\nTotal Sales:")
print(df["Sales"].sum())

print("\nSales by City:")
print(df.groupby("City")["Sales"].sum())

city_sales = df.groupby("City")["Sales"].sum()

city_sales.plot(kind="bar")

plt.title("Sales by City")
plt.xlabel("City")
plt.ylabel("Sales")

plt.show()