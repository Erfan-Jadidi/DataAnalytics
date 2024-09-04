from matplotlib import pyplot as plt
from sklearn.preprocessing import StandardScaler
import yfinance as yf

btc  = yf.download("BTC-USD", start="2021-01-01")
eth  = yf.download("ETH-USD", start="2021-01-01")

btc_close = btc["Close"].values.reshape(-1,1)
eth_close = eth["Close"].values.reshape(-1,1)

# normalized X = (X-mean) / std     mean=0, std=1
scaler=StandardScaler()

btc_close = scaler.fit_transform(btc_close)
eth_close = scaler.fit_transform(eth_close)

plt.subplot(2, 1, 1)
plt.plot(btc_close, "r", label="normalized btc close")
plt.plot(eth_close, label="normalized eth close")
plt.legend()


plt.subplot(2, 1, 2)
plt.plot(btc, "r")
plt.plot(eth, "b")

plt.show()