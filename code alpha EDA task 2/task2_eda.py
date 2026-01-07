import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\mani3\Downloads\large_sales_dataset.csv")

df.head()
df.info()
df.describe()
df.isnull().sum()

df.hist(figsize=(12,8))
plt.show()

corr = df.select_dtypes(include='number').corr()

plt.figure(figsize=(10,6))
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()