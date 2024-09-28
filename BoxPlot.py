import pandas as pd
import yfinance as yf
from matplotlib import pyplot as plt

df = yf.download("BTC-USD")


df["Date"] = pd.to_datetime(df.index)

df["Month"] = df["Date"].dt.month

print(df.describe())

df.boxplot(column="Close", by="Month")
plt.show()



# plt.subplot(1,2,1)
# plt.plot(df["Close"])
# plt.subplot(1,2,2)
# plt.hist(df["Close"])
# plt.show()
