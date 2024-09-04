import matplotlib.pyplot as plt
import numpy as np
from sympy import diff, symbols

# x,y = symbols(["x","y"])
# f = pow(x, 2) + pow(y, 2)

# print(diff(f))


point_1 = (20,30)
point_2 = (80,60)

plt.xlim(0,100)
plt.ylim(0,100)

plt.plot([point_1[0], point_2[0]],[point_1[1], point_2[1]])

# np.gradient(point_1[0],point_2[0],point_1[1],point_2[1])

plt.show()