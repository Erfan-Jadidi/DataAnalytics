import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv("BTC-USD.csv")
df["sma_7"] = df["Close"].rolling(7).mean()
df["sma_14"] = df["Close"].rolling(14).mean()
df["sma_28"] = df["Close"].rolling(28).mean()
df["ema_28"] = df["Close"].ewm(span=28).mean()

# df.to_excel("result.xlsx")

plt.plot(df["Close"],label="close")
plt.plot(df["sma_7"],label="sma_7")
plt.plot(df["sma_14"],label="sma_14")
plt.plot(df["sma_28"],label="sma_28")
plt.plot(df["ema_28"],label="ema_28")
plt.legend()
plt.show()

# df = pd.read_csv("sell.csv")
# simple_moving_average_3 = df["amount"].rolling(3).mean()     #sma-3
# simple_moving_average_7 = df["amount"].rolling(7).mean()     #sma-7
# simple_moving_average_14 = df["amount"].rolling(14).mean()    #sma-14
# simple_moving_average_21 = df["amount"].rolling(21).mean()    #sma-12
# simple_moving_average = df["amount"].rolling(50).mean()    #sma-50
# simple_moving_average = df["amount"].rolling(100).mean()   #sma-100
