import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales.csv")

print(df)

print("Total Sales:", df["Sales"].sum())
print("Average Sales:", df["Sales"].mean())

print("Highest Sales Month:")
print(df.loc[df["Sales"].idxmax()])

category = df.groupby("Category")["Sales"].sum()
print(category)

category.plot(kind="bar")
plt.show()

df.plot(x="Month", y="Sales", kind="line")
plt.show()

category.plot(kind="pie", autopct="%1.1f%%")
plt.show()