import numpy as np
from matplotlib import pyplot as plt

X = np.array([1,1,2,2,4,2,2,1,1]*5)
n = len(X)

pattern = np.array([1,1,2,2,4,2,2,1,1])
pattern_len = len(pattern)
pattern_sum = np.sum(pattern)
coef = 0.99

sse_list = []

for i in range(n-pattern_len + 1):
    part = X[i:i+pattern_len]
    sse = np.sum(np.power(part - pattern, 2))
    sse_list.append(pattern_sum - sse)
    print(pattern_sum - sse)
    if sse > pattern_sum * coef:
        print(i)

plt.subplot(2,1,1)
plt.plot(X)

plt.subplot(2,1,2)
plt.plot(sse_list)
plt.show()
print(sse_list.count(16))
# 16 is the number to check if there exsist an pattern