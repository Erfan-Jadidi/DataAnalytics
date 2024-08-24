import numpy as np
import yfinance as yf
from matplotlib import pyplot as plt

btc = yf.download("BTC-USD",start="2024-07-15")
X = np.arange(len(btc))

# X = days
# Y = based on close btc data

plt.plot(X,btc["Close"], label="Close Price")

# a|x1,y1
# b|x2,y2

plt.legend()
plt.show()