import numpy as np
from matplotlib import pyplot as plt

X = np.array([100, 110, 170, 200, 220, 300, 360, 370, 400, 420])
y = np.array([80, 100, 160, 170, 250, 265, 330, 340, 370, 400])

model = np.poly1d(np.polyfit(X, y, 6))

h = model(X)

print(model(270))

plt.scatter(X,y)
plt.plot(X, h)
plt.show()