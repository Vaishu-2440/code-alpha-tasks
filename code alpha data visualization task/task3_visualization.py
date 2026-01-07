import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("data.csv")

# Line chart
plt.figure()
plt.plot(df["Year"], df["Sales"], marker='o')
plt.title("Sales Trend Over Years")
plt.xlabel("Year")
plt.ylabel("Sales")
plt.savefig("images/line_chart.png")
plt.show()

# Bar chart
plt.figure()
plt.bar(df["Year"], df["Profit"])
plt.title("Profit Comparison by Year")
plt.xlabel("Year")
plt.ylabel("Profit")
plt.savefig("images/bar_chart.png")
plt.show()
