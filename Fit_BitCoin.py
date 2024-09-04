import numpy as np
from matplotlib import pyplot as plt
import yfinance as yf

df = yf.download("BTC-USD")

X = np.arange(len(df))
y = df["Close"]


cost_function = []

# tune up
# for i in range(1,20):
#     model = np.poly1d(np.polyfit(X, y, i))
#     h = model(X)
#     print(model(270))
#     plt.plot(X, h,label=str(i))
    # root_mean_squared_error = np.sqrt(np.mean(np.power(h - y, 2)))
    # cost_function.append(root_mean_squared_error)


# plt.scatter(np.arange(1,20), cost_function)

plt.plot(X,y)
model = np.poly1d(np.polyfit(X[:1000], y[:1000], 16))
h = model(X[:1000])
plt.plot(X[:1000],h)

plt.legend()
plt.show()