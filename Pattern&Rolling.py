import numpy as np
import pandas as pd

df = pd.DataFrame(np.array([1,1,2,2,4,2,2,1,1]*5))
df.columns = ["Data"]

n = len(df)
pattern_len = 9

coef = 0.7

sse_list = []
for x in list(df["Data"].rolling(9))[8:]:

    pattern = x.values
    pattern_sum = np.sum(pattern)
    for i in range(n - pattern_len):
        part = df.iloc[i:i + pattern_len].values
        sse = np.sum(np.power(part - pattern, 2))
        if sse > pattern_sum * coef:
            sse_list.append(1)
            print(i, i + pattern_len)
        else:
            sse_list.append(0)



    print(pattern, len(sse_list))
    sse_list = []



