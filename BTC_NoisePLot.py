import numpy as np
import yfinance as yf
from matplotlib import pyplot as plt

# y = np.array([198, 195, 202, 189, 165, 178, 184, 190, 225])
# X = np.arange(len(y))

y = yf.download("BTC-USD",start="2024-07-15")
X = np.arange(len(y))

mean = y["Close"].mean()
std = np.std(y["Close"])

plt.plot(X,y["Close"], label="Close Price")
plt.plot([0,X.max()] , [mean,mean],"g--",label= "Mean")
plt.plot([0,X.max()] , [mean+std,mean+std],"r--",label= "Mean+Std")
plt.plot([0,X.max()] , [mean-std,mean-std],"r--",label= "Mean-Std")

# Noise it is just like std but multiply by 2
# because some parts are important
plt.plot([0,X.max()] , [mean+std*2,mean+std*2],"r--",label= "Noise - Mean+Std")
plt.plot([0,X.max()] , [mean-std*2,mean-std*2],"r--",label= "Noise - Mean-Std")

plt.legend()
plt.show()