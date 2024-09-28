import numpy as np

X = np.array([0,1,2,3,2,1,0,2,3,2])

for i in range(2,len(X) // 4):
    pattern = ...
    df.rolling(i)
    conv = np.convolve(X, pattern, mode="same")

pattern = np.array([1,1,1])

conv = np.convolve(X, pattern, mode="full")
print(conv)
conv = np.convolve(X, pattern, mode="valid")
print(conv)
conv = np.convolve(X, pattern, mode="same")
print(conv)

