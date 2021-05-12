import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("C:/Users/dhrum/Desktop/transactions.csv")
df1=df.groupby(["product_name"], axis=0, as_index=False).sum()
plt.pie(df1['quantity'],labels=df1['product_name'],autopct='%1.1f%%')
plt.show()
