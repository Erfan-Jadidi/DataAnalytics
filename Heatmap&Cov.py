import yfinance as yf
import seaborn as sns
from matplotlib import pyplot as plt

# now we have covariance matrix

btc = yf.download("BTC-USD")

print(btc.corr())
print(btc)
sns.heatmap(btc.corr(), cmap="coolwarm", annot=True, fmt=".4f")
plt.show()