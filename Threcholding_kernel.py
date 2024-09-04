import numpy as np
from matplotlib import pyplot as plt

y = np.array([1,2,3,4,5,4,3,2,1,2,3,4,5,4,3,2,1])
X=np.arange(len(y))
kernel = [4,5,4]
kernel_size = len(kernel)
rate = 0.9

plt.plot(X,y)


for i in range(0, len(y) - kernel_size):
    sa = np.sum(np.abs(y[i:i + kernel_size] - kernel))
    # ss = np.sum(np.power(y[i:i + kernel_size] - kernel,2))
    similarity = np.sum(kernel) - sa
    if similarity >= np.sum(kernel) * rate:
        plt.plot(X[i:i+kernel_size],kernel ,"r--"  )



plt.show()