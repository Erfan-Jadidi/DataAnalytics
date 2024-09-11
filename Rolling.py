import numpy as np
import pandas as pd

X = np.arange(1, 100).reshape(-1, 1)
weights = np.array([50, 2, 3, 4, 5]).reshape(-1, 1)

# data = np.hstack((X, X*10))

# df = pd.DataFrame(data, columns= ["Close", "Open"])

df = pd.DataFrame(X)

my_list = list(df.rolling(5))
# print(my_list)

for item in my_list:
    if len(item) == 5:
        print(item.values * weights)
