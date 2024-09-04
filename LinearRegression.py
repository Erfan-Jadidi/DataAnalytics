import numpy as np
from matplotlib import pyplot as plt
import yfinance as yf
from sklearn.linear_model import LinearRegression

df = yf.download("BTC-USD")
df["Tomorrow"] = df["Close"].shift(-1)

df.dropna(inplace=True)

X = df[["Open", "Close", "Low", "High"]]
y = df["Tomorrow"]

model = LinearRegression()
model.fit(X,y)

plt.plot(np.arange(len(X)), y)

prediction = model.predict(X)

plt.plot(np.arange(len(X)), prediction, "g--")

print(model.predict([[150,160,140,200]]))

plt.show()