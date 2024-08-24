import numpy as np
import yfinance as yf
from matplotlib import pyplot as plt

btc = yf.download("BTC-USD",start="2024-07-15")
X = np.arange(len(btc))

# X = days
# Y = based on close btc data

plt.plot(X,btc["Close"], label="Close Price")

std = np.std(btc["Close"])

mean = btc["Close"].mean()
plt.plot([0,X.max()] , [mean,mean],"g--",label= "Mean")
plt.plot([0,X.max()] , [mean+std,mean+std],"r--",label= "Mean+Std")
plt.plot([0,X.max()] , [mean-std,mean-std],"r--",label= "Mean-Std")

plt.legend()
plt.show()