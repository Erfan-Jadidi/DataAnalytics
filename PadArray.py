import numpy as np
from matplotlib import pyplot as plt

X = np.array([10,6,8,3])

y = np.diff(np.pad(X,[1,0],  mode="constant", constant_values=0))

plt.plot(X)
plt.plot(0-X)
# plt.plot(0-y)
plt.show()


# numbers = np.array([10,8,14,9,17])

# print(np.pad(numbers, [3, 5], mode="constant", constant_values=[2,4]))
# print(np.pad(numbers, [3, 5], mode="edge"))
# print(np.pad(numbers, [3, 5], mode="reflect"))
# print(np.pad(numbers, [3, 9], mode="linear_ramp"))

# plt.plot(np.pad(numbers, [3, 9], mode="linear_ramp"))
# plt.show()